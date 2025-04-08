import csv
import json
import os
from typing import Dict, Tuple
from WorldParser import WorldParser


class CheckParser:
    def __init__(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "./TPGC US Check Flags.csv")
        with open(file_path, "r") as f:
            self.reader = csv.reader(f)
            next(self.reader)  # Skip header
            self.check_flags = {
                row[0]: {
                    "address": row[1],
                    "flag": row[2],
                    "is_region_flag": True if row[3] != "" else False,
                    "save_file_region": row[4] if row[4] != "" else None,
                    "enabled": True,
                    # "note": row[5],
                }
                for row in self.reader
            }

        file_path = os.path.join(current_folder, "./json/CheckFlags.json")
        with open(file_path, "r") as f:
            self.json_flags = json.load(f)

        self.world_parser = WorldParser()

    def get_check_address_and_flag(self, check_name: str) -> Tuple[str, str]:
        address_str = self.check_flags[check_name]["address"]
        flag_str = self.check_flags[check_name]["flag"]

        # Check if the address is valid before conversion
        if address_str == "Not added yet":
            return None, None

        if self.check_flags[check_name]["is_region_flag"]:
            return (
                int(self.check_flags[check_name]["save_file_region"], 16)
                + int(address_str, 16),
                flag_str,
            )
        else:
            return (
                int(address_str, 16),
                flag_str,
            )

    def create_check_dict_file(self) -> None:
        file_content = "from typing import Dict, Tuple\n\ncheck_dict: Dict[str, Tuple[int, int, bool]] = {\n"

        for check_name, check_data in self.check_flags.items():
            address, flag = self.get_check_address_and_flag(check_name)
            file_content += f'\t"{check_name}": ({address}, {flag}, False),\n'

        file_content += "}\n"

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "files/CheckDict.py")

        with open(file_path, "w") as f:
            f.write(file_content)

    def validate_check_names(self) -> None:

        invalid_checks = []

        def append(check_name: str, check_data: Dict[str, any], dungeon_name: str):
            if check_name not in self.check_flags:
                invalid_checks.append(check_name)

        self.world_parser.func_over_all_checks(append)

        if invalid_checks:
            print(f"Invalid checks: {invalid_checks}")

    def create_check_json_file(self) -> None:
        file_content = json.dumps(self.check_flags, indent=4)

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "json/CheckFlags.json")

        with open(file_path, "w") as f:
            f.write(file_content)

    def create_region_list(self) -> None:
        regions = set()
        for check_name in self.json_flags:
            if self.json_flags[check_name]["enabled"]:
                regions.add(self.json_flags[check_name]["save_file_region"])

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "json/regions.json")

        with open(file_path, "w") as f:
            f.write(str(regions))


if __name__ == "__main__":
    check_parser = CheckParser()
    # check_parser.create_check_dict_file()
    # check_parser.validate_check_names()
    # check_parser.create_check_json_file()
    check_parser.create_region_list()
