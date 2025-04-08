import os
import json
from typing import Dict
from AccessParser import AccessParser
from WorldParser import WorldParser


class LocationGenerator:
    def __init__(self):
        self.access_parser = AccessParser()
        self.world_parser = WorldParser()

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "./json/CheckFlags.json")
        with open(file_path, "r") as f:
            self.check_flags = json.load(f)

    def generate_location_rules(self):

        self.file_content = RULES_HEADER

        def append(check_name: str, check_data: Dict, region: str) -> None:
            requirement = check_data["requirements"]
            if "glitchedRequirements" in check_data:
                glitched_requirement = check_data["glitchedRequirements"]
            else:
                glitched_requirement = None

            self.file_content += f"""\n    set_rule_if_exists(\n		CheckName.{self.location_name_to_enum_name(check_name)},\n		lambda state: ({self.access_parser.convert_access_rule(requirement)})"""

            if glitched_requirement and glitched_requirement != requirement:
                self.file_content += f""",\n		lambda state: ({self.access_parser.convert_access_rule(glitched_requirement)})"""

            self.file_content += "\n\t)"

        self.world_parser.func_over_all_checks(append)

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "files/LocationRules.py")

        with open(file_path, "w") as f:
            f.write(self.file_content)

    def location_name_to_enum_name(self, location_name: str) -> str:
        return location_name.replace(" ", "_").upper()

    def create_location_table_file(self):
        self.location_table = ""
        self.location_count = 0

        def append(check_name: str, check_data: Dict, region: str) -> None:
            if check_name not in self.check_flags:
                print(f"check {check_name} not found in check flags")
                return
            if not self.check_flags[check_name]["enabled"]:
                self.location_table += (
                    f'\n\t"{check_name}": TPLocationData(\n\t\tcode=None'
                )
            else:
                self.location_table += (
                    f'\t"{check_name}": TPLocationData(\n\t\tcode={self.location_count}'
                )
                self.location_count += 1

            if "checkCategory" in check_data:
                self.location_table += ", flags = TPFlag.Always"
                for category in check_data["checkCategory"]:
                    match category:
                        case "Dungeon":
                            self.location_table += " | TPFlag.Dungeon"
                        case "Dungeon Reward":
                            self.location_table += " | TPFlag.Dungeon"
                        case "Shop":
                            self.location_table += " | TPFlag.Shop"
                        case "Overworld":
                            self.location_table += " | TPFlag.Overworld"
                        case "Boss":
                            self.location_table += " | TPFlag.Boss"
                        case "Poe":
                            self.location_table += " | TPFlag.Poe"
                        case "Golden Bug":
                            self.location_table += " | TPFlag.Bug"
                        case "Hidden Skill":
                            self.location_table += " | TPFlag.Skill"
                        case "Heart Container":
                            self.location_table += " | TPFlag.Heart"
                        case "Piece of Heart":
                            self.location_table += " | TPFlag.Heart"
                        case "Sky Book":
                            self.location_table += " | TPFlag.Sky_Book"
                        case "Npc":
                            self.location_table += " | TPFlag.Npc"
                if check_name in [
                    "Renados Letter",
                    "Telma Invoice",
                    "Wooden Statue",
                    "Ilia Charm",
                    "Ilia Memory Reward",
                ]:
                    self.location_table += " | TPFlag.Story"

                stage = self.get_stage_id(check_data)
                self.location_table += f", stage_id = {stage}"
            if self.check_flags[check_name]["is_region_flag"]:
                self.location_table += f", type = TPLocationType.Region"
                if (
                    int(self.check_flags[check_name]["save_file_region"], 16)
                    in ADDR_TO_NODE
                ):
                    self.location_table += f", region= {ADDR_TO_NODE[int(self.check_flags[check_name]['save_file_region'],16)]}"
                else:
                    self.location_table += ", region= None"
            else:
                self.location_table += f", type = TPLocationType.Flag, region= None"

            self.location_table += (
                f", offset = {self.check_flags[check_name]['address']}"
            )
            self.location_table += f", bit = {self.check_flags[check_name]['flag']}"

            self.location_table += f"\n\t),"

        self.world_parser.func_over_all_checks(append)

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "files/LocationTable.txt")
        with open(file_path, "w") as f:
            f.write(self.location_table)

    def get_stage_id(self, check_data):
        for category in check_data["checkCategory"]:
            if category in category_to_stage_id:
                return category_to_stage_id[category]
        return "TPStages.Unkown"


