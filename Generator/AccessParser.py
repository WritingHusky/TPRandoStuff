import json
import os
from typing import Dict

from WorldParser import WorldParser


class AccessParser:

    def __init__(self):
        self.world_parser = WorldParser()
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "./json/AccessRules.json")
        with open(file_path, "r") as f:
            self.access_rules = json.load(f)

    def create_access_rules_file(self):
        requirements = set()
        glitched_requirements = set()

        def check(check_name: str, check_data: Dict, region: str) -> None:
            if "requirements" in check_data:
                requirements.add(check_data["requirements"])
            if "glitchedRequirements" in check_data:
                glitched_requirements.add(check_data["glitchedRequirements"])

        def room(room_data: Dict, region: str) -> None:
            if "Exits" in room_data:
                for exit_data in room_data["Exits"]:
                    if "Requirements" in exit_data:
                        requirements.add(exit_data["Requirements"])
                    if "GlitchedRequirements" in exit_data:
                        glitched_requirements.add(exit_data["GlitchedRequirements"])

        self.world_parser.func_over_all_checks(check)
        self.world_parser.func_over_all_rooms(room)

        glitched_requirements.difference_update(requirements)

        parsed_requirements = set()
        for rule in requirements:
            for rule_part in self.split_out_brackets(rule):
                if rule_part in ["", "(", ")", "and", "or"]:
                    continue
                for number in range(2, 10):
                    if str(number) in rule_part:
                        rule_part = rule_part.replace(str(number), "1")
                parsed_requirements.add(rule_part)

        parsed_glitched_requirements = set()
        for rule in glitched_requirements:
            for rule_part in self.split_out_brackets(rule):
                if rule_part in ["", "(", ")", "and", "or"]:
                    continue
                for number in range(2, 10):
                    if str(number) in rule_part:
                        rule_part = rule_part.replace(str(number), "1")
                parsed_glitched_requirements.add(rule_part)

        parsed_glitched_requirements.difference_update(parsed_requirements)

        access_data = dict()
        access_data["requirements"] = [[req, ""] for req in parsed_requirements]
        access_data["glitched requirements"] = [
            [req, ""] for req in parsed_glitched_requirements
        ]

        # Load existing rules if they exist
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "./json/AccessRules.json")
        existing_rules = {}
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                existing_rules = json.load(f)

        # Convert existing rules to sets for easier comparison
        existing_req_set = {rule[0] for rule in existing_rules.get("requirements", [])}
        existing_glitched_req_set = {
            rule[0] for rule in existing_rules.get("glitched requirements", [])
        }

        # Only add new requirements that don't already exist
        new_requirements = [
            [req, ""] for req in parsed_requirements if req not in existing_req_set
        ]
        new_glitched_requirements = [
            [req, ""]
            for req in parsed_glitched_requirements
            if req not in existing_glitched_req_set
        ]

        # Combine existing and new rules
        if existing_rules:
            access_data["requirements"] = (
                existing_rules["requirements"] + new_requirements
            )
            access_data["glitched requirements"] = (
                existing_rules["glitched requirements"] + new_glitched_requirements
            )

        with open(file_path, "w") as f:
            json.dump(access_data, f, indent=4)

    def convert_access_rule(self, rule: str):
        """
        updates the rule to the new format
        """
        # Break the rule into parts
        split_rule = self.split_out_brackets(rule)

        # Check if split_rule is empty
        if not split_rule:
            return ""  # or handle it as needed

        converted_rule = ""
        for element in split_rule:
            if element in ["", "(", ")"]:
                converted_rule += element
                continue
            if element in ["and", "or"]:
                converted_rule += f" {element} "
                continue
            number = None
            # if the element has a number, save it to replace it later
            if any(char.isdigit() for char in element):
                number = int(next(char for char in element if char.isdigit()))
                element = element.replace(str(number), "1")

            # search for the rule in the access rules and replace it with the new format
            for new_rule in self.access_rules["requirements"]:
                if new_rule[0] == element:
                    element = new_rule[1]
                    if number:
                        element = element.replace("1", str(number))
                    break
            for new_rule in self.access_rules["glitched requirements"]:
                if new_rule[0] == element:
                    element = new_rule[1]
                    if number:
                        element = element.replace("1", str(number))
                    break
            converted_rule += element
        return converted_rule

    def split_out_brackets(self, rule: str) -> list[str]:
        result = []
        buffer = ""
        i = 0
        while i < len(rule):
            char = rule[i]
            if char in "()":
                if buffer:
                    result.append(buffer.strip())
                    buffer = ""
                result.append(char)
            elif rule[i : i + 5] == " and ":
                if buffer:
                    result.append(buffer.strip())
                    buffer = ""
                result.append("and")
                i += 4  # Skip the next four characters
            elif rule[i : i + 4] == " or ":
                if buffer:
                    result.append(buffer.strip())
                    buffer = ""
                result.append("or")
                i += 3  # Skip the next three characters
            else:
                buffer += char
            i += 1
        if buffer:
            result.append(buffer.strip())

        # Process commas and remove surrounding brackets
        for i in range(len(result)):
            if "," in result[i]:
                # Check if surrounded by brackets
                if (
                    i > 0
                    and i < len(result) - 1
                    and result[i - 1] == "("
                    and result[i + 1] == ")"
                ):
                    # Remove the brackets
                    result[i - 1] = ""
                    result[i + 1] = ""

        # Remove empty strings from the result
        result = [x for x in result if x]
        return result

    def validate_access_rules(self):
        # Look at the access rules and see if they are valid (i.e. the rules are not empty)
        self.__init__()
        if (
            not self.access_rules["requirements"]
            or not self.access_rules["glitched requirements"]
        ):
            return False
        for rule in self.access_rules["requirements"]:
            if rule[1] == "":
                return False
        for rule in self.access_rules["glitched requirements"]:
            if rule[1] == "":
                return False
        return True


if __name__ == "__main__":
    access_parser = AccessParser()
    access_parser.create_access_rules_file()
