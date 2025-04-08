from typing import Callable, Dict
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


    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_ENTRANCE} -> {RoomName.OUTSIDE_ARBITERS_GROUNDS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_ENTRANCE} -> {RoomName.ARBITERS_GROUNDS_LOBBY}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.ArbitersGroundsSmallKey, player, 1) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_LOBBY} -> {RoomName.ARBITERS_GROUNDS_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_LOBBY} -> {RoomName.ARBITERS_GROUNDS_EAST_WING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_LOBBY} -> {RoomName.ARBITERS_GROUNDS_WEST_WING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_LOBBY} -> {RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE}")
    set_rule(
        exit,
          lambda state: (can_defeat_Poe(state, player) and state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_RedeadKnight(state, player) and can_defeat_Stalchild(state, player) and can_defeat_Bubble(state, player) and can_defeat_GhoulRat(state, player) and can_defeat_Stalfos(state, player) and (state.has(ItemList.ArbitersGroundsSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_EAST_WING} -> {RoomName.ARBITERS_GROUNDS_LOBBY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_WEST_WING} -> {RoomName.ARBITERS_GROUNDS_LOBBY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE} -> {RoomName.ARBITERS_GROUNDS_LOBBY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE} -> {RoomName.ARBITERS_GROUNDS_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Spinner, player) and (state.has(ItemList.ArbitersGroundsBigKey, player) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.ARBITERS_GROUNDS_BOSS_ROOM} -> {RoomName.MIRROR_CHAMBER_LOWER}")
    set_rule(
        exit,
          lambda state: (can_defeat_Stallord(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_BOSS_ROOM} -> {RoomName.CITY_IN_THE_SKY_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (can_defeat_Argorok(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR} -> {RoomName.CITY_IN_THE_SKY_WEST_WING}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR} -> {RoomName.CITY_IN_THE_SKY_LOBBY}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.IronBoots, player) and state.has(ItemList.ShadowCrystal, player)) and (state._tp_damage_magnification(player) != DamageMagnification.option_ohko)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_EAST_WING} -> {RoomName.CITY_IN_THE_SKY_LOBBY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_ENTRANCE} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_ENTRANCE} -> {RoomName.CITY_IN_THE_SKY_LOBBY}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_LOBBY} -> {RoomName.CITY_IN_THE_SKY_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_LOBBY} -> {RoomName.CITY_IN_THE_SKY_EAST_WING}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Spinner, player) and (state.has(ItemList.CityInTheSkySmallKey, player, 1) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_LOBBY} -> {RoomName.CITY_IN_THE_SKY_WEST_WING}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_LOBBY} -> {RoomName.CITY_IN_THE_SKY_NORTH_WING}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_BabaSerpent(state, player) and can_defeat_Kargarok(state, player) and state.has(ItemList.ShadowCrystal, player) and state.has(ItemList.IronBoots, player)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_NORTH_WING} -> {RoomName.CITY_IN_THE_SKY_LOBBY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_NORTH_WING} -> {RoomName.CITY_IN_THE_SKY_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_Aeralfos(state, player) and (state.has(ItemList.CityInTheSkyBigKey, player) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_WEST_WING} -> {RoomName.CITY_IN_THE_SKY_LOBBY}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2)),
    )

    exit = world.get_entrance(f"{RoomName.CITY_IN_THE_SKY_WEST_WING} -> {RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 2)),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_BOSS_ROOM} -> {RoomName.SOUTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (can_defeat_Diababa(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_EAST_WING} -> {RoomName.FOREST_TEMPLE_LOBBY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_EAST_WING} -> {RoomName.FOREST_TEMPLE_NORTH_WING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_ENTRANCE} -> {RoomName.NORTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_ENTRANCE} -> {RoomName.FOREST_TEMPLE_LOBBY}")
    set_rule(
        exit,
          lambda state: (can_defeat_Walltula(state, player) and can_defeat_Bokoblin(state, player) and can_break_monkey_cage(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_LOBBY} -> {RoomName.FOREST_TEMPLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_LOBBY} -> {RoomName.FOREST_TEMPLE_EAST_WING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_LOBBY} -> {RoomName.FOREST_TEMPLE_WEST_WING}")
    set_rule(
        exit,
          lambda state: (can_burn_webs(state, player) and (((state.has(ItemList.ForestTempleSmallKey, player, 2) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_Bokoblin(state, player)) or state.has(ItemList.ProgressiveClawshot, player, 1))),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_LOBBY} -> {RoomName.OOK}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player) and can_defeat_Walltula(state, player) and can_defeat_Bokoblin(state, player) and can_break_monkey_cage(state, player) and (state.has(ItemList.ForestTempleSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_NORTH_WING} -> {RoomName.FOREST_TEMPLE_EAST_WING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_NORTH_WING} -> {RoomName.FOREST_TEMPLE_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.ForestTempleBigKey, player) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy)) and state.has(ItemList.GaleBoomerang, player) and (can_free_all_monkeys(state, player) or state.has(ItemList.ProgressiveClawshot, player, 1))),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_WEST_WING} -> {RoomName.FOREST_TEMPLE_LOBBY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FOREST_TEMPLE_WEST_WING} -> {RoomName.OOK}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.GaleBoomerang, player)),
    )

    exit = world.get_entrance(f"{RoomName.OOK} -> {RoomName.FOREST_TEMPLE_WEST_WING}")
    set_rule(
        exit,
          lambda state: (can_defeat_Ook(state, player) and state.has(ItemList.GaleBoomerang, player)),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_BOSS_ROOM} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (can_defeat_Fyrus(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM} -> {RoomName.GORON_MINES_MAGNET_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM} -> {RoomName.GORON_MINES_NORTH_WING}")
    set_rule(
        exit,
          lambda state: (((state.has(ItemList.IronBoots, player) and has_sword(state, player)) or state.has(ItemList.ProgressiveHerosBow, player, 1)) and (state.has(ItemList.GoronMinesSmallKey, player, 2) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_ENTRANCE} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_ENTRANCE} -> {RoomName.GORON_MINES_MAGNET_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player) and can_break_wooden_door(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_LOWER_WEST_WING} -> {RoomName.GORON_MINES_MAGNET_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_MAGNET_ROOM} -> {RoomName.GORON_MINES_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_MAGNET_ROOM} -> {RoomName.GORON_MINES_LOWER_WEST_WING}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.GoronMinesSmallKey, player, 1) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_MAGNET_ROOM} -> {RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.GoronMinesSmallKey, player, 1) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.IronBoots, player)),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_NORTH_WING} -> {RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_NORTH_WING} -> {RoomName.GORON_MINES_UPPER_EAST_WING}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.GoronMinesSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_NORTH_WING} -> {RoomName.GORON_MINES_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1) and state.has(ItemList.IronBoots, player) and can_defeat_Bulblin(state, player) and (state.has(ItemList.GoronMinesKeyShard, player, 3) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_UPPER_EAST_WING} -> {RoomName.GORON_MINES_NORTH_WING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GORON_MINES_UPPER_EAST_WING} -> {RoomName.GORON_MINES_MAGNET_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player) and can_defeat_Dangoro(state, player) and state.has(ItemList.ProgressiveHerosBow, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.GANONDORF_CASTLE} -> {RoomName.HYRULE_CASTLE_TOWER_CLIMB}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_ENTRANCE} -> {RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_ENTRANCE} -> {RoomName.HYRULE_CASTLE_MAIN_HALL}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.HyruleCastleSmallKey, player, 1) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_ENTRANCE} -> {RoomName.HYRULE_CASTLE_OUTSIDE_WEST_WING}")
    set_rule(
        exit,
          lambda state: (can_defeat_Bokoblin_Red(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_ENTRANCE} -> {RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING}")
    set_rule(
        exit,
          lambda state: (can_defeat_Bokoblin_Red(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_GRAVEYARD} -> {RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_INSIDE_EAST_WING} -> {RoomName.HYRULE_CASTLE_MAIN_HALL}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_INSIDE_EAST_WING} -> {RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player) and can_defeat_Dinalfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_INSIDE_WEST_WING} -> {RoomName.HYRULE_CASTLE_MAIN_HALL}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_INSIDE_WEST_WING} -> {RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY}")
    set_rule(
        exit,
          lambda state: (can_knock_down_hc_painting(state, player) and can_defeat_Lizalfos(state, player) and can_defeat_Darknut(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_MAIN_HALL} -> {RoomName.HYRULE_CASTLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_MAIN_HALL} -> {RoomName.HYRULE_CASTLE_INSIDE_EAST_WING}")
    set_rule(
        exit,
          lambda state: (can_defeat_Bokoblin(state, player) and can_defeat_Lizalfos(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_Darknut(state, player) and state.has(ItemList.GaleBoomerang, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_MAIN_HALL} -> {RoomName.HYRULE_CASTLE_INSIDE_WEST_WING}")
    set_rule(
        exit,
          lambda state: (can_defeat_Bokoblin(state, player) and can_defeat_Lizalfos(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_Darknut(state, player) and state.has(ItemList.GaleBoomerang, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING} -> {RoomName.HYRULE_CASTLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING} -> {RoomName.HYRULE_CASTLE_GRAVEYARD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_OUTSIDE_WEST_WING} -> {RoomName.HYRULE_CASTLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY} -> {RoomName.HYRULE_CASTLE_INSIDE_WEST_WING}")
    set_rule(
        exit,
          lambda state: (can_defeat_Darknut(state, player) and can_defeat_Lizalfos(state, player) and can_knock_down_hc_painting(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY} -> {RoomName.HYRULE_CASTLE_INSIDE_EAST_WING}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player) and can_defeat_Dinalfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY} -> {RoomName.HYRULE_CASTLE_TOWER_CLIMB}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.HyruleCastleSmallKey, player, 2) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_TOWER_CLIMB} -> {RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_TOWER_CLIMB} -> {RoomName.HYRULE_CASTLE_TREASURE_ROOM}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.HyruleCastleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.Spinner, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_Darknut(state, player) and can_defeat_Lizalfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_TOWER_CLIMB} -> {RoomName.GANONDORF_CASTLE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Spinner, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_Darknut(state, player) and can_defeat_Lizalfos(state, player) and (state.has(ItemList.HyruleCastleBigKey, player) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy)) and can_defeat_Ganondorf(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_CASTLE_TREASURE_ROOM} -> {RoomName.HYRULE_CASTLE_TOWER_CLIMB}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_BOSS_ROOM} -> {RoomName.LAKE_HYLIA_LANAYRU_SPRING}")
    set_rule(
        exit,
          lambda state: (can_defeat_Morpheel(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.LakebedTempleSmallKey, player, 1) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_WEST_WING}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_smash(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.LakebedTempleSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_launch_bombs(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and (state.has(ItemList.LakebedTempleBigKey, player) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR} -> {RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR} -> {RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR} -> {RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR}")
    set_rule(
        exit,
          lambda state: (can_launch_bombs(state, player) or state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_ENTRANCE} -> {RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_ENTRANCE} -> {RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM}")
    set_rule(
        exit,
          lambda state: (can_launch_bombs(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKEBED_TEMPLE_WEST_WING} -> {RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_ENTRANCE} -> {RoomName.MIRROR_CHAMBER_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_ENTRANCE} -> {RoomName.PALACE_OF_TWILIGHT_WEST_WING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_ENTRANCE} -> {RoomName.PALACE_OF_TWILIGHT_EAST_WING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_ENTRANCE} -> {RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveMasterSword, player, 4)),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_WEST_WING} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_EAST_WING} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.PalaceOfTwilightSmallKey, player, 5) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.ProgressiveMasterSword, player, 4)),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.PalaceOfTwilightSmallKey, player, 6) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER} -> {RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER} -> {RoomName.PALACE_OF_TWILIGHT_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: (can_defeat_ZantHead(state, player) and state.has(ItemList.ProgressiveMasterSword, player, 4) and (state.has(ItemList.PalaceOfTwilightBigKey, player) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy)) and can_defeat_ShadowBeast(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and (state.has(ItemList.PalaceOfTwilightSmallKey, player, 7) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.PALACE_OF_TWILIGHT_BOSS_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (can_defeat_Zant(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_LEFT_DOOR} -> {RoomName.SNOWPEAK_RUINS_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_LEFT_DOOR} -> {RoomName.SNOWPEAK_SUMMIT_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_RIGHT_DOOR} -> {RoomName.SNOWPEAK_RUINS_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_RIGHT_DOOR} -> {RoomName.SNOWPEAK_SUMMIT_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_BOSS_ROOM} -> {RoomName.SNOWPEAK_SUMMIT_LOWER}")
    set_rule(
        exit,
          lambda state: (can_defeat_Blizzeta(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.BallAndChain, player) and (state.has(ItemList.SnowpeakRuinsSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.BallAndChain, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.SnowpeakRuinsSmallKey, player, 2) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_CHAPEL} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (can_defeat_Chilfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_DARKHAMMER_ROOM} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (can_defeat_Darkhammer(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_EAST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player) or state.has(ItemList.BallAndChain, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_EAST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.BallAndChain, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_EAST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR}")
    set_rule(
        exit,
          lambda state: (((state.has(ItemList.SnowpeakRuinsSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_MiniFreezard(state, player)) or ((state.has(ItemList.SnowpeakRuinsSmallKey, player, 2) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_MiniFreezard(state, player))),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_ENTRANCE} -> {RoomName.SNOWPEAK_RUINS_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_ENTRANCE} -> {RoomName.SNOWPEAK_RUINS_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_ENTRANCE} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR} -> {RoomName.SNOWPEAK_RUINS_EAST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}")
    set_rule(
        exit,
          lambda state: (can_defeat_Chilfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR} -> {RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.BallAndChain, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_EAST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player) or state.has(ItemList.BallAndChain, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.BallAndChain, player) and state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_Chilfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.SnowpeakRuinsSmallKey, player, 4) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM} -> {RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_EAST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.BallAndChain, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_CHAPEL}")
    set_rule(
        exit,
          lambda state: (((state.has(ItemList.SnowpeakRuinsSmallKey, player, 4) and state.has(ItemList.OrdonGoatCheese, player)) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.BallAndChain, player) and has_bombs(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_DARKHAMMER_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.BallAndChain, player) or (((state.has(ItemList.SnowpeakRuinsSmallKey, player, 2) or state.has(ItemList.OrdonGoatCheese, player)) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and has_bombs(state, player))),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: (((state.has(ItemList.SnowpeakRuinsSmallKey, player, 4) and state.has(ItemList.OrdonGoatCheese, player)) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and state.has(ItemList.BallAndChain, player) and has_bombs(state, player) and (state.has(ItemList.BedroomKey, player) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM} -> {RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_YETO_AND_YETA} -> {RoomName.SNOWPEAK_RUINS_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_YETO_AND_YETA} -> {RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.OrdonGoatCheese, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_YETO_AND_YETA} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.OrdonPumpkin, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_RUINS_YETO_AND_YETA} -> {RoomName.SNOWPEAK_RUINS_EAST_COURTYARD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player) or state.has(ItemList.BallAndChain, player)),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER} -> {RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_BOSS_ROOM} -> {RoomName.SACRED_GROVE_PAST}")
    set_rule(
        exit,
          lambda state: (can_defeat_Armogohma(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM} -> {RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM} -> {RoomName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Spinner, player)),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM} -> {RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Spinner, player) and (state.has(ItemList.TempleOfTimeSmallKey, player, 2) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS} -> {RoomName.TEMPLE_OF_TIME_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS} -> {RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM}")
    set_rule(
        exit,
          lambda state: (has_ranged_item(state, player) and can_defeat_YoungGohma(state, player) and can_defeat_Lizalfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR} -> {RoomName.TEMPLE_OF_TIME_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR} -> {RoomName.TEMPLE_OF_TIME_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveDominionRod, player, 1) and (state.has(ItemList.TempleOfTimeBigKey, player) or (state._tp_big_key_settings(player) == BigKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_DARKNUT_ARENA} -> {RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR}")
    set_rule(
        exit,
          lambda state: (can_defeat_Darknut(state, player) and state.has(ItemList.ProgressiveDominionRod, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_ENTRANCE} -> {RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_ENTRANCE} -> {RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.TempleOfTimeSmallKey, player, 1) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_ENTRANCE} -> {RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.ProgressiveDominionRod, player, 1) and state.has(ItemList.ProgressiveHerosBow, player, 1) and state.has(ItemList.Spinner, player) and can_defeat_Lizalfos(state, player) and can_defeat_Dinalfos(state, player) and can_defeat_Darknut(state, player) and (state.has(ItemList.TempleOfTimeSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))) or (state._tp_tot_entrance(player))),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM} -> {RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS} -> {RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS} -> {RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1) and can_defeat_Lizalfos(state, player) and can_defeat_Dinalfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME} -> {RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME} -> {RoomName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and state.has(ItemList.Spinner, player)),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME} -> {RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR} -> {RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR} -> {RoomName.TEMPLE_OF_TIME_DARKNUT_ARENA}")
    set_rule(
        exit,
          lambda state: (can_defeat_Lizalfos(state, player) and can_defeat_BabyGohma(state, player) and can_defeat_YoungGohma(state, player) and can_defeat_Armos(state, player) and (state.has(ItemList.TempleOfTimeSmallKey, player, 3) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy))),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO} -> {RoomName.DEATH_MOUNTAIN_TRAIL}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player) or can_complete_goron_mines(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_TRAIL} -> {RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_TRAIL} -> {RoomName.DEATH_MOUNTAIN_VOLCANO}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_VOLCANO} -> {RoomName.DEATH_MOUNTAIN_TRAIL}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_VOLCANO} -> {RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player) and (can_defeat_Goron(state, player) or can_complete_goron_mines(state, player))),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_VOLCANO} -> {RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER}")
    set_rule(
        exit,
          lambda state: (state.can_reach_region(RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER) or (state._tp_goron_mines_enterance(player) == GoronMinesEntrance.option_open)),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_VOLCANO}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER} -> {RoomName.DEATH_MOUNTAIN_VOLCANO}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player)),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player) or (state._tp_goron_mines_enterance(player) == GoronMinesEntrance.option_no_wrestling) or (state._tp_goron_mines_enterance(player) != GoronMinesEntrance.option_closed)),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player) or (state._tp_goron_mines_enterance(player) == GoronMinesEntrance.option_no_wrestling) or (state._tp_goron_mines_enterance(player) != GoronMinesEntrance.option_closed)),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR} -> {RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player)),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL}")
    set_rule(
        exit,
          lambda state: ((can_reach_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL) and state.has(ItemList.IronBoots, player)) or (state._tp_goron_mines_enterance(player) == GoronMinesEntrance.option_no_wrestling) or (state._tp_goron_mines_enterance(player) != GoronMinesEntrance.option_closed)),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL}")
    set_rule(
        exit,
          lambda state: ((can_reach_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL) and state.has(ItemList.IronBoots, player)) or (state._tp_goron_mines_enterance(player) == GoronMinesEntrance.option_no_wrestling) or (state._tp_goron_mines_enterance(player) != GoronMinesEntrance.option_closed)),
    )

    exit = world.get_entrance(f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL} -> {RoomName.GORON_MINES_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HIDDEN_VILLAGE} -> {RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HIDDEN_VILLAGE} -> {RoomName.HIDDEN_VILLAGE_IMPAZ_HOUSE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1) and state.has(ItemList.ProgressiveDominionRod, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.HIDDEN_VILLAGE_IMPAZ_HOUSE} -> {RoomName.HIDDEN_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE} -> {RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE} -> {RoomName.KAKARIKO_GORGE_BEHIND_GATE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE} -> {RoomName.FARON_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE} -> {RoomName.ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE} -> {RoomName.KAKARIKO_GORGE_KEESE_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE} -> {RoomName.KAKARIKO_GORGE}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE} -> {RoomName.ELDIN_LANTERN_CAVE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE_BEHIND_GATE} -> {RoomName.KAKARIKO_GORGE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player) or state.has(ItemList.GateKeys, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE_BEHIND_GATE} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_LANTERN_CAVE} -> {RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GORGE_KEESE_GROTTO} -> {RoomName.KAKARIKO_GORGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN}")
    set_rule(
        exit,
          lambda state: (state.can_reach_region(RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD} -> {RoomName.KAKARIKO_GORGE}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD} -> {RoomName.KAKARIKO_VILLAGE_BEHIND_GATE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD} -> {RoomName.NORTH_ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_BOMSKIT_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN} -> {RoomName.ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (state.can_reach_region(RoomName.KAKARIKO_MALO_MART)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN} -> {RoomName.OUTSIDE_CASTLE_TOWN_EAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE} -> {RoomName.ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER} -> {RoomName.ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.NORTH_ELDIN_FIELD} -> {RoomName.ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.NORTH_ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE}")
    set_rule(
        exit,
          lambda state: (state.can_reach_region(RoomName.KAKARIKO_RENADOS_SANCTUARY) and state.has(ItemList.WoodenStatue, player)),
    )

    exit = world.get_entrance(f"{RoomName.NORTH_ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_GROTTO_PLATFORM}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Spinner, player)),
    )

    exit = world.get_entrance(f"{RoomName.NORTH_ELDIN_FIELD} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE} -> {RoomName.NORTH_ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (state.can_reach_region(RoomName.KAKARIKO_RENADOS_SANCTUARY) and state.has(ItemList.WoodenStatue, player)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE} -> {RoomName.HIDDEN_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_GROTTO_PLATFORM} -> {RoomName.NORTH_ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Spinner, player)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_GROTTO_PLATFORM} -> {RoomName.ELDIN_FIELD_STALFOS_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.IronBoots, player)),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER} -> {RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_BOMSKIT_GROTTO} -> {RoomName.ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO} -> {RoomName.ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ELDIN_FIELD_STALFOS_GROTTO} -> {RoomName.ELDIN_FIELD_GROTTO_PLATFORM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.UPPER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: ((can_complete_goron_mines(state, player) and can_change_time(state, player)) or can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_VILLAGE_BEHIND_GATE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_GORGE_BEHIND_GATE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_GRAVEYARD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_MALO_MART}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_BUG_HOUSE_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_TOP_OF_WATCHTOWER}")
    set_rule(
        exit,
          lambda state: (can_complete_goron_mines(state, player) and can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_TOP_OF_WATCHTOWER} -> {RoomName.UPPER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_TOP_OF_WATCHTOWER} -> {RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_VILLAGE_BEHIND_GATE} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.GateKeys, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_VILLAGE_BEHIND_GATE} -> {RoomName.ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BASEMENT}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BASEMENT} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_MALO_MART} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR} -> {RoomName.KAKARIKO_ELDE_INN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR} -> {RoomName.KAKARIKO_ELDE_INN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_ELDE_INN} -> {RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_ELDE_INN} -> {RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BUG_HOUSE_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BUG_HOUSE_DOOR} -> {RoomName.KAKARIKO_BUG_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE} -> {RoomName.KAKARIKO_BUG_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BUG_HOUSE} -> {RoomName.KAKARIKO_BUG_HOUSE_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BUG_HOUSE} -> {RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER} -> {RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER} -> {RoomName.UPPER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER} -> {RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR} -> {RoomName.UPPER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR} -> {RoomName.KAKARIKO_WATCHTOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT} -> {RoomName.UPPER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT} -> {RoomName.KAKARIKO_WATCHTOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR} -> {RoomName.KAKARIKO_TOP_OF_WATCHTOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR} -> {RoomName.KAKARIKO_WATCHTOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER} -> {RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER} -> {RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_WATCHTOWER} -> {RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GRAVEYARD} -> {RoomName.LOWER_KAKARIKO_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.KAKARIKO_GRAVEYARD} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.GateKeys, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and (state.has(ItemList.IronBoots, player) or state.has(ItemList.ZoraArmor, player)) and can_use_water_bombs(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.SOUTH_FARON_WOODS_BEHIND_GATE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.ORDON_BRIDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.FARON_FIELD}")
    set_rule(
        exit,
          lambda state: (can_clear_forest(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.FARON_WOODS_COROS_HOUSE_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS_BEHIND_GATE} -> {RoomName.SOUTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (state.can_reach_region(RoomName.SOUTH_FARON_WOODS) or state.has(ItemList.ShadowCrystal, player) or can_clear_forest(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS_BEHIND_GATE} -> {RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS_COROS_LEDGE} -> {RoomName.SOUTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS_COROS_LEDGE} -> {RoomName.FARON_WOODS_COROS_HOUSE_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA} -> {RoomName.SOUTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA} -> {RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE}")
    set_rule(
        exit,
          lambda state: (can_clear_forest(state, player) and state.has(ItemList.ProgressiveDominionRod, player, 2) and state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE} -> {RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE} -> {RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_COROS_HOUSE_LOWER} -> {RoomName.FARON_WOODS_COROS_HOUSE_UPPER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_COROS_HOUSE_LOWER} -> {RoomName.SOUTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_COROS_HOUSE_UPPER} -> {RoomName.FARON_WOODS_COROS_HOUSE_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_COROS_HOUSE_UPPER} -> {RoomName.SOUTH_FARON_WOODS_COROS_LEDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE} -> {RoomName.SOUTH_FARON_WOODS_BEHIND_GATE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE} -> {RoomName.FARON_WOODS_CAVE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_CAVE} -> {RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_CAVE} -> {RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE} -> {RoomName.MIST_AREA_INSIDE_MIST}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE} -> {RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player) or state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE} -> {RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_INSIDE_MIST} -> {RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_INSIDE_MIST} -> {RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_INSIDE_MIST} -> {RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_INSIDE_MIST} -> {RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST} -> {RoomName.MIST_AREA_INSIDE_MIST}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST} -> {RoomName.MIST_AREA_CENTER_STUMP}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST} -> {RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST} -> {RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_CENTER_STUMP} -> {RoomName.MIST_AREA_INSIDE_MIST}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_CENTER_STUMP} -> {RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE} -> {RoomName.MIST_AREA_INSIDE_MIST}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE} -> {RoomName.MIST_AREA_FARON_MIST_CAVE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS} -> {RoomName.MIST_AREA_INSIDE_MIST}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Lantern, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS} -> {RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS} -> {RoomName.NORTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.NorthFaronWoodsGateKey, player) or (state._tp_skip_prologue(player))),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE} -> {RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE} -> {RoomName.FARON_WOODS_CAVE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIST_AREA_FARON_MIST_CAVE} -> {RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.NORTH_FARON_WOODS} -> {RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.NORTH_FARON_WOODS} -> {RoomName.LOST_WOODS}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.NORTH_FARON_WOODS} -> {RoomName.FOREST_TEMPLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD} -> {RoomName.FARON_FIELD_BEHIND_BOULDER}")
    set_rule(
        exit,
          lambda state: (can_get_hot_spring_water(state, player) and state.can_reach_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH)),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD} -> {RoomName.SOUTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD} -> {RoomName.KAKARIKO_GORGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD} -> {RoomName.LAKE_HYLIA_BRIDGE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.GateKeys, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD} -> {RoomName.FARON_FIELD_CORNER_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD} -> {RoomName.FARON_FIELD_FISHING_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD_BEHIND_BOULDER} -> {RoomName.FARON_FIELD}")
    set_rule(
        exit,
          lambda state: (can_get_hot_spring_water(state, player) and state.can_reach_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH)),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD_BEHIND_BOULDER} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_INSIDE_BOULDER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD_CORNER_GROTTO} -> {RoomName.FARON_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FARON_FIELD_FISHING_GROTTO} -> {RoomName.FARON_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOST_WOODS} -> {RoomName.LOST_WOODS_LOWER_BATTLE_ARENA}")
    set_rule(
        exit,
          lambda state: ((can_defeat_SkullKid(state, player) and state.has(ItemList.ShadowCrystal, player)) or (state._tp_tot_entrance(player) == TotEntrance.option_open) or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)),
    )

    exit = world.get_entrance(f"{RoomName.LOST_WOODS} -> {RoomName.LOST_WOODS_UPPER_BATTLE_ARENA}")
    set_rule(
        exit,
          lambda state: ((can_defeat_SkullKid(state, player) and state.has(ItemList.ShadowCrystal, player)) or (state._tp_tot_entrance(player) == TotEntrance.option_open) or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)),
    )

    exit = world.get_entrance(f"{RoomName.LOST_WOODS} -> {RoomName.NORTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOST_WOODS_LOWER_BATTLE_ARENA} -> {RoomName.LOST_WOODS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LOST_WOODS_LOWER_BATTLE_ARENA} -> {RoomName.SACRED_GROVE_LOWER}")
    set_rule(
        exit,
          lambda state: (can_defeat_SkullKid(state, player) or (state._tp_tot_entrance(player) == TotEntrance.option_open) or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)),
    )

    exit = world.get_entrance(f"{RoomName.LOST_WOODS_LOWER_BATTLE_ARENA} -> {RoomName.LOST_WOODS_BABA_SERPENT_GROTTO}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player) and state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.LOST_WOODS_UPPER_BATTLE_ARENA} -> {RoomName.SACRED_GROVE_BEFORE_BLOCK}")
    set_rule(
        exit,
          lambda state: (can_defeat_SkullKid(state, player) or (state._tp_tot_entrance(player) == TotEntrance.option_open) or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)),
    )

    exit = world.get_entrance(f"{RoomName.LOST_WOODS_BABA_SERPENT_GROTTO} -> {RoomName.LOST_WOODS_LOWER_BATTLE_ARENA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_BEFORE_BLOCK} -> {RoomName.LOST_WOODS_UPPER_BATTLE_ARENA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_BEFORE_BLOCK} -> {RoomName.SACRED_GROVE_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_UPPER} -> {RoomName.SACRED_GROVE_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_UPPER} -> {RoomName.SACRED_GROVE_PAST}")
    set_rule(
        exit,
          lambda state: ((state._tp_tot_entrance(player) == TotEntrance.option_open) or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove) or (state.can_reach_region(RoomName.SACRED_GROVE_LOWER) and state.has(ItemList.ProgressiveMasterSword, player, 3) and can_defeat_ShadowBeast(state, player))),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_LOWER} -> {RoomName.LOST_WOODS_LOWER_BATTLE_ARENA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_LOWER} -> {RoomName.SACRED_GROVE_UPPER}")
    set_rule(
        exit,
          lambda state: (state.can_reach_region(RoomName.SACRED_GROVE_BEFORE_BLOCK) or (state._tp_tot_entrance(player) == TotEntrance.option_open) or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_PAST} -> {RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW}")
    set_rule(
        exit,
          lambda state: ((state._tp_tot_entrance(player) == TotEntrance.option_open) or state.has(ItemList.ProgressiveMasterSword, player, 3)),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_PAST} -> {RoomName.SACRED_GROVE_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW} -> {RoomName.SACRED_GROVE_PAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW} -> {RoomName.TEMPLE_OF_TIME_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_12_21}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Spinner, player) and can_defeat_Bokoblin(state, player) and can_defeat_Keese(state, player) and can_defeat_Rat(state, player) and can_defeat_BabaSerpent(state, player) and can_defeat_Skulltula(state, player) and can_defeat_Bulblin(state, player) and can_defeat_TorchSlug(state, player) and can_defeat_FireKeese(state, player) and can_defeat_Dodongo(state, player) and can_defeat_Tektite(state, player) and can_defeat_Lizalfos(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_12_21} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_22_31}")
    set_rule(
        exit,
          lambda state: (can_defeat_Helmasaur(state, player) and can_defeat_Rat(state, player) and state.has(ItemList.BallAndChain, player) and can_defeat_Chu(state, player) and can_defeat_ChuWorm(state, player) and can_defeat_Bubble(state, player) and can_defeat_Bulblin(state, player) and can_defeat_Keese(state, player) and can_defeat_Rat(state, player) and can_defeat_Stalhound(state, player) and can_defeat_Poe(state, player) and can_defeat_Leever(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_22_31} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_32_41}")
    set_rule(
        exit,
          lambda state: (can_defeat_Bokoblin(state, player) and can_defeat_IceKeese(state, player) and state.has(ItemList.ProgressiveDominionRod, player, 2) and can_defeat_Keese(state, player) and can_defeat_Rat(state, player) and can_defeat_GhoulRat(state, player) and can_defeat_Stalchild(state, player) and can_defeat_RedeadKnight(state, player) and can_defeat_Bulblin(state, player) and can_defeat_Stalfos(state, player) and can_defeat_Skulltula(state, player) and can_defeat_Bubble(state, player) and can_defeat_Lizalfos(state, player) and can_defeat_FireBubble(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_32_41} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_42_50}")
    set_rule(
        exit,
          lambda state: (can_defeat_Beamos(state, player) and can_defeat_Keese(state, player) and state.has(ItemList.ProgressiveClawshot, player, 2) and can_defeat_TorchSlug(state, player) and can_defeat_FireKeese(state, player) and can_defeat_Dodongo(state, player) and can_defeat_FireBubble(state, player) and can_defeat_RedeadKnight(state, player) and can_defeat_Poe(state, player) and can_defeat_GhoulRat(state, player) and can_defeat_Chu(state, player) and can_defeat_IceKeese(state, player) and can_defeat_Freezard(state, player) and can_defeat_Chilfos(state, player) and can_defeat_IceBubble(state, player) and can_defeat_Leever(state, player) and can_defeat_Darknut(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_42_50} -> {RoomName.LAKE_HYLIA_LANAYRU_SPRING}")
    set_rule(
        exit,
          lambda state: (can_defeat_Armos(state, player) and can_defeat_Bokoblin(state, player) and can_defeat_BabaSerpent(state, player) and can_defeat_Lizalfos(state, player) and can_defeat_Bulblin(state, player) and can_defeat_Dinalfos(state, player) and can_defeat_Poe(state, player) and can_defeat_RedeadKnight(state, player) and can_defeat_Chu(state, player) and can_defeat_Freezard(state, player) and can_defeat_Chilfos(state, player) and can_defeat_GhoulRat(state, player) and can_defeat_Rat(state, player) and can_defeat_Stalchild(state, player) and can_defeat_Aeralfos(state, player) and can_defeat_Darknut(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) and can_defeat_ShadowBeast(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT} -> {RoomName.GERUDO_DESERT_BASIN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT} -> {RoomName.GERUDO_DESERT_SKULLTULA_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU} -> {RoomName.GERUDO_DESERT}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_BASIN} -> {RoomName.GERUDO_DESERT}")
    set_rule(
        exit,
          lambda state: (can_defeat_Bulblin(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_BASIN} -> {RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_BASIN} -> {RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP}")
    set_rule(
        exit,
          lambda state: (can_defeat_Bulblin(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_BASIN} -> {RoomName.GERUDO_DESERT_CHU_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE} -> {RoomName.GERUDO_DESERT_BASIN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE} -> {RoomName.GERUDO_DESERT_ROCK_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP} -> {RoomName.GERUDO_DESERT_BASIN}")
    set_rule(
        exit,
          lambda state: (state.can_reach_region(RoomName.GERUDO_DESERT_BASIN) and can_defeat_Bulblin(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP} -> {RoomName.BULBLIN_CAMP}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_SKULLTULA_GROTTO} -> {RoomName.GERUDO_DESERT}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_CHU_GROTTO} -> {RoomName.GERUDO_DESERT_BASIN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.GERUDO_DESERT_ROCK_GROTTO} -> {RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.BULBLIN_CAMP} -> {RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.BULBLIN_CAMP} -> {RoomName.OUTSIDE_ARBITERS_GROUNDS}")
    set_rule(
        exit,
          lambda state: (((state.has(ItemList.GerudoDesertBulblinCampKey, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)) and can_defeat_KingBulblinDesert(state, player)) or (state._tp_skip_arbiters_entrance(player))),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_ARBITERS_GROUNDS} -> {RoomName.BULBLIN_CAMP}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_ARBITERS_GROUNDS} -> {RoomName.ARBITERS_GROUNDS_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIRROR_CHAMBER_LOWER} -> {RoomName.ARBITERS_GROUNDS_BOSS_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIRROR_CHAMBER_LOWER} -> {RoomName.MIRROR_CHAMBER_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.MIRROR_CHAMBER_UPPER} -> {RoomName.MIRROR_CHAMBER_LOWER}")
    set_rule(
        exit,
          lambda state: (can_defeat_ShadowBeast(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIRROR_CHAMBER_UPPER} -> {RoomName.MIRROR_CHAMBER_PORTAL}")
    set_rule(
        exit,
          lambda state: (can_defeat_ShadowBeast(state, player) and ((state._tp_palace_requirements(player) == PalaceRequirements.option_open) or ((state._tp_palace_requirements(player) == PalaceRequirements.option_fused_shadows) and state.has(ItemList.ProgressiveFusedShadow, player, 3)) or ((state._tp_palace_requirements(player) == PalaceRequirements.option_mirror_shards) and state.has(ItemList.ProgressiveMirrorShard, player, 4)) or ((state._tp_palace_requirements(player) == PalaceRequirements.option_vanilla) and can_complete_city_in_the_sky(state, player)))),
    )

    exit = world.get_entrance(f"{RoomName.MIRROR_CHAMBER_PORTAL} -> {RoomName.MIRROR_CHAMBER_UPPER}")
    set_rule(
        exit,
          lambda state: (can_defeat_ShadowBeast(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.MIRROR_CHAMBER_PORTAL} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_WEST} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_WEST} -> {RoomName.CASTLE_TOWN_CENTER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_WEST} -> {RoomName.CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_WEST} -> {RoomName.CASTLE_TOWN_STAR_GAME}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_STAR_GAME} -> {RoomName.CASTLE_TOWN_WEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_WEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_NORTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_EAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_MALO_MART}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR} -> {RoomName.CASTLE_TOWN_CENTER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR} -> {RoomName.CASTLE_TOWN_GORON_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR} -> {RoomName.CASTLE_TOWN_CENTER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR} -> {RoomName.CASTLE_TOWN_GORON_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_GORON_HOUSE} -> {RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_GORON_HOUSE} -> {RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_MALO_MART} -> {RoomName.CASTLE_TOWN_CENTER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_NORTH} -> {RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR}")
    set_rule(
        exit,
          lambda state: (can_complete_MDH(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_NORTH} -> {RoomName.CASTLE_TOWN_CENTER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR} -> {RoomName.CASTLE_TOWN_NORTH}")
    set_rule(
        exit,
          lambda state: (can_complete_MDH(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR} -> {RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER}")
    set_rule(
        exit,
          lambda state: ((state._tp_castle_requirements(player) == CastleRequirements.option_open) or ((state._tp_castle_requirements(player) == CastleRequirements.option_vanilla) and can_complete_palace_of_twilight(state, player)) or ((state._tp_castle_requirements(player) == CastleRequirements.option_fused_shadows) and state.has(ItemList.ProgressiveFusedShadow, player, 3)) or ((state._tp_castle_requirements(player) == CastleRequirements.option_mirror_shards) and state.has(ItemList.ProgressiveMirrorShard, player, 4)) or ((state._tp_castle_requirements(player) == CastleRequirements.option_all_dungeons) and can_complete_all_dungeons(state, player))),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER} -> {RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR}")
    set_rule(
        exit,
          lambda state: (can_complete_MDH(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER} -> {RoomName.HYRULE_CASTLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_CENTER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.OUTSIDE_CASTLE_TOWN_EAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY} -> {RoomName.CASTLE_TOWN_EAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR} -> {RoomName.CASTLE_TOWN_EAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR} -> {RoomName.CASTLE_TOWN_EAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Invoice, player)),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.Invoice, player)),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_WEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_CENTER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_EAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_AGITHAS_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_SEER_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_JOVANIS_HOUSE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_TELMAS_BAR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_AGITHAS_HOUSE} -> {RoomName.CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_SEER_HOUSE} -> {RoomName.CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_JOVANIS_HOUSE} -> {RoomName.CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.CASTLE_TOWN_TELMAS_BAR} -> {RoomName.CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_CAVE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_BEHIND_BOULDER}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD} -> {RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD} -> {RoomName.NORTH_ELDIN_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_CHU_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_SKULLTULA_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_POE_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD_CAVE_ENTRANCE} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD_CAVE_ENTRANCE} -> {RoomName.LANAYRU_ICE_PUZZLE_CAVE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD_BEHIND_BOULDER} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD_BEHIND_BOULDER} -> {RoomName.ZORAS_DOMAIN_WEST_LEDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS} -> {RoomName.LAKE_HYLIA_BRIDGE}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_ICE_PUZZLE_CAVE} -> {RoomName.LANAYRU_FIELD_CAVE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD_CHU_GROTTO} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD_SKULLTULA_GROTTO} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LANAYRU_FIELD_POE_GROTTO} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST} -> {RoomName.CASTLE_TOWN_WEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST} -> {RoomName.LAKE_HYLIA_BRIDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST_HELMASAUR_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST_HELMASAUR_GROTTO} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_EAST} -> {RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_EAST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH} -> {RoomName.FARON_FIELD_BEHIND_BOULDER}")
    set_rule(
        exit,
          lambda state: (can_get_hot_spring_water(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_TEKTITE_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_INSIDE_BOULDER} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (can_get_hot_spring_water(state, player) and state.can_reach_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH)),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_TEKTITE_GROTTO} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE}")
    set_rule(
        exit,
          lambda state: (can_launch_bombs(state, player) and state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.FARON_FIELD}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.GateKeys, player) or (state._tp_small_key_settings(player) == SmallKeySettings.option_keysy)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE} -> {RoomName.LAKE_HYLIA_BRIDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE} -> {RoomName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO} -> {RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_CAVE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ZoraArmor, player) and ((state._tp_skip_lakebed_entrance(player)) or (state.has(ItemList.IronBoots, player) and can_use_water_bombs(state, player)))),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_BRIDGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.GERUDO_DESERT}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.AurusMemo, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.UPPER_ZORAS_RIVER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_LANAYRU_SPRING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_SHELL_BLADE_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA} -> {RoomName.CITY_IN_THE_SKY_ENTRANCE}")
    set_rule(
        exit,
          lambda state: ((state.has(ItemList.ProgressiveSkyBook, player, 7) or (state._tp_skip_city_in_the_sky_entrance(player))) and state.has(ItemList.ProgressiveClawshot, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_CAVE_ENTRANCE} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_CAVE_ENTRANCE} -> {RoomName.LAKE_HYLIA_LONG_CAVE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ZoraArmor, player) and ((state._tp_skip_lakebed_entrance(player)) or (state.has(ItemList.IronBoots, player) and can_use_water_bombs(state, player)))),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE} -> {RoomName.LAKEBED_TEMPLE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_LANAYRU_SPRING} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_LONG_CAVE} -> {RoomName.LAKE_HYLIA_CAVE_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_SHELL_BLADE_GROTTO} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_ZORAS_RIVER} -> {RoomName.LANAYRU_FIELD}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_ZORAS_RIVER} -> {RoomName.FISHING_HOLE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_ZORAS_RIVER} -> {RoomName.ZORAS_DOMAIN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_ZORAS_RIVER} -> {RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE}")
    set_rule(
        exit,
          lambda state: (has_sword(state, player) or (can_defeat_ShadowBeast(state, player) and (state._tp_transform_anywhere(player)))),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE} -> {RoomName.UPPER_ZORAS_RIVER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE} -> {RoomName.LAKE_HYLIA}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveHerosBow, player, 1)),
    )

    exit = world.get_entrance(f"{RoomName.FISHING_HOLE} -> {RoomName.UPPER_ZORAS_RIVER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FISHING_HOLE} -> {RoomName.FISHING_HOLE_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.FISHING_HOLE_HOUSE} -> {RoomName.FISHING_HOLE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ZORAS_DOMAIN} -> {RoomName.ZORAS_DOMAIN_WEST_LEDGE}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ProgressiveClawshot, player, 1) or state.has(ItemList.ShadowCrystal, player) or can_smash(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ZORAS_DOMAIN} -> {RoomName.UPPER_ZORAS_RIVER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ZORAS_DOMAIN} -> {RoomName.ZORAS_THRONE_ROOM}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ZORAS_DOMAIN} -> {RoomName.SNOWPEAK_CLIMB_LOWER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ZORAS_DOMAIN_WEST_LEDGE} -> {RoomName.ZORAS_DOMAIN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ZORAS_DOMAIN_WEST_LEDGE} -> {RoomName.LANAYRU_FIELD_BEHIND_BOULDER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ZORAS_THRONE_ROOM} -> {RoomName.ZORAS_DOMAIN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_LINKS_HOUSE} -> {RoomName.ORDON_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_LINKS_HOUSE} -> {RoomName.ORDON_SPRING}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.OUTSIDE_LINKS_HOUSE} -> {RoomName.ORDON_LINKS_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_LINKS_HOUSE} -> {RoomName.OUTSIDE_LINKS_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_VILLAGE} -> {RoomName.OUTSIDE_LINKS_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_RANCH_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_SERAS_SHOP}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_SHIELD_HOUSE}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_SWORD_HOUSE}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_BOS_HOUSE_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_SERAS_SHOP} -> {RoomName.ORDON_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_SHIELD_HOUSE} -> {RoomName.ORDON_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_SWORD_HOUSE} -> {RoomName.ORDON_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_BOS_HOUSE_LEFT_DOOR} -> {RoomName.ORDON_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_BOS_HOUSE_LEFT_DOOR} -> {RoomName.ORDON_BOS_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR} -> {RoomName.ORDON_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR} -> {RoomName.ORDON_BOS_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_BOS_HOUSE} -> {RoomName.ORDON_BOS_HOUSE_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_BOS_HOUSE} -> {RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_RANCH_ENTRANCE} -> {RoomName.ORDON_RANCH}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_RANCH_ENTRANCE} -> {RoomName.ORDON_VILLAGE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_RANCH} -> {RoomName.ORDON_RANCH_ENTRANCE}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_RANCH} -> {RoomName.ORDON_RANCH_STABLE}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_RANCH_STABLE} -> {RoomName.ORDON_RANCH}")
    set_rule(
        exit,
          lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_RANCH_STABLE} -> {RoomName.ORDON_RANCH_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_RANCH_GROTTO} -> {RoomName.ORDON_RANCH_STABLE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_SPRING} -> {RoomName.OUTSIDE_LINKS_HOUSE}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_SPRING} -> {RoomName.ORDON_BRIDGE}")
    set_rule(
        exit,
          lambda state: ((state.can_reach_region(RoomName.OUTSIDE_LINKS_HOUSE) and has_sword(state, player) and state.has(ItemList.Slingshot, player)) or (state._tp_skip_prologue(player))),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_BRIDGE} -> {RoomName.ORDON_SPRING}")
    set_rule(
        exit,
          lambda state: ((state.can_reach_region(RoomName.OUTSIDE_LINKS_HOUSE) and has_sword(state, player) and state.has(ItemList.Slingshot, player)) or (state._tp_skip_prologue(player))),
    )

    exit = world.get_entrance(f"{RoomName.ORDON_BRIDGE} -> {RoomName.SOUTH_FARON_WOODS}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_CLIMB_LOWER} -> {RoomName.SNOWPEAK_CLIMB_UPPER}")
    set_rule(
        exit,
          lambda state: (((state._tp_skip_snowpeak_entrance(player)) or (state.can_reach_region(RoomName.ZORAS_DOMAIN) and state.has(ItemList.ProgressiveFishingRod, player, 2))) and state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_CLIMB_LOWER} -> {RoomName.ZORAS_DOMAIN}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_CLIMB_UPPER} -> {RoomName.SNOWPEAK_CLIMB_LOWER}")
    set_rule(
        exit,
          lambda state: (((state._tp_skip_snowpeak_entrance(player)) or (state.can_reach_region(RoomName.ZORAS_DOMAIN) and state.has(ItemList.ProgressiveFishingRod, player, 2))) and state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_CLIMB_UPPER} -> {RoomName.SNOWPEAK_SUMMIT_UPPER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_CLIMB_UPPER} -> {RoomName.SNOWPEAK_ICE_KEESE_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_CLIMB_UPPER} -> {RoomName.SNOWPEAK_FREEZARD_GROTTO}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_ICE_KEESE_GROTTO} -> {RoomName.SNOWPEAK_CLIMB_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_FREEZARD_GROTTO} -> {RoomName.SNOWPEAK_CLIMB_UPPER}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_SUMMIT_UPPER} -> {RoomName.SNOWPEAK_SUMMIT_LOWER}")
    set_rule(
        exit,
          lambda state: (can_defeat_ShadowBeast(state, player) and ((not state._tp_bonks_do_damage(player)) or ((state._tp_bonks_do_damage(player)) and ((state._tp_damage_magnification(player) != DamageMagnification.option_ohko) or can_use_bottled_fairy(state, player))))),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_SUMMIT_UPPER} -> {RoomName.SNOWPEAK_CLIMB_UPPER}")
    set_rule(
        exit,
          lambda state: (state.has(ItemList.ShadowCrystal, player)),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_SUMMIT_LOWER} -> {RoomName.SNOWPEAK_RUINS_LEFT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )

    exit = world.get_entrance(f"{RoomName.SNOWPEAK_SUMMIT_LOWER} -> {RoomName.SNOWPEAK_RUINS_RIGHT_DOOR}")
    set_rule(
        exit,
          lambda state: (True),
    )