RULES_HEADER = """from typing import TYPE_CHECKING, Callable

from BaseClasses import CollectionState, MultiWorld
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import set_rule
from ..options import (
    BigKeySettings,
    LogicRules,
    SmallKeySettings,
    TotEntrance,
)
from ..Enums import CheckName, ItemList, RoomName
from .Macros import *
from ..Locations import LOCATION_TABLE

if TYPE_CHECKING:
    from .. import TPWorld

class TPLogic(LogicMixin):

    multiworld: MultiWorld

    def _tp_glitched(self, player: int) -> bool:
        return (
            self.multiworld.worlds[player].options.logic_rules.value
            == LogicRules.option_glitched
        )

    def _tp_shops_shuffled(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.shop_items_shuffled.value

    def _tp_is_small_keysy(self, player: int) -> bool:
        return (
            self.multiworld.worlds[player].options.small_key_settings.value
            == SmallKeySettings.option_keysy
        )
    def _tp_is_big_keysy(self, player: int) -> bool:
        return (
            self.multiworld.worlds[player].options.big_key_settings.value
            == BigKeySettings.option_keysy
        )
    
    def _tp_small_key_settings(self, player: int) -> int:
        return self.multiworld.worlds[player].options.small_key_settings.value
    
    def _tp_big_key_settings(self, player: int) -> int:
        return self.multiworld.worlds[player].options.big_key_settings.value


    def _tp_skip_prologue(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.skip_prologue.value

    def _tp_skip_mdh(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.skip_mdh.value

    def _tp_faron_twilight_cleared(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.faron_twilight_cleared.value

    def _tp_eldin_twilight_cleared(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.eldin_twilight_cleared.value

    def _tp_lanayru_twilight_cleared(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.lanayru_twilight_cleared.value

    def _tp_skip_arbiters_entrance(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.skip_arbiters_grounds_entrance.value

    def _tp_skip_lakebed_entrance(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.skip_lakebed_entrance.value

    def _tp_skip_city_in_the_sky_entrance(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.skip_city_in_the_sky_entrance.value

    def _tp_skip_snowpeak_entrance(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.skip_snowpeak_entrance.value

    def _tp_tot_entrance(self, player: int) -> int:
        return self.multiworld.worlds[player].options.tot_entrance.value

    def _tp_palace_requirements(self, player: int) -> int:
        return self.multiworld.worlds[player].options.palace_requirements.value

    def _tp_castle_requirements(self, player: int) -> int:
        return self.multiworld.worlds[player].options.castle_requirements.value

    def _tp_goron_mines_enterance(self, player: int) -> int:
        return self.multiworld.worlds[player].options.goron_mines_entrance.value

    def _tp_faron_woods_logic(self, player: int) -> int:
        return self.multiworld.worlds[player].options.faron_woods_logic.value

    def _tp_open_map(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.open_map.value

    def _tp_barren_dungeons(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.barren_dungeons.value

    def _tp_increase_wallet(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.increase_wallet.value

    def _tp_bonks_do_damage(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.bonks_do_damage.value

    def _tp_damage_magnification(self, player: int) -> int:
        return self.multiworld.worlds[player].options.damage_magnification.value

    def _tp_transform_anywhere(self, player: int) -> bool:
        return self.multiworld.worlds[player].options.transform_anywhere.value


def set_location_access_rules(world: "TPWorld"):

    def set_rule_if_exists(
        location_name: str,
        rule: Callable[[CollectionState], bool],
        glitched_rule: Callable[[CollectionState], bool] = None,
    ) -> None:
        # Only worry about logic if the location can be a progress item (and location_name not in world.nonprogress_locations) do not worry bout yet
        if (location_name in LOCATION_TABLE):
            if world.options.logic_rules.value == LogicRules.option_glitched:
                set_rule(world.get_location(location_name), glitched_rule)
            else:
                set_rule(world.get_location(location_name), rule)
        else:
            raise Exception(f"Location {location_name} not found in location table")

    player = world.player
"""

