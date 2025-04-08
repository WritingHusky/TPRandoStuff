import json
from typing import Callable, Dict, List
import os
from pathlib import Path
import re


class WorldParser:

    def __init__(
        self,
    ):
        try:
            current_folder = os.path.dirname(os.path.abspath(__file__))
            world_file_path = os.path.join(current_folder, "./json/combined_world.json")
            with open(world_file_path, "r") as f:
                content = self._strip_comments(f.read())
                self.world_data = json.loads(content)
        except FileNotFoundError:
            self.combine_world_files()

    def _strip_comments(self, text: str) -> str:
        """Remove comments from JSONC text.

        Args:
            text: The JSONC text to process

        Returns:
            Clean JSON string with comments removed
        """
        # Remove single line comments
        text = re.sub(r"//.*$", "", text, flags=re.MULTILINE)

        # Remove multi-line comments
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)

        return text

    def combine_world_files(self, world_folder: str = "World") -> Dict:
        """Combines all the world files into a single dictionary structure.

        Args:
            world_folder: Path to the World folder containing Rooms and Checks

        Returns:
            Dict containing the combined world data
        """
        current_folder = os.path.dirname(os.path.abspath(__file__))
        world_folder_path = (
            Path(current_folder) / world_folder
        )  # Look for "World" folder in the current directory

        combined_data = {
            "Rooms": {"Dungeons": {}, "Overworld": {}},
            "Checks": {"Dungeons": {}, "Overworld": {}},
        }

        # Process Rooms
        rooms_path = Path(world_folder_path) / "Rooms"

        # Process Dungeon Rooms
        dungeons_path = rooms_path / "Dungeons"
        if dungeons_path.exists():
            for dungeon_file in dungeons_path.glob("*.jsonc"):
                # print(dungeon_file.stem)
                with open(dungeon_file, "r") as f:
                    try:
                        content = self._strip_comments(f.read())
                        dungeon_data = json.loads(content)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from file {dungeon_file}: {e}")
                        continue  # Skip this file and continue with the next
                    dungeon_name = dungeon_file.stem
                    combined_data["Rooms"]["Dungeons"][dungeon_name] = dungeon_data

        # Process Overworld Rooms
        overworld_path = rooms_path / "Overworld"
        if overworld_path.exists():
            for region_folder in overworld_path.iterdir():
                if region_folder.is_dir():
                    region_name = region_folder.name
                    combined_data["Rooms"]["Overworld"][region_name] = dict()
                    for room_file in region_folder.glob("*.jsonc"):
                        with open(room_file, "r") as f:
                            content = self._strip_comments(f.read())
                            room_data = json.loads(content)
                            room_name = room_file.stem
                            combined_data["Rooms"]["Overworld"][region_name][
                                room_name
                            ] = room_data
        # Process Checks
        checks_path = Path(world_folder_path) / "Checks"

        # Process Dungeon Checks
        dungeon_checks_path = checks_path / "Dungeons"
        if dungeon_checks_path.exists():
            for dungeon_dir in dungeon_checks_path.iterdir():
                if dungeon_dir.is_dir():
                    dungeon_name = dungeon_dir.name
                    combined_data["Checks"]["Dungeons"][dungeon_name] = {}

                    for check_file in dungeon_dir.glob("*.jsonc"):
                        with open(check_file, "r") as f:
                            content = self._strip_comments(f.read())
                            check_data = json.loads(content)
                            check_name = check_file.stem
                            combined_data["Checks"]["Dungeons"][dungeon_name][
                                check_name
                            ] = check_data

        # Process Overworld Checks
        overworld_checks_path = checks_path / "Overworld"
        if overworld_checks_path.exists():
            for region_dir in overworld_checks_path.iterdir():
                if region_dir.is_dir():
                    region_name = region_dir.name
                    combined_data["Checks"]["Overworld"][region_name] = {}

                    for check_file in region_dir.glob("*.jsonc"):
                        with open(check_file, "r") as f:
                            content = self._strip_comments(f.read())
                            check_data = json.loads(content)
                            check_name = check_file.stem
                            combined_data["Checks"]["Overworld"][region_name][
                                check_name
                            ] = check_data

        # Save combined data
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "./json/combined_world.json")

        with open(file_path, "w") as f:
            json.dump(combined_data, f, indent=4)

        self.world_data = combined_data
        return combined_data

    def func_over_all_checks(self, func: Callable[[str, Dict, str], None]) -> None:
        dungeons = self.world_data.get("Checks", {}).get("Dungeons", {})
        for dungeon_name, dungeon_checks in dungeons.items():
            for check_name, check_data in dungeon_checks.items():
                func(check_name, check_data, dungeon_name)

        overworld = self.world_data.get("Checks", {}).get("Overworld", {})
        for region_name, overworld_checks in overworld.items():
            for check_name, check_data in overworld_checks.items():
                func(check_name, check_data, region_name)

    def func_over_all_rooms(self, func: Callable[[Dict, str], None]) -> None:
        dungeons = self.world_data.get("Rooms", {}).get("Dungeons", {})
        for dungeon_name, dungeon_room_lis in dungeons.items():
            for room_data in dungeon_room_lis:  # dungeon_data is a list
                func(room_data, dungeon_name)

        overworld = self.world_data.get("Rooms", {}).get("Overworld", {})
        for province_name, overworld_province_lis in overworld.items():
            for region_name, region_lis in overworld_province_lis.items():
                for room_data in region_lis:  # region_data is a list
                    func(room_data, region_name)

    def get_all_check_names(self) -> List[str]:
        all_checks = []

        def append(check_name: str, check_data: Dict, region: str) -> None:
            all_checks.append(check_name)

        self.func_over_all_checks(append)
        return all_checks

    def get_all_room_names(self) -> List[str]:
        all_rooms = []

        def append(room_data: Dict, region: str) -> None:
            if "RoomName" in room_data:
                all_rooms.append(room_data["RoomName"])

        self.func_over_all_checks(append)
        return all_rooms


if __name__ == "__main__":
    world_parser = WorldParser()
    world_parser.combine_world_files()
