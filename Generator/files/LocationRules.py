from typing import TYPE_CHECKING, Callable

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

    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_BIG_KEY_CHEST,
		lambda state: ((state.has(ItemList.ArbitersGroundsSmallKey, player, 5) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player) and can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_DEATH_SWORD_CHEST,
		lambda state: (can_defeat_DeathSword(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_Bubble(state, player) and can_defeat_Stalfos(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 5) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_DUNGEON_REWARD,
		lambda state: (can_defeat_Stallord(state, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_EAST_LOWER_TURNABLE_REDEAD_CHEST,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_EAST_TURNING_ROOM_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_EAST_UPPER_TURNABLE_CHEST,
		lambda state: ((state.has(ItemList.ArbitersGroundsSmallKey, player, 2) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_EAST_UPPER_TURNABLE_REDEAD_CHEST,
		lambda state: (has_damaging_item(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 2) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_ENTRANCE_CHEST,
		lambda state: (can_break_wooden_door(state, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_GHOUL_RAT_ROOM_CHEST,
		lambda state: (can_defeat_Bubble(state, player) and can_defeat_Stalchild(state, player) and can_defeat_RedeadKnight(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_HIDDEN_WALL_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_defeat_RedeadKnight(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_NORTH_TURNING_ROOM_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_FIRST_SMALL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player) and can_defeat_Bubble(state, player) and can_defeat_Stalfos(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 5) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_LOWER_CENTRAL_SMALL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player) and can_defeat_Bubble(state, player) and can_defeat_Stalfos(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 5) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_LOWER_NORTH_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player) and can_defeat_Bubble(state, player) and can_defeat_Stalfos(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 5) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_SECOND_SMALL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player) and can_defeat_Bubble(state, player) and can_defeat_Stalfos(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 5) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_STALFOS_ALCOVE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player) and can_defeat_Bubble(state, player) and can_defeat_Stalfos(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 5) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_STALLORD_HEART_CONTAINER,
		lambda state: (can_defeat_Stallord(state, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_TORCH_ROOM_EAST_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_TORCH_ROOM_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_TORCH_ROOM_WEST_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_WEST_CHANDELIER_CHEST,
		lambda state: ((state.has(ItemList.ArbitersGroundsSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_WEST_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_smash(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_RedeadKnight(state, player) and can_defeat_Stalchild(state, player) and can_defeat_Bubble(state, player) and can_defeat_GhoulRat(state, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_WEST_SMALL_CHEST_BEHIND_BLOCK,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_WEST_STALFOS_NORTHEAST_CHEST,
		lambda state: (can_break_wooden_door(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_RedeadKnight(state, player) and can_defeat_Stalchild(state, player) and can_defeat_Bubble(state, player) and can_defeat_GhoulRat(state, player))
	)
    set_rule_if_exists(
		CheckName.ARBITERS_GROUNDS_WEST_STALFOS_WEST_CHEST,
		lambda state: (can_break_wooden_door(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_RedeadKnight(state, player) and can_defeat_Stalchild(state, player) and can_defeat_Bubble(state, player) and can_defeat_GhoulRat(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_AERALFOS_CHEST,
		lambda state: (can_defeat_Aeralfos(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.IronBoots, player) and can_defeat_Dinalfos(state, player) and can_defeat_TileWorm(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_ARGOROK_HEART_CONTAINER,
		lambda state: (can_defeat_Argorok(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_BABA_TOWER_ALCOVE_CHEST,
		lambda state: (can_defeat_BabaSerpent(state, player) and can_defeat_BigBaba(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_BABA_TOWER_NARROW_LEDGE_CHEST,
		lambda state: (can_defeat_BabaSerpent(state, player) and can_defeat_BigBaba(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_BABA_TOWER_TOP_SMALL_CHEST,
		lambda state: (can_defeat_BabaSerpent(state, player) and can_defeat_BigBaba(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_BIG_KEY_CHEST,
		lambda state: (can_defeat_Dinalfos(state, player) and can_defeat_Walltula(state, player) and can_defeat_Kargarok(state, player) and state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_CENTRAL_OUTSIDE_LEDGE_CHEST,
		lambda state: (can_defeat_Dinalfos(state, player) and can_defeat_Walltula(state, player) and can_defeat_Kargarok(state, player) and state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_CENTRAL_OUTSIDE_POE_ISLAND_CHEST,
		lambda state: (can_defeat_Dinalfos(state, player) and can_defeat_Walltula(state, player) and can_defeat_Kargarok(state, player) and state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_CHEST_BEHIND_NORTH_FAN,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_CHEST_BELOW_BIG_KEY_CHEST,
		lambda state: (can_defeat_Helmasaur(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_DUNGEON_REWARD,
		lambda state: (can_defeat_Argorok(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_EAST_FIRST_WING_CHEST_AFTER_FANS,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_EAST_TILE_WORM_SMALL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_EAST_WING_AFTER_DINALFOS_ALCOVE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_TileWorm(state, player) and can_defeat_Dinalfos(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_EAST_WING_AFTER_DINALFOS_LEDGE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_TileWorm(state, player) and can_defeat_Dinalfos(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_EAST_WING_LOWER_LEVEL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_Dinalfos(state, player) and can_defeat_TileWorm(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_GARDEN_ISLAND_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_POE_ABOVE_CENTRAL_FAN,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_defeat_Walltula(state, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_UNDERWATER_EAST_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_UNDERWATER_WEST_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_WEST_GARDEN_CORNER_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LEDGE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LONE_ISLAND_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LOWER_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_WEST_WING_BABA_BALCONY_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_WEST_WING_FIRST_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_WEST_WING_NARROW_LEDGE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.CITY_IN_THE_SKY_WEST_WING_TILE_WORM_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_BIG_BABA_KEY,
		lambda state: (can_defeat_BigBaba(state, player) and can_defeat_Walltula(state, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_BIG_KEY_CHEST,
		lambda state: (state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_CENTRAL_CHEST_BEHIND_STAIRS,
		lambda state: (state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_CENTRAL_CHEST_HANGING_FROM_WEB,
		lambda state: (can_cut_hanging_web(state, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_CENTRAL_NORTH_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_DIABABA_HEART_CONTAINER,
		lambda state: (can_defeat_Diababa(state, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_DUNGEON_REWARD,
		lambda state: (can_defeat_Diababa(state, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_EAST_TILE_WORM_CHEST,
		lambda state: (can_defeat_TileWorm(state, player) and can_defeat_Skulltula(state, player) and can_defeat_Walltula(state, player) and state.has(ItemList.GaleBoomerang, player) and (state.has(ItemList.ForestTempleSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_EAST_WATER_CAVE_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_ENTRANCE_VINES_CHEST,
		lambda state: (can_defeat_Walltula(state, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_GALE_BOOMERANG,
		lambda state: (can_defeat_Ook(state, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_NORTH_DEKU_LIKE_CHEST,
		lambda state: (state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_SECOND_MONKEY_UNDER_BRIDGE_CHEST,
		lambda state: (state.has(ItemList.ForestTempleSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_TOTEM_POLE_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_WEST_DEKU_LIKE_CHEST,
		lambda state: (can_defeat_Walltula(state, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_WEST_TILE_WORM_CHEST_BEHIND_STAIRS,
		lambda state: (state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_WEST_TILE_WORM_ROOM_VINES_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FOREST_TEMPLE_WINDLESS_BRIDGE_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_AFTER_CRYSTAL_SWITCH_ROOM_MAGNET_WALL_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_BEAMOS_ROOM_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player) and can_defeat_Dangoro(state, player) and state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_CHEST_BEFORE_DANGORO,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_CRYSTAL_SWITCH_ROOM_SMALL_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_CRYSTAL_SWITCH_ROOM_UNDERWATER_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_DANGORO_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player) and can_defeat_Dangoro(state, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_DUNGEON_REWARD,
		lambda state: (can_defeat_Fyrus(state, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_ENTRANCE_CHEST,
		lambda state: (can_press_mines_switch(state, player) and can_break_wooden_door(state, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_FYRUS_HEART_CONTAINER,
		lambda state: (can_defeat_Fyrus(state, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_GOR_AMATO_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_GOR_AMATO_KEY_SHARD,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_GOR_AMATO_SMALL_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_GOR_EBIZO_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_GOR_EBIZO_KEY_SHARD,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_GOR_LIGGS_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player) and can_defeat_Dangoro(state, player) and state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_GOR_LIGGS_KEY_SHARD,
		lambda state: (state.has(ItemList.IronBoots, player) and can_defeat_Dangoro(state, player) and state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_MAGNET_MAZE_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_MAIN_MAGNET_ROOM_BOTTOM_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_MAIN_MAGNET_ROOM_TOP_CHEST,
		lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1) and state.has(ItemList.IronBoots, player) and can_defeat_Dangoro(state, player) and (state.has(ItemList.GoronMinesSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_OUTSIDE_BEAMOS_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_OUTSIDE_CLAWSHOT_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and (state.has(ItemList.ProgressiveHerosBow, player, 1) or state.has(ItemList.Slingshot, player)))
	)
    set_rule_if_exists(
		CheckName.GORON_MINES_OUTSIDE_UNDERWATER_CHEST,
		lambda state: ((has_sword(state, player) or can_use_water_bombs(state, player)) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_BIG_KEY_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_EAST_WING_BALCONY_CHEST,
		lambda state: (state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_EAST_WING_BOOMERANG_PUZZLE_CHEST,
		lambda state: (state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_BACK_LEFT_CHEST,
		lambda state: (can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_FRONT_LEFT_CHEST,
		lambda state: (can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_RIGHT_CHEST,
		lambda state: (can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_GRAVEYARD_OWL_STATUE_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player) and state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_KING_BULBLIN_KEY,
		lambda state: (can_defeat_KingBulblinCastle(state, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_LANTERN_STAIRCASE_CHEST,
		lambda state: (can_defeat_Darknut(state, player) and state.has(ItemList.GaleBoomerang, player) and can_defeat_Bokoblin(state, player) and can_defeat_Lizalfos(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_MAIN_HALL_NORTHEAST_CHEST,
		lambda state: (can_defeat_Bokoblin(state, player) and can_defeat_Lizalfos(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_MAIN_HALL_NORTHWEST_CHEST,
		lambda state: (can_knock_down_hc_painting(state, player) and can_defeat_Lizalfos(state, player) and can_defeat_Darknut(state, player) and state.has(ItemList.GaleBoomerang, player) and state.has(ItemList.Lantern, player) and state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_MAIN_HALL_SOUTHWEST_CHEST,
		lambda state: (can_knock_down_hc_painting(state, player) and can_defeat_Lizalfos(state, player) and can_defeat_Darknut(state, player) and state.has(ItemList.GaleBoomerang, player) and state.has(ItemList.Lantern, player) and state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_SOUTHEAST_BALCONY_TOWER_CHEST,
		lambda state: (can_defeat_Aeralfos(state, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_EIGHTH_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIFTH_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIFTH_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIRST_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIRST_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_FOURTH_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_FOURTH_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_SECOND_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_SECOND_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_SEVENTH_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_SIXTH_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_THIRD_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_TREASURE_ROOM_THIRD_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_WEST_COURTYARD_CENTRAL_SMALL_CHEST,
		lambda state: (can_defeat_Bokoblin(state, player))
	)
    set_rule_if_exists(
		CheckName.HYRULE_CASTLE_WEST_COURTYARD_NORTH_SMALL_CHEST,
		lambda state: (can_defeat_Bokoblin(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_ALCOVE_CHEST,
		lambda state: (((state._tp_small_key_settings(player) == SmallKeySettings.option_vanilla) and can_defeat_DekuToad(state, player) and state.has(ItemList.LakebedTempleSmallKey, player, 2) and state.has(ItemList.ZoraArmor, player) and state.has(ItemList.IronBoots, player) and can_use_water_bombs(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1)) or ((state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and (can_launch_bombs(state, player) or (state.has(ItemList.ProgressiveClawshot, player, 1) and can_smash(state, player)))))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_UNDERWATER_LEFT_CHEST,
		lambda state: (state.has(ItemList.ZoraArmor, player) and state.has(ItemList.IronBoots, player) and (state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and (can_launch_bombs(state, player) or (state.has(ItemList.ProgressiveClawshot, player, 1) and can_smash(state, player))))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_UNDERWATER_RIGHT_CHEST,
		lambda state: (state.has(ItemList.ZoraArmor, player) and state.has(ItemList.IronBoots, player) and (state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and (can_launch_bombs(state, player) or (state.has(ItemList.ProgressiveClawshot, player, 1) and can_smash(state, player))))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_BIG_KEY_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and can_use_water_bombs(state, player) and state.has(ItemList.ZoraArmor, player) and can_launch_bombs(state, player) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_SPIRE_CHEST,
		lambda state: ((state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.IronBoots, player) and can_launch_bombs(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_CHANDELIER_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_DEKU_TOAD_CHEST,
		lambda state: (can_defeat_DekuToad(state, player) and (state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.ZoraArmor, player) and state.has(ItemList.IronBoots, player) and can_use_water_bombs(state, player) and (can_launch_bombs(state, player) or (state.has(ItemList.ProgressiveClawshot, player, 1) and can_smash(state, player))))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_DUNGEON_REWARD,
		lambda state: (can_defeat_Morpheel(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_EAST_LOWER_WATERWHEEL_BRIDGE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and (state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_launch_bombs(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_EAST_LOWER_WATERWHEEL_STALACTITE_CHEST,
		lambda state: (can_launch_bombs(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_EAST_SECOND_FLOOR_SOUTHEAST_CHEST,
		lambda state: (can_launch_bombs(state, player) or (state.has(ItemList.ProgressiveClawshot, player, 1) and can_smash(state, player)))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_EAST_SECOND_FLOOR_SOUTHWEST_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_EAST_WATER_SUPPLY_CLAWSHOT_CHEST,
		lambda state: ((state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_smash(state, player) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_EAST_WATER_SUPPLY_SMALL_CHEST,
		lambda state: ((state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and (state.has(ItemList.ProgressiveClawshot, player, 1) or can_launch_bombs(state, player)) and can_smash(state, player) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_LOBBY_LEFT_CHEST,
		lambda state: (state.has(ItemList.ZoraArmor, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_LOBBY_REAR_CHEST,
		lambda state: (state.has(ItemList.ZoraArmor, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_MORPHEEL_HEART_CONTAINER,
		lambda state: (can_defeat_Morpheel(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_STALACTITE_ROOM_CHEST,
		lambda state: (can_launch_bombs(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_UNDERWATER_MAZE_SMALL_CHEST,
		lambda state: (state.has(ItemList.ZoraArmor, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_launch_bombs(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_WEST_LOWER_SMALL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_CENTRAL_SMALL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_NORTHEAST_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and can_launch_bombs(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_SOUTHEAST_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and can_launch_bombs(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_SOUTHWEST_UNDERWATER_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.IronBoots, player) and can_launch_bombs(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_WEST_WATER_SUPPLY_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and can_launch_bombs(state, player) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.LAKEBED_TEMPLE_WEST_WATER_SUPPLY_SMALL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and can_launch_bombs(state, player) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_BIG_KEY_CHEST,
		lambda state: (state.has(ItemList.ProgressiveMasterSword, player, 4) and state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_ZantHead(state, player))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM_CHEST,
		lambda state: (can_defeat_ZantHead(state, player) and state.has(ItemList.ProgressiveMasterSword, player, 4))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_CENTRAL_OUTDOOR_CHEST,
		lambda state: (can_defeat_ZantHead(state, player))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_CENTRAL_TOWER_CHEST,
		lambda state: (can_defeat_ZantHead(state, player) and state.has(ItemList.ProgressiveMasterSword, player, 4) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_COLLECT_BOTH_SOLS,
		lambda state: (can_defeat_PhantomZant(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_ZantHead(state, player) and (state.has(ItemList.PalaceOfTwilightSmallKey, player, 7) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_ShadowBeast(state, player))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_EAST_ALCOVE,
		lambda state: (state.has(ItemList.ProgressiveMasterSword, player, 4) or (can_defeat_PhantomZant(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_ZantHead(state, player) and (state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_ShadowBeast(state, player)))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_NORTH_SMALL_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_WEST_ALCOVE,
		lambda state: (state.has(ItemList.ProgressiveMasterSword, player, 4) or (can_defeat_PhantomZant(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_ZantHead(state, player) and (state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_ShadowBeast(state, player)))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_ZANT_HEAD_CHEST,
		lambda state: (can_defeat_ZantHead(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_NORTHEAST_CHEST,
		lambda state: (can_defeat_ZantHead(state, player) and can_defeat_ShadowBeast(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and (((state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or ((state._tp_small_key_settings(player) == SmallKeySettings.option_vanilla) and state.has(ItemList.PalaceOfTwilightSmallKey, player, 3))) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_NORTHWEST_CHEST,
		lambda state: (can_defeat_ZantHead(state, player) and can_defeat_ShadowBeast(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and (((state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or ((state._tp_small_key_settings(player) == SmallKeySettings.option_vanilla) and state.has(ItemList.PalaceOfTwilightSmallKey, player, 3))) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_SOUTHEAST_CHEST,
		lambda state: (can_defeat_ZantHead(state, player) and can_defeat_ShadowBeast(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and (((state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or ((state._tp_small_key_settings(player) == SmallKeySettings.option_vanilla) and state.has(ItemList.PalaceOfTwilightSmallKey, player, 3))) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_SOUTHWEST_CHEST,
		lambda state: (can_defeat_ZantHead(state, player) and can_defeat_ShadowBeast(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and (((state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or ((state._tp_small_key_settings(player) == SmallKeySettings.option_vanilla) and state.has(ItemList.PalaceOfTwilightSmallKey, player, 3))) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_WEST_WING_CHEST_BEHIND_WALL_OF_DARKNESS,
		lambda state: (state.has(ItemList.ProgressiveMasterSword, player, 4) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_WEST_WING_FIRST_ROOM_CENTRAL_CHEST,
		lambda state: (can_defeat_ZantHead(state, player))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_CENTRAL_CHEST,
		lambda state: ((((state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or ((state._tp_small_key_settings(player) == SmallKeySettings.option_vanilla) and state.has(ItemList.PalaceOfTwilightSmallKey, player, 3))) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))) and can_defeat_ZantHead(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_LOWER_SOUTH_CHEST,
		lambda state: ((((state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or ((state._tp_small_key_settings(player) == SmallKeySettings.option_vanilla) and state.has(ItemList.PalaceOfTwilightSmallKey, player, 3))) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))) and can_defeat_ZantHead(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_SOUTHEAST_CHEST,
		lambda state: ((((state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or ((state._tp_small_key_settings(player) == SmallKeySettings.option_vanilla) and state.has(ItemList.PalaceOfTwilightSmallKey, player, 3))) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))) and can_defeat_ZantHead(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.PALACE_OF_TWILIGHT_ZANT_HEART_CONTAINER,
		lambda state: (can_defeat_Zant(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_BALL_AND_CHAIN,
		lambda state: (can_defeat_Darkhammer(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_BLIZZETA_HEART_CONTAINER,
		lambda state: (can_defeat_Blizzeta(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_BROKEN_FLOOR_CHEST,
		lambda state: (state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_CHAPEL_CHEST,
		lambda state: (can_defeat_Chilfos(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_CHEST_AFTER_DARKHAMMER,
		lambda state: (can_defeat_Darkhammer(state, player) and state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_COURTYARD_CENTRAL_CHEST,
		lambda state: (state.has(ItemList.BallAndChain, player) or (has_bombs(state, player) and ((state.has(ItemList.SnowpeakRuinsSmallKey, player, 2) or state.has(ItemList.OrdonGoatCheese, player)) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_DUNGEON_REWARD,
		lambda state: (can_defeat_Blizzeta(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_EAST_COURTYARD_BURIED_CHEST,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_EAST_COURTYARD_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_ICE_ROOM_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_LOBBY_ARMOR_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_LOBBY_CHANDELIER_CHEST,
		lambda state: (((state.has(ItemList.SnowpeakRuinsSmallKey, player, 3) and state.has(ItemList.OrdonGoatCheese, player)) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_LOBBY_EAST_ARMOR_CHEST,
		lambda state: (state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_LOBBY_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_LOBBY_WEST_ARMOR_CHEST,
		lambda state: (state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_MANSION_MAP,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_NORTHEAST_CHANDELIER_CHEST,
		lambda state: (can_defeat_Chilfos(state, player) and state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_ORDON_PUMPKIN_CHEST,
		lambda state: (can_defeat_Chilfos(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_WEST_CANNON_ROOM_CENTRAL_CHEST,
		lambda state: (state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_WEST_CANNON_ROOM_CORNER_CHEST,
		lambda state: (can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_WEST_COURTYARD_BURIED_CHEST,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_CENTRAL_CHEST,
		lambda state: (can_defeat_IceKeese(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_CHANDELIER_CHEST,
		lambda state: ((state.has(ItemList.OrdonGoatCheese, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_NORTHWEST_CHEST,
		lambda state: (can_defeat_IceKeese(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_ARMOGOHMA_HEART_CONTAINER,
		lambda state: (can_defeat_Armogohma(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_EAST_CHEST,
		lambda state: (can_defeat_Armos(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_NORTH_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_STATUE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 1))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_BIG_KEY_CHEST,
		lambda state: (can_defeat_Helmasaur(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_CHEST_BEFORE_DARKNUT,
		lambda state: (can_defeat_Armos(state, player) and can_defeat_BabyGohma(state, player) and can_defeat_YoungGohma(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_DARKNUT_CHEST,
		lambda state: (can_defeat_Darknut(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_DUNGEON_REWARD,
		lambda state: (can_defeat_Armogohma(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_ARMOS_CHEST,
		lambda state: (can_defeat_Armos(state, player) and has_ranged_item(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_GOHMA_GATE_CHEST,
		lambda state: (can_defeat_YoungGohma(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_WINDOW_CHEST,
		lambda state: (has_ranged_item(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM_UPPER_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_GILLOUTINE_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_LOBBY_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_MOVING_WALL_BEAMOS_ROOM_CHEST,
		lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_MOVING_WALL_DINALFOS_ROOM_CHEST,
		lambda state: (can_defeat_Dinalfos(state, player) and state.has(ItemList.ProgressiveDominionRod, player, 1) and state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_POE_ABOVE_SCALES,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_POE_BEHIND_GATE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveDominionRod, player, 1))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_SCALES_GOHMA_CHEST,
		lambda state: (can_defeat_YoungGohma(state, player) and can_defeat_BabyGohma(state, player))
	)
    set_rule_if_exists(
		CheckName.TEMPLE_OF_TIME_SCALES_UPPER_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player))
	)
    set_rule_if_exists(
		CheckName.BARNES_BOMB_BAG,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.BRIDGE_OF_ELDIN_FEMALE_PHASMID,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.BRIDGE_OF_ELDIN_MALE_PHASMID,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.BRIDGE_OF_ELDIN_OWL_STATUE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.BRIDGE_OF_ELDIN_OWL_STATUE_SKY_CHARACTER,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.CATS_HIDE_AND_SEEK_MINIGAME,
		lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1) and state.can_reach_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player) and state.has(ItemList.IliasCharm, player) and state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.DEATH_MOUNTAIN_ALCOVE_CHEST,
		lambda state: ((can_complete_goron_mines(state, player) and (not state._tp_barren_dungeons(player))) or (state.has(ItemList.ProgressiveClawshot, player, 1) and (state.has(ItemList.IronBoots, player) or state.has(ItemList.ShadowCrystal, player))))
	)
    set_rule_if_exists(
		CheckName.DEATH_MOUNTAIN_TRAIL_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_complete_goron_mines(state, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_BOMB_ROCK_CHEST,
		lambda state: (can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_BOMSKIT_GROTTO_LANTERN_CHEST,
		lambda state: (can_defeat_Bomskit(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_BOMSKIT_GROTTO_LEFT_CHEST,
		lambda state: (can_defeat_Bomskit(state, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_FEMALE_GRASSHOPPER,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_MALE_GRASSHOPPER,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_STALFOS_GROTTO_LEFT_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_STALFOS_GROTTO_RIGHT_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_STALFOS_GROTTO_STALFOS_CHEST,
		lambda state: (can_defeat_Stalfos(state, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ELDIN_LANTERN_CAVE_FIRST_CHEST,
		lambda state: (can_burn_webs(state, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_LANTERN_CAVE_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_LANTERN_CAVE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_burn_webs(state, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_LANTERN_CAVE_SECOND_CHEST,
		lambda state: (can_burn_webs(state, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_SPRING_UNDERWATER_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_STOCKCAVE_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.ELDIN_STOCKCAVE_LOWEST_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ELDIN_STOCKCAVE_UPPER_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.GIFT_FROM_RALIS,
		lambda state: (state.has(ItemList.AsheisSketch, player) and (state.has(ItemList.GateKeys, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)))
	)
    set_rule_if_exists(
		CheckName.GORON_SPRINGWATER_RUSH,
		lambda state: (can_smash(state, player) or (((state._tp_lanayru_twilight_cleared(player)) or state.has(ItemList.ShadowCrystal, player)) and (state.has(ItemList.GateKeys, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))))
	)
    set_rule_if_exists(
		CheckName.HIDDEN_VILLAGE_POE,
		lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1) and state.can_reach_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player) and state.has(ItemList.IliasCharm, player) and state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.ILIA_CHARM,
		lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.ILIA_MEMORY_REWARD,
		lambda state: (state.has(ItemList.IliasCharm, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GORGE_DOUBLE_CLAWSHOT_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GORGE_FEMALE_PILL_BUG,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GORGE_MALE_PILL_BUG,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GORGE_OWL_STATUE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GORGE_OWL_STATUE_SKY_CHARACTER,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GORGE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_complete_MDH(state, player) and can_complete_all_twilight(state, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GORGE_SPIRE_HEART_PIECE,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GRAVEYARD_GOLDEN_WOLF,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.can_reach_region(RoomName.SNOWPEAK_CLIMB_UPPER, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GRAVEYARD_GRAVE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_change_time(state, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GRAVEYARD_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GRAVEYARD_MALE_ANT,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_GRAVEYARD_OPEN_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_change_time(state, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_INN_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_VILLAGE_BOMB_ROCK_SPIRE_HEART_PIECE,
		lambda state: (has_bombs(state, player) and state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_VILLAGE_BOMB_SHOP_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_change_time(state, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_VILLAGE_FEMALE_ANT,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_VILLAGE_MALO_MART_HAWKEYE,
		lambda state: (can_complete_goron_mines(state, player) and state.can_reach_region(RoomName.KAKARIKO_TOP_OF_WATCHTOWER, player) and state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_VILLAGE_MALO_MART_HYLIAN_SHIELD,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_VILLAGE_MALO_MART_RED_POTION,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_VILLAGE_MALO_MART_WOODEN_SHIELD,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_VILLAGE_WATCHTOWER_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_change_time(state, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_WATCHTOWER_ALCOVE_CHEST,
		lambda state: (can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.KAKARIKO_WATCHTOWER_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.RENADOS_LETTER,
		lambda state: (can_complete_temple_of_time(state, player))
	)
    set_rule_if_exists(
		CheckName.RUTELAS_BLESSING,
		lambda state: (state.has(ItemList.GateKeys, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))
	)
    set_rule_if_exists(
		CheckName.SKYBOOK_FROM_IMPAZ,
		lambda state: (state.can_reach_region(RoomName.HIDDEN_VILLAGE, player) and state.has(ItemList.ProgressiveHerosBow, player, 1) and state.has(ItemList.ProgressiveDominionRod, player, 1))
	)
    set_rule_if_exists(
		CheckName.TALO_SHARPSHOOTING,
		lambda state: (can_complete_goron_mines(state, player) and state.has(ItemList.ProgressiveHerosBow, player, 1) and can_change_time(state, player))
	)
    set_rule_if_exists(
		CheckName.CORO_BOTTLE,
		lambda state: (can_complete_prologue(state, player))
	)
    set_rule_if_exists(
		CheckName.FARON_FIELD_BRIDGE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.FARON_FIELD_CORNER_GROTTO_LEFT_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FARON_FIELD_CORNER_GROTTO_REAR_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FARON_FIELD_CORNER_GROTTO_RIGHT_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FARON_FIELD_FEMALE_BEETLE,
		lambda state: (state.has(ItemList.GaleBoomerang, player) or state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.FARON_FIELD_MALE_BEETLE,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FARON_FIELD_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_complete_MDH(state, player) and can_complete_all_twilight(state, player))
	)
    set_rule_if_exists(
		CheckName.FARON_FIELD_TREE_HEART_PIECE,
		lambda state: (state.has(ItemList.GaleBoomerang, player) or state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.FARON_MIST_CAVE_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.FARON_MIST_CAVE_OPEN_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FARON_MIST_NORTH_CHEST,
		lambda state: (state.has(ItemList.Lantern, player) and can_complete_prologue(state, player))
	)
    set_rule_if_exists(
		CheckName.FARON_MIST_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_complete_prologue(state, player))
	)
    set_rule_if_exists(
		CheckName.FARON_MIST_SOUTH_CHEST,
		lambda state: (state.has(ItemList.Lantern, player) and can_complete_prologue(state, player))
	)
    set_rule_if_exists(
		CheckName.FARON_MIST_STUMP_CHEST,
		lambda state: (state.has(ItemList.Lantern, player) and can_complete_prologue(state, player))
	)
    set_rule_if_exists(
		CheckName.FARON_WOODS_GOLDEN_WOLF,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FARON_WOODS_OWL_STATUE_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FARON_WOODS_OWL_STATUE_SKY_CHARACTER,
		lambda state: (can_clear_forest(state, player) and state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.LOST_WOODS_BOULDER_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and (can_defeat_SkullKid(state, player) or (state._tp_tot_entrance(player) == TotEntrance.option_open) or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)) and can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.LOST_WOODS_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LOST_WOODS_WATERFALL_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.NORTH_FARON_WOODS_DEKU_BABA_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_BABA_SERPENT_GROTTO_CHEST,
		lambda state: (can_defeat_BabaSerpent(state, player) and can_knock_down_HangingBaba(state, player))
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_FEMALE_SNAIL,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_MALE_SNAIL,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_MASTER_SWORD_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_PAST_OWL_STATUE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 1))
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_PEDESTAL_MASTER_SWORD,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_PEDESTAL_SHADOW_CRYSTAL,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_SPINNER_CHEST,
		lambda state: (state.has(ItemList.Spinner, player))
	)
    set_rule_if_exists(
		CheckName.SACRED_GROVE_TEMPLE_OF_TIME_OWL_STATUE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveDominionRod, player, 1))
	)
    set_rule_if_exists(
		CheckName.SOUTH_FARON_CAVE_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.BULBLIN_CAMP_FIRST_CHEST_UNDER_TOWER_AT_ENTRANCE,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.BULBLIN_CAMP_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and (state.has(ItemList.GerudoDesertBulblinCampKey, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy) or (state._tp_skip_arbiters_entrance(player))))
	)
    set_rule_if_exists(
		CheckName.BULBLIN_CAMP_ROASTED_BOAR,
		lambda state: (has_damaging_item(state, player))
	)
    set_rule_if_exists(
		CheckName.BULBLIN_CAMP_SMALL_CHEST_IN_BACK_OF_CAMP,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.BULBLIN_GUARD_KEY,
		lambda state: (can_defeat_Bulblin(state, player))
	)
    set_rule_if_exists(
		CheckName.CAVE_OF_ORDEALS_FLOOR_17_POE,
		lambda state: (state.has(ItemList.Spinner, player) and state.has(ItemList.ShadowCrystal, player) and can_defeat_Helmasaur(state, player) and can_defeat_Rat(state, player) and can_defeat_Chu(state, player) and can_defeat_ChuWorm(state, player) and can_defeat_Bubble(state, player) and can_defeat_Keese(state, player) and can_defeat_Stalhound(state, player))
	)
    set_rule_if_exists(
		CheckName.CAVE_OF_ORDEALS_FLOOR_33_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveDominionRod, player, 2) and can_defeat_Beamos(state, player) and can_defeat_Keese(state, player) and can_defeat_Dodongo(state, player) and can_defeat_Bubble(state, player) and can_defeat_RedeadKnight(state, player))
	)
    set_rule_if_exists(
		CheckName.CAVE_OF_ORDEALS_FLOOR_44_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_Armos(state, player) and can_defeat_BabaSerpent(state, player) and can_defeat_Lizalfos(state, player) and can_defeat_Dinalfos(state, player) and (state.has(ItemList.ProgressiveHerosBow, player, 1) or state.has(ItemList.BallAndChain, player)))
	)
    set_rule_if_exists(
		CheckName.CAVE_OF_ORDEALS_GREAT_FAIRY_REWARD,
		lambda state: (can_defeat_Armos(state, player) and can_defeat_Bokoblin(state, player) and can_defeat_BabaSerpent(state, player) and can_defeat_Lizalfos(state, player) and can_defeat_Bulblin(state, player) and can_defeat_Dinalfos(state, player) and can_defeat_Poe(state, player) and can_defeat_RedeadKnight(state, player) and can_defeat_Chu(state, player) and can_defeat_Freezard(state, player) and can_defeat_Chilfos(state, player) and can_defeat_GhoulRat(state, player) and can_defeat_Rat(state, player) and can_defeat_Stalchild(state, player) and can_defeat_Aeralfos(state, player) and can_defeat_Darknut(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_CAMPFIRE_EAST_CHEST,
		lambda state: (can_defeat_Bulblin(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_CAMPFIRE_NORTH_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_CAMPFIRE_WEST_CHEST,
		lambda state: (can_defeat_Bulblin(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_EAST_CANYON_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_EAST_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_FEMALE_DAYFLY,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_GOLDEN_WOLF,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.can_reach_region(RoomName.LAKE_HYLIA, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_LONE_SMALL_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_MALE_DAYFLY,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_NORTH_PEAHAT_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_NORTH_SMALL_CHEST_BEFORE_BULBLIN_CAMP,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_NORTHEAST_CHEST_BEHIND_GATES,
		lambda state: (can_defeat_Bulblin(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_NORTHWEST_CHEST_BEHIND_GATES,
		lambda state: (can_defeat_Bulblin(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_OWL_STATUE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_OWL_STATUE_SKY_CHARACTER,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_PEAHAT_LEDGE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_POE_ABOVE_CAVE_OF_ORDEALS,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_ROCK_GROTTO_FIRST_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_ROCK_GROTTO_LANTERN_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_ROCK_GROTTO_SECOND_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_smash(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_SKULLTULA_GROTTO_CHEST,
		lambda state: (can_defeat_Skulltula(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_SOUTH_CHEST_BEHIND_WOODEN_GATES,
		lambda state: (can_defeat_Bulblin(state, player))
	)
    set_rule_if_exists(
		CheckName.GERUDO_DESERT_WEST_CANYON_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_ARBITERS_GROUNDS_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_ARBITERS_GROUNDS_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_BULBLIN_CAMP_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_ANT_REWARD,
		lambda state: (state.has(ItemList.FemaleAnt, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_BEETLE_REWARD,
		lambda state: (state.has(ItemList.FemaleBeetle, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_BUTTERFLY_REWARD,
		lambda state: (state.has(ItemList.FemaleButterfly, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_DAYFLY_REWARD,
		lambda state: (state.has(ItemList.FemaleDayfly, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_DRAGONFLY_REWARD,
		lambda state: (state.has(ItemList.FemaleDragonfly, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_GRASSHOPPER_REWARD,
		lambda state: (state.has(ItemList.FemaleGrasshopper, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_LADYBUG_REWARD,
		lambda state: (state.has(ItemList.FemaleLadybug, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_MANTIS_REWARD,
		lambda state: (state.has(ItemList.FemaleMantis, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_PHASMID_REWARD,
		lambda state: (state.has(ItemList.FemalePhasmid, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_PILL_BUG_REWARD,
		lambda state: (state.has(ItemList.FemalePillBug, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_SNAIL_REWARD,
		lambda state: (state.has(ItemList.FemaleSnail, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_FEMALE_STAG_BEETLE_REWARD,
		lambda state: (state.has(ItemList.FemaleStagBeetle, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_ANT_REWARD,
		lambda state: (state.has(ItemList.MaleAnt, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_BEETLE_REWARD,
		lambda state: (state.has(ItemList.MaleBeetle, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_BUTTERFLY_REWARD,
		lambda state: (state.has(ItemList.MaleButterfly, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_DAYFLY_REWARD,
		lambda state: (state.has(ItemList.MaleDayfly, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_DRAGONFLY_REWARD,
		lambda state: (state.has(ItemList.MaleDragonfly, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_GRASSHOPPER_REWARD,
		lambda state: (state.has(ItemList.MaleGrasshopper, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_LADYBUG_REWARD,
		lambda state: (state.has(ItemList.MaleLadybug, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_MANTIS_REWARD,
		lambda state: (state.has(ItemList.MaleMantis, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_PHASMID_REWARD,
		lambda state: (state.has(ItemList.MalePhasmid, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_PILL_BUG_REWARD,
		lambda state: (state.has(ItemList.MalePillBug, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_SNAIL_REWARD,
		lambda state: (state.has(ItemList.MaleSnail, player))
	)
    set_rule_if_exists(
		CheckName.AGITHA_MALE_STAG_BEETLE_REWARD,
		lambda state: (state.has(ItemList.MaleStagBeetle, player))
	)
    set_rule_if_exists(
		CheckName.AURU_GIFT_TO_FYER,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.CASTLE_TOWN_MALO_MART_MAGIC_ARMOR,
		lambda state: (state.can_reach_region(RoomName.KAKARIKO_MALO_MART, player) and state.can_reach_region(RoomName.LOWER_KAKARIKO_VILLAGE, player) and ((state._tp_increase_wallet(player)) or state.has(ItemList.ProgressiveWallet, player, 1)))
	)
    set_rule_if_exists(
		CheckName.CHARLO_DONATION_BLESSING,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.DOCTORS_OFFICE_BALCONY_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.EAST_CASTLE_TOWN_BRIDGE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.FISHING_HOLE_BOTTLE,
		lambda state: (state.has(ItemList.ProgressiveFishingRod, player, 1))
	)
    set_rule_if_exists(
		CheckName.FISHING_HOLE_HEART_PIECE,
		lambda state: (state.can_reach_region(RoomName.FISHING_HOLE_HOUSE, player) or state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.FLIGHT_BY_FOWL_FIFTH_PLATFORM_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FLIGHT_BY_FOWL_FOURTH_PLATFORM_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FLIGHT_BY_FOWL_LEDGE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.FLIGHT_BY_FOWL_SECOND_PLATFORM_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FLIGHT_BY_FOWL_THIRD_PLATFORM_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.FLIGHT_BY_FOWL_TOP_PLATFORM_REWARD,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.HYRULE_FIELD_AMPHITHEATER_OWL_STATUE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.HYRULE_FIELD_AMPHITHEATER_OWL_STATUE_SKY_CHARACTER,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2))
	)
    set_rule_if_exists(
		CheckName.HYRULE_FIELD_AMPHITHEATER_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.ISLE_OF_RICHES_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.IZA_HELPING_HAND,
		lambda state: (state.can_reach_region(RoomName.UPPER_ZORAS_RIVER, player) and (has_sword(state, player) or (can_defeat_ShadowBeast(state, player) and (state._tp_transform_anywhere(player)))) and state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.IZA_RAGING_RAPIDS_MINIGAME,
		lambda state: (state.can_reach_region(RoomName.UPPER_ZORAS_RIVER, player) and (has_sword(state, player) or (can_defeat_ShadowBeast(state, player) and (state._tp_transform_anywhere(player)))) and state.has(ItemList.ProgressiveHerosBow, player, 1))
	)
    set_rule_if_exists(
		CheckName.JOVANI_20_POE_SOUL_REWARD,
		lambda state: (state.has(ItemList.PoeSoul, player, 20))
	)
    set_rule_if_exists(
		CheckName.JOVANI_60_POE_SOUL_REWARD,
		lambda state: (state.has(ItemList.PoeSoul, player, 60))
	)
    set_rule_if_exists(
		CheckName.JOVANI_HOUSE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_ALCOVE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO_CHEST,
		lambda state: (can_defeat_Bubble(state, player) and can_defeat_FireBubble(state, player) and can_defeat_IceBubble(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_BRIDGE_CLIFF_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_BRIDGE_CLIFF_POE,
		lambda state: (can_complete_MDH(state, player) and state.has(ItemList.ShadowCrystal, player) and can_complete_all_twilight(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_BRIDGE_FEMALE_MANTIS,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_BRIDGE_MALE_MANTIS,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_BRIDGE_OWL_STATUE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_BRIDGE_OWL_STATUE_SKY_CHARACTER,
		lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 2) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_BRIDGE_VINES_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_DOCK_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_SHELL_BLADE_GROTTO_CHEST,
		lambda state: (can_defeat_ShellBlade(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_TOWER_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_UNDERWATER_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO_CHEST,
		lambda state: (can_defeat_WaterToadpoli(state, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_EIGHTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_ELEVENTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_END_LANTERN_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_FIFTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_FINAL_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_FIRST_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_FIRST_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_FOURTEENTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_FOURTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_NINTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_SECOND_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_SECOND_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_SEVENTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_SIXTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_TENTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_THIRD_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_THIRTEENTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LAKE_LANTERN_CAVE_TWELFTH_CHEST,
		lambda state: (can_smash(state, player) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_FIELD_BEHIND_GATE_UNDERWATER_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_FIELD_BRIDGE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_complete_MDH(state, player) and can_complete_all_twilight(state, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_FIELD_FEMALE_STAG_BEETLE,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_FIELD_MALE_STAG_BEETLE,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_FIELD_POE_GROTTO_LEFT_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_FIELD_POE_GROTTO_RIGHT_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_FIELD_SKULLTULA_GROTTO_CHEST,
		lambda state: (can_defeat_Skulltula(state, player) and state.has(ItemList.Lantern, player) and can_break_wooden_door(state, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_FIELD_SPINNER_TRACK_CHEST,
		lambda state: (state.has(ItemList.Spinner, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_ICE_BLOCK_PUZZLE_CAVE_CHEST,
		lambda state: (state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_SPRING_BACK_ROOM_LANTERN_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_SPRING_BACK_ROOM_LEFT_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_SPRING_BACK_ROOM_RIGHT_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_SPRING_EAST_DOUBLE_CLAWSHOT_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_SPRING_UNDERWATER_LEFT_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_SPRING_UNDERWATER_RIGHT_CHEST,
		lambda state: (state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.LANAYRU_SPRING_WEST_DOUBLE_CLAWSHOT_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.NORTH_CASTLE_TOWN_GOLDEN_WOLF,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.can_reach_region(RoomName.HIDDEN_VILLAGE, player) and can_complete_MDH(state, player))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_LANAYRU_SPRING_LEFT_STATUE_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_LANAYRU_SPRING_RIGHT_STATUE_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_DOUBLE_CLAWSHOT_CHASM_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_FEMALE_LADYBUG,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_FOUNTAIN_CHEST,
		lambda state: (state.has(ItemList.Spinner, player) and state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_GOLDEN_WOLF,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.can_reach_region(RoomName.NORTH_FARON_WOODS, player))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_MALE_LADYBUG,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_TEKTITE_GROTTO_CHEST,
		lambda state: (can_defeat_Tektite(state, player))
	)
    set_rule_if_exists(
		CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_TIGHTROPE_CHEST,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.PLUMM_FRUIT_BALLOON_MINIGAME,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.STAR_PRIZE_1,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1))
	)
    set_rule_if_exists(
		CheckName.STAR_PRIZE_2,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2))
	)
    set_rule_if_exists(
		CheckName.TELMA_INVOICE,
		lambda state: (state.has(ItemList.RenadosLetter, player))
	)
    set_rule_if_exists(
		CheckName.UPPER_ZORAS_RIVER_FEMALE_DRAGONFLY,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.UPPER_ZORAS_RIVER_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.WEST_HYRULE_FIELD_FEMALE_BUTTERFLY,
		lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.GaleBoomerang, player) or state.can_reach_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE, player, player))
	)
    set_rule_if_exists(
		CheckName.WEST_HYRULE_FIELD_GOLDEN_WOLF,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.can_reach_region(RoomName.UPPER_ZORAS_RIVER, player))
	)
    set_rule_if_exists(
		CheckName.WEST_HYRULE_FIELD_HELMASAUR_GROTTO_CHEST,
		lambda state: (can_defeat_Helmasaur(state, player))
	)
    set_rule_if_exists(
		CheckName.WEST_HYRULE_FIELD_MALE_BUTTERFLY,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.WOODEN_STATUE,
		lambda state: (state.can_reach_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER, player) and state.has(ItemList.ShadowCrystal, player) and state.can_reach_region(RoomName.CASTLE_TOWN_SOUTH, player))
	)
    set_rule_if_exists(
		CheckName.ZORAS_DOMAIN_CHEST_BEHIND_WATERFALL,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.ZORAS_DOMAIN_CHEST_BY_MOTHER_AND_CHILD_ISLES,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ZORAS_DOMAIN_EXTINGUISH_ALL_TORCHES_CHEST,
		lambda state: (state.has(ItemList.GaleBoomerang, player) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.ZORAS_DOMAIN_LIGHT_ALL_TORCHES_CHEST,
		lambda state: (state.has(ItemList.Lantern, player) and state.has(ItemList.IronBoots, player))
	)
    set_rule_if_exists(
		CheckName.ZORAS_DOMAIN_MALE_DRAGONFLY,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ZORAS_DOMAIN_MOTHER_AND_CHILD_ISLE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.ZORAS_DOMAIN_UNDERWATER_GORON,
		lambda state: (can_use_water_bombs(state, player) and state.has(ItemList.IronBoots, player) and state.has(ItemList.ZoraArmor, player))
	)
    set_rule_if_exists(
		CheckName.ZORAS_DOMAIN_WATERFALL_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.HERDING_GOATS_REWARD,
		lambda state: (can_complete_prologue(state, player) and can_change_time(state, player))
	)
    set_rule_if_exists(
		CheckName.LINKS_BASEMENT_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.ORDON_CAT_RESCUE,
		lambda state: (state.can_reach_region(RoomName.ORDON_VILLAGE, player) and state.has(ItemList.ProgressiveFishingRod, player, 1) and can_change_time(state, player))
	)
    set_rule_if_exists(
		CheckName.ORDON_RANCH_GROTTO_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player))
	)
    set_rule_if_exists(
		CheckName.ORDON_SHIELD,
		lambda state: ((((state._tp_faron_twilight_cleared(player)) and can_complete_prologue(state, player)) or ((state._tp_faron_twilight_cleared(player)) and state.has(ItemList.ShadowCrystal, player))) and ((not state._tp_bonks_do_damage(player)) or ((state._tp_bonks_do_damage(player)) and ((state._tp_damage_magnification(player) != DamageMagnification.option_ohko) or can_use_bottled_fairies(state, player)))))
	)
    set_rule_if_exists(
		CheckName.ORDON_SPRING_GOLDEN_WOLF,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.can_reach_region(RoomName.DEATH_MOUNTAIN_TRAIL, player))
	)
    set_rule_if_exists(
		CheckName.ORDON_SWORD,
		lambda state: (can_complete_prologue(state, player) or (state._tp_faron_twilight_cleared(player)))
	)
    set_rule_if_exists(
		CheckName.SERA_SHOP_SLINGSHOT,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ULI_CRADLE_DELIVERY,
		lambda state: (can_change_time(state, player))
	)
    set_rule_if_exists(
		CheckName.WOODEN_SWORD_CHEST,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.WRESTLING_WITH_BO,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.ASHEI_SKETCH,
		lambda state: (True)
	)
    set_rule_if_exists(
		CheckName.SNOWBOARD_RACING_PRIZE,
		lambda state: (can_complete_snowpeak_ruins(state, player) and can_defeat_ShadowBeast(state, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_ABOVE_FREEZARD_GROTTO_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_BLIZZARD_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_CAVE_ICE_LANTERN_CHEST,
		lambda state: (state.has(ItemList.Lantern, player) and state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_CAVE_ICE_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_FREEZARD_GROTTO_CHEST,
		lambda state: (state.has(ItemList.BallAndChain, player))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_ICY_SUMMIT_POE,
		lambda state: (state.has(ItemList.ShadowCrystal, player) and can_defeat_ShadowBeast(state, player) and ((not state._tp_bonks_do_damage(player)) or ((state._tp_bonks_do_damage(player)) and ((state._tp_damage_magnification(player) != DamageMagnification.option_ohko) or can_use_bottled_fairy(state, player)))))
	)
    set_rule_if_exists(
		CheckName.SNOWPEAK_POE_AMONG_TREES,
		lambda state: (state.has(ItemList.ShadowCrystal, player))
	)