category_to_stage_id = {
    "Lakebed Temple": "TPStages.Lakebed_Temple",
    "Goron Mines": "TPStages.Goron_Mines",
    "Forest Temple": "TPStages.Forest_Temple",
    "Temple of Time": "TPStages.Temple_of_Time",
    "City in the Sky": "TPStages.City_in_the_Sky",
    "Palace of Twilight": "TPStages.Palace_of_Twilight",
    "Hyrule Castle": "TPStages.Hyrule_Castle",
    "Arbiters Grounds": "TPStages.Arbiters_Grounds",
    "Snowpeak Ruins": "TPStages.Snowpeak_Ruins",
    "Lanayru Ice Puzzle Cave": "TPStages.Lanayru_Ice_Puzzle_Cave",
    "Cave of Ordeals": "TPStages.Cave_of_Ordeals",
    "Eldin Lantern Cave": "TPStages.Eldin_Long_Cave",
    "Lake Lantern Cave": "TPStages.Lake_Hylia_Long_Cave",
    "Eldin Stockcave": "TPStages.Eldin_Goron_Stockcave",
    "Grotto 1": "TPStages.Grotto_1",
    "Grotto 2": "TPStages.Grotto_2",
    "Grotto 3": "TPStages.Grotto_3",
    "Grotto 4": "TPStages.Grotto_4",
    "Grotto 5": "TPStages.Grotto_5",
    "Faron Woods Cave": "TPStages.Faron_Woods_Cave",
    "Ordon Ranch": "TPStages.Ordon_Ranch",
    "Ordon Village": "TPStages.Ordon_Village",
    "Ordon Spring": "TPStages.Ordon_Spring",
    "Faron Woods": "TPStages.Faron_Woods",
    "Kakariko Village": "TPStages.Kakariko_Village",
    "Death Mountain": "TPStages.Death_Mountain",
    "Kakariko Graveyard": "TPStages.Kakariko_Graveyard",
    "Zoras River": "TPStages.Zoras_River",
    "Zoras Domain": "TPStages.Zoras_Domain",
    "Snowpeak": "TPStages.Snowpeak",
    "Lake Hylia": "TPStages.Lake_Hylia",
    "Castle Town": "TPStages.Castle_Town",
    "Sacred Grove": "TPStages.Sacred_Grove",
    "Bulblin Camp": "TPStages.Bulblin_Camp",
    "Hyrule Field": "TPStages.Hyrule_Field",
    "Outside Castle Town": "TPStages.Outside_Castle_Town",
    "Gerudo Desert": "TPStages.Gerudo_Desert",
    "Mirror Chamber": "TPStages.Mirror_Chamber",
    "Upper Zoras River": "TPStages.Upper_Zoras_River",
    "Fishing Hole": "TPStages.Fishing_Pond",
    "Hidden Village": "TPStages.Hidden_Village",
    "Hidden Skill": "TPStages.Hidden_Skill",
    "Ordon Village Interiors": "TPStages.Ordon_Village_Interiors",
    "Hyrule Castle Sewers": "TPStages.Hyrule_Castle_Sewers",
    "Faron Woods Interiors": "TPStages.Faron_Woods_Interiors",
    "Kakariko Village Interiors": "TPStages.Kakariko_Village_Interiors",
    "Death Mountain Interiors": "TPStages.Death_Mountain_Interiors",
    "Castle Town Interiors": "TPStages.Castle_Town_Interiors",
    "Fishing Pond Interiors": "TPStages.Fishing_Pond_Interiors",
    "Hidden Village Interiors": "TPStages.Hidden_Village_Interiors",
    "Castle Town Shops": "TPStages.Castle_Town_Shops",
    "Star Game": "TPStages.Star_Game",
    "Hyrule Field - Eldin Province": "TPStages.Eldin_Field",
    "Hyrule Field - Faron Province": "TPStages.Faron_Field",
    "Bulblin Camp": "TPStages.Bublin_Camp",
    "Hyrule Field - Lanayru Province": "TPStages.Lanayru_Field",
}
ADDR_TO_NODE = {
    0x804063B0: "NodeID.Ordon",
    0x804063D0: "NodeID.Sewers",
    0x804063F0: "NodeID.Faron",
    0x80406410: "NodeID.Eldin",
    0x80406430: "NodeID.Lanayru",
    0x80406470: "NodeID.Hyrule_Field",
    0x80406490: "NodeID.Sacred_Grove",
    0x804064B0: "NodeID.Snowpeak",
    0x804064D0: "NodeID.Castle_Town",
    0x804064F0: "NodeID.Gerudo_Desert",
    0x80406510: "NodeID.Fishing_Pond",
    0x804065B0: "NodeID.Forest_Temple",
    0x804065D0: "NodeID.Goron_Mines",
    0x804065F0: "NodeID.Lakebed_Temple",
    0x80406610: "NodeID.Arbiters_Grounds",
    0x80406630: "NodeID.Snowpeak_Ruins",
    0x80406650: "NodeID.Temple_of_Time",
    0x80406670: "NodeID.City_in_the_Sky",
    0x80406690: "NodeID.Palace_of_Twilight",
    0x804066B0: "NodeID.Hyrule_Castle",
    0x804066D0: "NodeID.Cave_of_Ordeals",
    0x804066F0: "NodeID.Lake_Hylia_Cave",
    0x80406710: "NodeID.Grotto",
}

location_generator = LocationGenerator()
# location_generator.generate_location_rules()
location_generator.create_location_table_file()
