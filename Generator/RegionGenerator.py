import os
from typing import Dict
from AccessParser import AccessParser
from WorldParser import WorldParser


class RegionGenerator:
    def __init__(self):
        self.world_parser = WorldParser()
        self.access_parser = AccessParser()

    def location_to_region_map(self):
        self.map_content = "LOCATION_TO_REGION: dict[str, str] = {"

        def append(room_data: dict, region: str):
            room_name = room_data["RoomName"]
            room_checks = room_data["Checks"]
            if "" in room_checks:
                self.map_content += f'\n# "" : "{room_name}",'
                return
            for check in room_checks:
                self.map_content += f'\n"{check}" : "{room_name}",'

        self.world_parser.func_over_all_rooms(append)

        self.map_content += "\n}"
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "files/RegionMap.py")

        with open(file_path, "w") as f:
            f.write(self.map_content)

    def generate_region_creation(self):
        self.file_content = CREATION_HEADER

        def append(room_data: Dict, region: str) -> None:
            room_name = room_data["RoomName"]
            room_checks = room_data["Checks"]
            enum_name = room_name.replace(" ", "_").upper().replace("-", "_")

            variable_name = room_name.replace(" ", "_").lower().replace("-", "_")
            # First create the region
            self.file_content += f"""
    {variable_name} = Region(RoomName.{enum_name}, player, world)
    regions[RoomName.{enum_name}] = {variable_name}
    world.regions.append({variable_name})
"""
            for check in room_checks:
                if check != "":
                    check_name = check.upper().replace(" ", "_").replace("-", "_")
                    self.file_content += f"""
    {variable_name}.locations.append(
    TPLocation(
        player,
        CheckName.{check_name},
        {variable_name},
        LOCATION_TABLE[CheckName.{check_name}]
      )
    )
"""

        self.world_parser.func_over_all_rooms(append)

        self.file_content += """# Connect Menu to starting region
    menu.connect(regions[RoomName.OUTSIDE_LINKS_HOUSE])
    
def create_portal_location(world: MultiWorld, player: int):
    if CheckName.SNOWPEAK_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.SNOWPEAK_SUMMIT_UPPER, player).locations.append(
            TPLocation(
                player,
                CheckName.SNOWPEAK_PORTAL,
                world.get_region(RoomName.SNOWPEAK_SUMMIT_UPPER, player),
                LOCATION_TABLE[CheckName.SNOWPEAK_PORTAL],
            )
        )
    if CheckName.ZORAS_DOMAIN_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.ZORAS_DOMAIN_THRONE_ROOM, player).locations.append(
            TPLocation(
                player,
                CheckName.ZORAS_DOMAIN_PORTAL,
                world.get_region(RoomName.ZORAS_DOMAIN_THRONE_ROOM, player),
                LOCATION_TABLE[CheckName.ZORAS_DOMAIN_PORTAL],
            )
        )
    if CheckName.UPPER_ZORAS_RIVER_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.UPPER_ZORAS_RIVER, player).locations.append(
            TPLocation(
                player,
                CheckName.UPPER_ZORAS_RIVER_PORTAL,
                world.get_region(RoomName.UPPER_ZORAS_RIVER, player),
                LOCATION_TABLE[CheckName.UPPER_ZORAS_RIVER_PORTAL],
            )
        )
    if CheckName.LAKE_HYLIA_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.LAKE_HYLIA, player).locations.append(
            TPLocation(
                player,
                CheckName.LAKE_HYLIA_PORTAL,
                world.get_region(RoomName.LAKE_HYLIA, player),
                LOCATION_TABLE[CheckName.LAKE_HYLIA_PORTAL],
            )
        )
    if CheckName.CASTLE_TOWN_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player).locations.append(
            TPLocation(
                player,
                CheckName.CASTLE_TOWN_PORTAL,
                world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player),
                LOCATION_TABLE[CheckName.CASTLE_TOWN_PORTAL],
            )
        )
    if CheckName.GERUDO_DESERT_PORTAL in LOCATION_TABLE:
        world.get_region(
            RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU, player
        ).locations.append(
            TPLocation(
                player,
                CheckName.GERUDO_DESERT_PORTAL,
                world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU, player),
                LOCATION_TABLE[CheckName.GERUDO_DESERT_PORTAL],
            )
        )
    if CheckName.SACRED_GROVE_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.SACRED_GROVE_LOWER, player).locations.append(
            TPLocation(
                player,
                CheckName.SACRED_GROVE_PORTAL,
                world.get_region(RoomName.SACRED_GROVE_LOWER, player),
                LOCATION_TABLE[CheckName.SACRED_GROVE_PORTAL],
            )
        )
    if CheckName.NORTH_FARON_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.NORTH_FARON_WOODS, player).locations.append(
            TPLocation(
                player,
                CheckName.NORTH_FARON_PORTAL,
                world.get_region(RoomName.NORTH_FARON_WOODS, player),
                LOCATION_TABLE[CheckName.NORTH_FARON_PORTAL],
            )
        )
    if CheckName.SOUTH_FARON_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.SOUTH_FARON_WOODS, player).locations.append(
            TPLocation(
                player,
                CheckName.SOUTH_FARON_PORTAL,
                world.get_region(RoomName.SOUTH_FARON_WOODS, player),
                LOCATION_TABLE[CheckName.SOUTH_FARON_PORTAL],
            )
        )
    if CheckName.KAKARIKO_VILLAGE_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).locations.append(
            TPLocation(
                player,
                CheckName.KAKARIKO_VILLAGE_PORTAL,
                world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
                LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_PORTAL],
            )
        )
    if CheckName.BRIDGE_OF_ELDIN_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.ELDIN_FIELD, player).locations.append(
            TPLocation(
                player,
                CheckName.BRIDGE_OF_ELDIN_PORTAL,
                world.get_region(RoomName.ELDIN_FIELD, player),
                LOCATION_TABLE[CheckName.BRIDGE_OF_ELDIN_PORTAL],
            )
        )
    if CheckName.KAKARIKO_GORGE_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.KAKARIKO_GORGE, player).locations.append(
            TPLocation(
                player,
                CheckName.KAKARIKO_GORGE_PORTAL,
                world.get_region(RoomName.KAKARIKO_GORGE, player),
                LOCATION_TABLE[CheckName.KAKARIKO_GORGE_PORTAL],
            )
        )
    if CheckName.DEATH_MOUNTAIN_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.DEATH_MOUNTAIN_VOLCANO, player).locations.append(
            TPLocation(
                player,
                CheckName.DEATH_MOUNTAIN_PORTAL,
                world.get_region(RoomName.DEATH_MOUNTAIN_VOLCANO, player),
                LOCATION_TABLE[CheckName.DEATH_MOUNTAIN_PORTAL],
            )
        )
    
    if CheckName.MIRROR_CHAMBER_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.MIRROR_CHAMBER_UPPER, player).locations.append(
            TPLocation(
                player,
                CheckName.MIRROR_CHAMBER_PORTAL,
                world.get_region(RoomName.MIRROR_CHAMBER_UPPER, player),
                LOCATION_TABLE[CheckName.MIRROR_CHAMBER_PORTAL],
            )
        )

    if CheckName.ORDON_SPRING_PORTAL in LOCATION_TABLE:
        world.get_region(RoomName.ORDON_SPRING, player).locations.append(
            TPLocation(
                player,
                CheckName.ORDON_SPRING_PORTAL,
                world.get_region(RoomName.ORDON_SPRING, player),
                LOCATION_TABLE[CheckName.ORDON_SPRING_PORTAL],
            )
        )"""

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "files/RegionCreation.py")

        with open(file_path, "w") as f:
            f.write(self.file_content)

    def generate_region_connections(self):
        self.file_content = CONNECTION_HEADER

        def append(room_data: Dict, region: str) -> None:
            room_name = room_data["RoomName"]
            room_exits = room_data["Exits"]
            enum_name = room_name.replace(" ", "_").upper().replace("-", "_")

            for exit in room_exits:
                exit_name = exit["ConnectedArea"]
                exit_enum_name = exit_name.replace(" ", "_").upper().replace("-", "_")
                self.file_content += f"""
    world.get_region(RoomName.{enum_name}, player).connect(
        world.get_region(RoomName.{exit_enum_name}, player),
        f"{{RoomName.{enum_name}}} -> {{RoomName.{exit_enum_name}}}"
    )
"""

        self.world_parser.func_over_all_rooms(append)

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "files/RegionConnections.py")

        with open(file_path, "w") as f:
            f.write(self.file_content)

    def generate_region_rules(self):
        self.file_content = RULES_HEADER

        def append(room_data: Dict, region: str) -> None:
            room_name = room_data["RoomName"]
            room_exits = room_data["Exits"]
            enum_name = room_name.replace(" ", "_").upper().replace("-", "_")

            for exit in room_exits:
                requirement = exit["Requirements"]
                if requirement != "":
                    exit_enum_name = (
                        exit["ConnectedArea"]
                        .replace(" ", "_")
                        .upper()
                        .replace("-", "_")
                    )
                    self.file_content += f"""
    exit = world.get_entrance(f"{{RoomName.{enum_name}}} -> {{RoomName.{exit_enum_name}}}")
    set_rule(
        exit,
          lambda state: ({self.access_parser.convert_access_rule(requirement)}),
    )
"""
                    # If the requirement contains "RoomName", we need to register an indirect condition as per world generation rules
                    # Currently, this does not fire but future logic may require it
                    if "RoomName" in requirement:
                        self.file_content += f"""
    # world.register_indirect_condition(world.get_region(RoomName.{{{exit_enum_name}}}), exit)
"""

        self.world_parser.func_over_all_rooms(append)

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "files/RegionRules.py")

        with open(file_path, "w") as f:
            f.write(self.file_content)


CREATION_HEADER = """from typing import Dict
from BaseClasses import MultiWorld, Region
from .Locations import TPLocation, LOCATION_TABLE
from .Enums import RoomName, CheckName


def create_regions(world: MultiWorld, player: int) -> Dict[str, Region]:
    regions = {}

    # Create Menu region
    menu = Region("Menu", player, world)
    regions["Menu"] = menu
    world.regions.append(menu)
"""

CONNECTION_HEADER = """from BaseClasses import MultiWorld
from .Enums import RoomName

def connect_regions(world: MultiWorld, player: int) -> None:
    \"\"\"Connect all regions according to the world layout\"\"\"
"""

RULES_HEADER = """from typing import Callable, Dict
from BaseClasses import CollectionState, MultiWorld, Region, Entrance
from worlds.generic.Rules import set_rule
from .Enums import RoomName, CheckName, ItemList
from .Randomizer.Macros import *
from .options import (
    CastleRequirements,
    DamageMagnification,
    GoronMinesEntrance,
    LogicRules,
    SkipLakebedEntrance,
    SmallKeySettings,
    TotEntrance,
    PalaceRequirements,
)

# Considerations:
# - Look at logic for uncleared twilight provinces as logic may be weird with that


def set_region_access_rules(world: MultiWorld, player: int):

"""

if __name__ == "__main__":
    region_generator = RegionGenerator()
    # region_generator.generate_region_creation()
    # region_generator.generate_region_connections()
    # region_generator.generate_region_rules()
    region_generator.location_to_region_map()
