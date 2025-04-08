from BaseClasses import MultiWorld
from .Enums import RoomName

def connect_regions(world: MultiWorld, player: int) -> None:
    """Connect all regions according to the world layout"""

    world.get_region(RoomName.ARBITERS_GROUNDS_ENTRANCE, player).connect(
        world.get_region(RoomName.OUTSIDE_ARBITERS_GROUNDS, player),
        f"{RoomName.ARBITERS_GROUNDS_ENTRANCE} -> {RoomName.OUTSIDE_ARBITERS_GROUNDS}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_ENTRANCE, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_LOBBY, player),
        f"{RoomName.ARBITERS_GROUNDS_ENTRANCE} -> {RoomName.ARBITERS_GROUNDS_LOBBY}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_LOBBY, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_ENTRANCE, player),
        f"{RoomName.ARBITERS_GROUNDS_LOBBY} -> {RoomName.ARBITERS_GROUNDS_ENTRANCE}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_LOBBY, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_EAST_WING, player),
        f"{RoomName.ARBITERS_GROUNDS_LOBBY} -> {RoomName.ARBITERS_GROUNDS_EAST_WING}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_LOBBY, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_WEST_WING, player),
        f"{RoomName.ARBITERS_GROUNDS_LOBBY} -> {RoomName.ARBITERS_GROUNDS_WEST_WING}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_LOBBY, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE, player),
        f"{RoomName.ARBITERS_GROUNDS_LOBBY} -> {RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_EAST_WING, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_LOBBY, player),
        f"{RoomName.ARBITERS_GROUNDS_EAST_WING} -> {RoomName.ARBITERS_GROUNDS_LOBBY}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_WEST_WING, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_LOBBY, player),
        f"{RoomName.ARBITERS_GROUNDS_WEST_WING} -> {RoomName.ARBITERS_GROUNDS_LOBBY}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_LOBBY, player),
        f"{RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE} -> {RoomName.ARBITERS_GROUNDS_LOBBY}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_BOSS_ROOM, player),
        f"{RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE} -> {RoomName.ARBITERS_GROUNDS_BOSS_ROOM}"
    )

    world.get_region(RoomName.ARBITERS_GROUNDS_BOSS_ROOM, player).connect(
        world.get_region(RoomName.MIRROR_CHAMBER_LOWER, player),
        f"{RoomName.ARBITERS_GROUNDS_BOSS_ROOM} -> {RoomName.MIRROR_CHAMBER_LOWER}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_BOSS_ROOM, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_ENTRANCE, player),
        f"{RoomName.CITY_IN_THE_SKY_BOSS_ROOM} -> {RoomName.CITY_IN_THE_SKY_ENTRANCE}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_WEST_WING, player),
        f"{RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR} -> {RoomName.CITY_IN_THE_SKY_WEST_WING}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player),
        f"{RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR} -> {RoomName.CITY_IN_THE_SKY_LOBBY}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_EAST_WING, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player),
        f"{RoomName.CITY_IN_THE_SKY_EAST_WING} -> {RoomName.CITY_IN_THE_SKY_LOBBY}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_ENTRANCE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.CITY_IN_THE_SKY_ENTRANCE} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_ENTRANCE, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player),
        f"{RoomName.CITY_IN_THE_SKY_ENTRANCE} -> {RoomName.CITY_IN_THE_SKY_LOBBY}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_ENTRANCE, player),
        f"{RoomName.CITY_IN_THE_SKY_LOBBY} -> {RoomName.CITY_IN_THE_SKY_ENTRANCE}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_EAST_WING, player),
        f"{RoomName.CITY_IN_THE_SKY_LOBBY} -> {RoomName.CITY_IN_THE_SKY_EAST_WING}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_WEST_WING, player),
        f"{RoomName.CITY_IN_THE_SKY_LOBBY} -> {RoomName.CITY_IN_THE_SKY_WEST_WING}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_NORTH_WING, player),
        f"{RoomName.CITY_IN_THE_SKY_LOBBY} -> {RoomName.CITY_IN_THE_SKY_NORTH_WING}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_NORTH_WING, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player),
        f"{RoomName.CITY_IN_THE_SKY_NORTH_WING} -> {RoomName.CITY_IN_THE_SKY_LOBBY}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_NORTH_WING, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_BOSS_ROOM, player),
        f"{RoomName.CITY_IN_THE_SKY_NORTH_WING} -> {RoomName.CITY_IN_THE_SKY_BOSS_ROOM}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_WEST_WING, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_LOBBY, player),
        f"{RoomName.CITY_IN_THE_SKY_WEST_WING} -> {RoomName.CITY_IN_THE_SKY_LOBBY}"
    )

    world.get_region(RoomName.CITY_IN_THE_SKY_WEST_WING, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR, player),
        f"{RoomName.CITY_IN_THE_SKY_WEST_WING} -> {RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_BOSS_ROOM, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS, player),
        f"{RoomName.FOREST_TEMPLE_BOSS_ROOM} -> {RoomName.SOUTH_FARON_WOODS}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_EAST_WING, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_LOBBY, player),
        f"{RoomName.FOREST_TEMPLE_EAST_WING} -> {RoomName.FOREST_TEMPLE_LOBBY}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_EAST_WING, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_NORTH_WING, player),
        f"{RoomName.FOREST_TEMPLE_EAST_WING} -> {RoomName.FOREST_TEMPLE_NORTH_WING}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_ENTRANCE, player).connect(
        world.get_region(RoomName.NORTH_FARON_WOODS, player),
        f"{RoomName.FOREST_TEMPLE_ENTRANCE} -> {RoomName.NORTH_FARON_WOODS}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_ENTRANCE, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_LOBBY, player),
        f"{RoomName.FOREST_TEMPLE_ENTRANCE} -> {RoomName.FOREST_TEMPLE_LOBBY}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_LOBBY, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_ENTRANCE, player),
        f"{RoomName.FOREST_TEMPLE_LOBBY} -> {RoomName.FOREST_TEMPLE_ENTRANCE}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_LOBBY, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_EAST_WING, player),
        f"{RoomName.FOREST_TEMPLE_LOBBY} -> {RoomName.FOREST_TEMPLE_EAST_WING}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_LOBBY, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_WEST_WING, player),
        f"{RoomName.FOREST_TEMPLE_LOBBY} -> {RoomName.FOREST_TEMPLE_WEST_WING}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_LOBBY, player).connect(
        world.get_region(RoomName.OOK, player),
        f"{RoomName.FOREST_TEMPLE_LOBBY} -> {RoomName.OOK}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_NORTH_WING, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_EAST_WING, player),
        f"{RoomName.FOREST_TEMPLE_NORTH_WING} -> {RoomName.FOREST_TEMPLE_EAST_WING}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_NORTH_WING, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_BOSS_ROOM, player),
        f"{RoomName.FOREST_TEMPLE_NORTH_WING} -> {RoomName.FOREST_TEMPLE_BOSS_ROOM}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_WEST_WING, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_LOBBY, player),
        f"{RoomName.FOREST_TEMPLE_WEST_WING} -> {RoomName.FOREST_TEMPLE_LOBBY}"
    )

    world.get_region(RoomName.FOREST_TEMPLE_WEST_WING, player).connect(
        world.get_region(RoomName.OOK, player),
        f"{RoomName.FOREST_TEMPLE_WEST_WING} -> {RoomName.OOK}"
    )

    world.get_region(RoomName.OOK, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_WEST_WING, player),
        f"{RoomName.OOK} -> {RoomName.FOREST_TEMPLE_WEST_WING}"
    )

    world.get_region(RoomName.GORON_MINES_BOSS_ROOM, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.GORON_MINES_BOSS_ROOM} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM, player).connect(
        world.get_region(RoomName.GORON_MINES_MAGNET_ROOM, player),
        f"{RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM} -> {RoomName.GORON_MINES_MAGNET_ROOM}"
    )

    world.get_region(RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM, player).connect(
        world.get_region(RoomName.GORON_MINES_NORTH_WING, player),
        f"{RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM} -> {RoomName.GORON_MINES_NORTH_WING}"
    )

    world.get_region(RoomName.GORON_MINES_ENTRANCE, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL, player),
        f"{RoomName.GORON_MINES_ENTRANCE} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL}"
    )

    world.get_region(RoomName.GORON_MINES_ENTRANCE, player).connect(
        world.get_region(RoomName.GORON_MINES_MAGNET_ROOM, player),
        f"{RoomName.GORON_MINES_ENTRANCE} -> {RoomName.GORON_MINES_MAGNET_ROOM}"
    )

    world.get_region(RoomName.GORON_MINES_LOWER_WEST_WING, player).connect(
        world.get_region(RoomName.GORON_MINES_MAGNET_ROOM, player),
        f"{RoomName.GORON_MINES_LOWER_WEST_WING} -> {RoomName.GORON_MINES_MAGNET_ROOM}"
    )

    world.get_region(RoomName.GORON_MINES_MAGNET_ROOM, player).connect(
        world.get_region(RoomName.GORON_MINES_ENTRANCE, player),
        f"{RoomName.GORON_MINES_MAGNET_ROOM} -> {RoomName.GORON_MINES_ENTRANCE}"
    )

    world.get_region(RoomName.GORON_MINES_MAGNET_ROOM, player).connect(
        world.get_region(RoomName.GORON_MINES_LOWER_WEST_WING, player),
        f"{RoomName.GORON_MINES_MAGNET_ROOM} -> {RoomName.GORON_MINES_LOWER_WEST_WING}"
    )

    world.get_region(RoomName.GORON_MINES_MAGNET_ROOM, player).connect(
        world.get_region(RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM, player),
        f"{RoomName.GORON_MINES_MAGNET_ROOM} -> {RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM}"
    )

    world.get_region(RoomName.GORON_MINES_NORTH_WING, player).connect(
        world.get_region(RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM, player),
        f"{RoomName.GORON_MINES_NORTH_WING} -> {RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM}"
    )

    world.get_region(RoomName.GORON_MINES_NORTH_WING, player).connect(
        world.get_region(RoomName.GORON_MINES_UPPER_EAST_WING, player),
        f"{RoomName.GORON_MINES_NORTH_WING} -> {RoomName.GORON_MINES_UPPER_EAST_WING}"
    )

    world.get_region(RoomName.GORON_MINES_NORTH_WING, player).connect(
        world.get_region(RoomName.GORON_MINES_BOSS_ROOM, player),
        f"{RoomName.GORON_MINES_NORTH_WING} -> {RoomName.GORON_MINES_BOSS_ROOM}"
    )

    world.get_region(RoomName.GORON_MINES_UPPER_EAST_WING, player).connect(
        world.get_region(RoomName.GORON_MINES_NORTH_WING, player),
        f"{RoomName.GORON_MINES_UPPER_EAST_WING} -> {RoomName.GORON_MINES_NORTH_WING}"
    )

    world.get_region(RoomName.GORON_MINES_UPPER_EAST_WING, player).connect(
        world.get_region(RoomName.GORON_MINES_MAGNET_ROOM, player),
        f"{RoomName.GORON_MINES_UPPER_EAST_WING} -> {RoomName.GORON_MINES_MAGNET_ROOM}"
    )

    world.get_region(RoomName.GANONDORF_CASTLE, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_TOWER_CLIMB, player),
        f"{RoomName.GANONDORF_CASTLE} -> {RoomName.HYRULE_CASTLE_TOWER_CLIMB}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_ENTRANCE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER, player),
        f"{RoomName.HYRULE_CASTLE_ENTRANCE} -> {RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_ENTRANCE, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_MAIN_HALL, player),
        f"{RoomName.HYRULE_CASTLE_ENTRANCE} -> {RoomName.HYRULE_CASTLE_MAIN_HALL}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_ENTRANCE, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_OUTSIDE_WEST_WING, player),
        f"{RoomName.HYRULE_CASTLE_ENTRANCE} -> {RoomName.HYRULE_CASTLE_OUTSIDE_WEST_WING}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_ENTRANCE, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING, player),
        f"{RoomName.HYRULE_CASTLE_ENTRANCE} -> {RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_GRAVEYARD, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING, player),
        f"{RoomName.HYRULE_CASTLE_GRAVEYARD} -> {RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_INSIDE_EAST_WING, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_MAIN_HALL, player),
        f"{RoomName.HYRULE_CASTLE_INSIDE_EAST_WING} -> {RoomName.HYRULE_CASTLE_MAIN_HALL}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_INSIDE_EAST_WING, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY, player),
        f"{RoomName.HYRULE_CASTLE_INSIDE_EAST_WING} -> {RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_INSIDE_WEST_WING, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_MAIN_HALL, player),
        f"{RoomName.HYRULE_CASTLE_INSIDE_WEST_WING} -> {RoomName.HYRULE_CASTLE_MAIN_HALL}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_INSIDE_WEST_WING, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY, player),
        f"{RoomName.HYRULE_CASTLE_INSIDE_WEST_WING} -> {RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_MAIN_HALL, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_ENTRANCE, player),
        f"{RoomName.HYRULE_CASTLE_MAIN_HALL} -> {RoomName.HYRULE_CASTLE_ENTRANCE}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_MAIN_HALL, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_INSIDE_EAST_WING, player),
        f"{RoomName.HYRULE_CASTLE_MAIN_HALL} -> {RoomName.HYRULE_CASTLE_INSIDE_EAST_WING}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_MAIN_HALL, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_INSIDE_WEST_WING, player),
        f"{RoomName.HYRULE_CASTLE_MAIN_HALL} -> {RoomName.HYRULE_CASTLE_INSIDE_WEST_WING}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_ENTRANCE, player),
        f"{RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING} -> {RoomName.HYRULE_CASTLE_ENTRANCE}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_GRAVEYARD, player),
        f"{RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING} -> {RoomName.HYRULE_CASTLE_GRAVEYARD}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_OUTSIDE_WEST_WING, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_ENTRANCE, player),
        f"{RoomName.HYRULE_CASTLE_OUTSIDE_WEST_WING} -> {RoomName.HYRULE_CASTLE_ENTRANCE}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_INSIDE_WEST_WING, player),
        f"{RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY} -> {RoomName.HYRULE_CASTLE_INSIDE_WEST_WING}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_INSIDE_EAST_WING, player),
        f"{RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY} -> {RoomName.HYRULE_CASTLE_INSIDE_EAST_WING}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_TOWER_CLIMB, player),
        f"{RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY} -> {RoomName.HYRULE_CASTLE_TOWER_CLIMB}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_TOWER_CLIMB, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY, player),
        f"{RoomName.HYRULE_CASTLE_TOWER_CLIMB} -> {RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_TOWER_CLIMB, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_TREASURE_ROOM, player),
        f"{RoomName.HYRULE_CASTLE_TOWER_CLIMB} -> {RoomName.HYRULE_CASTLE_TREASURE_ROOM}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_TOWER_CLIMB, player).connect(
        world.get_region(RoomName.GANONDORF_CASTLE, player),
        f"{RoomName.HYRULE_CASTLE_TOWER_CLIMB} -> {RoomName.GANONDORF_CASTLE}"
    )

    world.get_region(RoomName.HYRULE_CASTLE_TREASURE_ROOM, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_TOWER_CLIMB, player),
        f"{RoomName.HYRULE_CASTLE_TREASURE_ROOM} -> {RoomName.HYRULE_CASTLE_TOWER_CLIMB}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_BOSS_ROOM, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_LANAYRU_SPRING, player),
        f"{RoomName.LAKEBED_TEMPLE_BOSS_ROOM} -> {RoomName.LAKE_HYLIA_LANAYRU_SPRING}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_ENTRANCE, player),
        f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_ENTRANCE}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR, player),
        f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR, player),
        f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_WEST_WING, player),
        f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_WEST_WING}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_BOSS_ROOM, player),
        f"{RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM} -> {RoomName.LAKEBED_TEMPLE_BOSS_ROOM}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player),
        f"{RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR} -> {RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player),
        f"{RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR} -> {RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR, player),
        f"{RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR} -> {RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_ENTRANCE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE, player),
        f"{RoomName.LAKEBED_TEMPLE_ENTRANCE} -> {RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_ENTRANCE, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player),
        f"{RoomName.LAKEBED_TEMPLE_ENTRANCE} -> {RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM}"
    )

    world.get_region(RoomName.LAKEBED_TEMPLE_WEST_WING, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player),
        f"{RoomName.LAKEBED_TEMPLE_WEST_WING} -> {RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player).connect(
        world.get_region(RoomName.MIRROR_CHAMBER_UPPER, player),
        f"{RoomName.PALACE_OF_TWILIGHT_ENTRANCE} -> {RoomName.MIRROR_CHAMBER_UPPER}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_WEST_WING, player),
        f"{RoomName.PALACE_OF_TWILIGHT_ENTRANCE} -> {RoomName.PALACE_OF_TWILIGHT_WEST_WING}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_EAST_WING, player),
        f"{RoomName.PALACE_OF_TWILIGHT_ENTRANCE} -> {RoomName.PALACE_OF_TWILIGHT_EAST_WING}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM, player),
        f"{RoomName.PALACE_OF_TWILIGHT_ENTRANCE} -> {RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_WEST_WING, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player),
        f"{RoomName.PALACE_OF_TWILIGHT_WEST_WING} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_EAST_WING, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player),
        f"{RoomName.PALACE_OF_TWILIGHT_EAST_WING} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player),
        f"{RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM, player),
        f"{RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM, player),
        f"{RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER, player),
        f"{RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM, player),
        f"{RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER} -> {RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_BOSS_ROOM, player),
        f"{RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER} -> {RoomName.PALACE_OF_TWILIGHT_BOSS_ROOM}"
    )

    world.get_region(RoomName.PALACE_OF_TWILIGHT_BOSS_ROOM, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player),
        f"{RoomName.PALACE_OF_TWILIGHT_BOSS_ROOM} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_LEFT_DOOR, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_ENTRANCE, player),
        f"{RoomName.SNOWPEAK_RUINS_LEFT_DOOR} -> {RoomName.SNOWPEAK_RUINS_ENTRANCE}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_LEFT_DOOR, player).connect(
        world.get_region(RoomName.SNOWPEAK_SUMMIT_LOWER, player),
        f"{RoomName.SNOWPEAK_RUINS_LEFT_DOOR} -> {RoomName.SNOWPEAK_SUMMIT_LOWER}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_ENTRANCE, player),
        f"{RoomName.SNOWPEAK_RUINS_RIGHT_DOOR} -> {RoomName.SNOWPEAK_RUINS_ENTRANCE}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.SNOWPEAK_SUMMIT_LOWER, player),
        f"{RoomName.SNOWPEAK_RUINS_RIGHT_DOOR} -> {RoomName.SNOWPEAK_SUMMIT_LOWER}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_BOSS_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_SUMMIT_LOWER, player),
        f"{RoomName.SNOWPEAK_RUINS_BOSS_ROOM} -> {RoomName.SNOWPEAK_SUMMIT_LOWER}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player),
        f"{RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_CHAPEL, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_CHAPEL} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_DARKHAMMER_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_DARKHAMMER_ROOM} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_EAST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player),
        f"{RoomName.SNOWPEAK_RUINS_EAST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_EAST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_EAST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_EAST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR, player),
        f"{RoomName.SNOWPEAK_RUINS_EAST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_ENTRANCE, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_LEFT_DOOR, player),
        f"{RoomName.SNOWPEAK_RUINS_ENTRANCE} -> {RoomName.SNOWPEAK_RUINS_LEFT_DOOR}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_ENTRANCE, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_RIGHT_DOOR, player),
        f"{RoomName.SNOWPEAK_RUINS_ENTRANCE} -> {RoomName.SNOWPEAK_RUINS_RIGHT_DOOR}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_ENTRANCE, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player),
        f"{RoomName.SNOWPEAK_RUINS_ENTRANCE} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_EAST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR} -> {RoomName.SNOWPEAK_RUINS_EAST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player),
        f"{RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR, player),
        f"{RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR} -> {RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player),
        f"{RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_ENTRANCE, player),
        f"{RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_ENTRANCE}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_EAST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_EAST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR, player),
        f"{RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM} -> {RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM} -> {RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player),
        f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_YETO_AND_YETA}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_EAST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_EAST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_CHAPEL, player),
        f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_CHAPEL}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_DARKHAMMER_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_DARKHAMMER_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_BOSS_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_WEST_COURTYARD} -> {RoomName.SNOWPEAK_RUINS_BOSS_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM} -> {RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_ENTRANCE, player),
        f"{RoomName.SNOWPEAK_RUINS_YETO_AND_YETA} -> {RoomName.SNOWPEAK_RUINS_ENTRANCE}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM, player),
        f"{RoomName.SNOWPEAK_RUINS_YETO_AND_YETA} -> {RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_YETO_AND_YETA} -> {RoomName.SNOWPEAK_RUINS_WEST_COURTYARD}"
    )

    world.get_region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_EAST_COURTYARD, player),
        f"{RoomName.SNOWPEAK_RUINS_YETO_AND_YETA} -> {RoomName.SNOWPEAK_RUINS_EAST_COURTYARD}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM, player),
        f"{RoomName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER} -> {RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_BOSS_ROOM, player).connect(
        world.get_region(RoomName.SACRED_GROVE_PAST, player),
        f"{RoomName.TEMPLE_OF_TIME_BOSS_ROOM} -> {RoomName.SACRED_GROVE_PAST}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS, player),
        f"{RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM} -> {RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER, player),
        f"{RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM} -> {RoomName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS, player),
        f"{RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM} -> {RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_ENTRANCE, player),
        f"{RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS} -> {RoomName.TEMPLE_OF_TIME_ENTRANCE}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM, player),
        f"{RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS} -> {RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_ENTRANCE, player),
        f"{RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR} -> {RoomName.TEMPLE_OF_TIME_ENTRANCE}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_BOSS_ROOM, player),
        f"{RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR} -> {RoomName.TEMPLE_OF_TIME_BOSS_ROOM}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_DARKNUT_ARENA, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR, player),
        f"{RoomName.TEMPLE_OF_TIME_DARKNUT_ARENA} -> {RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_ENTRANCE, player).connect(
        world.get_region(RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW, player),
        f"{RoomName.TEMPLE_OF_TIME_ENTRANCE} -> {RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_ENTRANCE, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS, player),
        f"{RoomName.TEMPLE_OF_TIME_ENTRANCE} -> {RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_ENTRANCE, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR, player),
        f"{RoomName.TEMPLE_OF_TIME_ENTRANCE} -> {RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME, player),
        f"{RoomName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM} -> {RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM, player),
        f"{RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS} -> {RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME, player),
        f"{RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS} -> {RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS, player),
        f"{RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME} -> {RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM, player),
        f"{RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME} -> {RoomName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR, player),
        f"{RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME} -> {RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME, player),
        f"{RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR} -> {RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME}"
    )

    world.get_region(RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_DARKNUT_ARENA, player),
        f"{RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR} -> {RoomName.TEMPLE_OF_TIME_DARKNUT_ARENA}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_TRAIL, player),
        f"{RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO} -> {RoomName.DEATH_MOUNTAIN_TRAIL}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_TRAIL, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO, player),
        f"{RoomName.DEATH_MOUNTAIN_TRAIL} -> {RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_TRAIL, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_VOLCANO, player),
        f"{RoomName.DEATH_MOUNTAIN_TRAIL} -> {RoomName.DEATH_MOUNTAIN_VOLCANO}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_VOLCANO, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_TRAIL, player),
        f"{RoomName.DEATH_MOUNTAIN_VOLCANO} -> {RoomName.DEATH_MOUNTAIN_TRAIL}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_VOLCANO, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL, player),
        f"{RoomName.DEATH_MOUNTAIN_VOLCANO} -> {RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_VOLCANO, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER, player),
        f"{RoomName.DEATH_MOUNTAIN_VOLCANO} -> {RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_VOLCANO, player),
        f"{RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_VOLCANO}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL, player),
        f"{RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_VOLCANO, player),
        f"{RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER} -> {RoomName.DEATH_MOUNTAIN_VOLCANO}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR, player),
        f"{RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL, player),
        f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR, player),
        f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL, player),
        f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER, player),
        f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR} -> {RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL, player),
        f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL, player),
        f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL} -> {RoomName.DEATH_MOUNTAIN_SUMO_HALL}"
    )

    world.get_region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL, player).connect(
        world.get_region(RoomName.GORON_MINES_ENTRANCE, player),
        f"{RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL} -> {RoomName.GORON_MINES_ENTRANCE}"
    )

    world.get_region(RoomName.HIDDEN_VILLAGE, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE, player),
        f"{RoomName.HIDDEN_VILLAGE} -> {RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE}"
    )

    world.get_region(RoomName.HIDDEN_VILLAGE, player).connect(
        world.get_region(RoomName.HIDDEN_VILLAGE_IMPAZ_HOUSE, player),
        f"{RoomName.HIDDEN_VILLAGE} -> {RoomName.HIDDEN_VILLAGE_IMPAZ_HOUSE}"
    )

    world.get_region(RoomName.HIDDEN_VILLAGE_IMPAZ_HOUSE, player).connect(
        world.get_region(RoomName.HIDDEN_VILLAGE, player),
        f"{RoomName.HIDDEN_VILLAGE_IMPAZ_HOUSE} -> {RoomName.HIDDEN_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE, player),
        f"{RoomName.KAKARIKO_GORGE} -> {RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE_BEHIND_GATE, player),
        f"{RoomName.KAKARIKO_GORGE} -> {RoomName.KAKARIKO_GORGE_BEHIND_GATE}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE, player).connect(
        world.get_region(RoomName.FARON_FIELD, player),
        f"{RoomName.KAKARIKO_GORGE} -> {RoomName.FARON_FIELD}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE, player).connect(
        world.get_region(RoomName.ELDIN_FIELD, player),
        f"{RoomName.KAKARIKO_GORGE} -> {RoomName.ELDIN_FIELD}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE_KEESE_GROTTO, player),
        f"{RoomName.KAKARIKO_GORGE} -> {RoomName.KAKARIKO_GORGE_KEESE_GROTTO}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE, player),
        f"{RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE} -> {RoomName.KAKARIKO_GORGE}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE, player).connect(
        world.get_region(RoomName.ELDIN_LANTERN_CAVE, player),
        f"{RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE} -> {RoomName.ELDIN_LANTERN_CAVE}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE_BEHIND_GATE, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE, player),
        f"{RoomName.KAKARIKO_GORGE_BEHIND_GATE} -> {RoomName.KAKARIKO_GORGE}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE_BEHIND_GATE, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_GORGE_BEHIND_GATE} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.ELDIN_LANTERN_CAVE, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE, player),
        f"{RoomName.ELDIN_LANTERN_CAVE} -> {RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE}"
    )

    world.get_region(RoomName.KAKARIKO_GORGE_KEESE_GROTTO, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE, player),
        f"{RoomName.KAKARIKO_GORGE_KEESE_GROTTO} -> {RoomName.KAKARIKO_GORGE}"
    )

    world.get_region(RoomName.ELDIN_FIELD, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN, player),
        f"{RoomName.ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN}"
    )

    world.get_region(RoomName.ELDIN_FIELD, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE, player),
        f"{RoomName.ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE}"
    )

    world.get_region(RoomName.ELDIN_FIELD, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE, player),
        f"{RoomName.ELDIN_FIELD} -> {RoomName.KAKARIKO_GORGE}"
    )

    world.get_region(RoomName.ELDIN_FIELD, player).connect(
        world.get_region(RoomName.KAKARIKO_VILLAGE_BEHIND_GATE, player),
        f"{RoomName.ELDIN_FIELD} -> {RoomName.KAKARIKO_VILLAGE_BEHIND_GATE}"
    )

    world.get_region(RoomName.ELDIN_FIELD, player).connect(
        world.get_region(RoomName.NORTH_ELDIN_FIELD, player),
        f"{RoomName.ELDIN_FIELD} -> {RoomName.NORTH_ELDIN_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_BOMSKIT_GROTTO, player),
        f"{RoomName.ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_BOMSKIT_GROTTO}"
    )

    world.get_region(RoomName.ELDIN_FIELD, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO, player),
        f"{RoomName.ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO}"
    )

    world.get_region(RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN, player).connect(
        world.get_region(RoomName.ELDIN_FIELD, player),
        f"{RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN} -> {RoomName.ELDIN_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_EAST, player),
        f"{RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN} -> {RoomName.OUTSIDE_CASTLE_TOWN_EAST}"
    )

    world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE, player).connect(
        world.get_region(RoomName.ELDIN_FIELD, player),
        f"{RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE} -> {RoomName.ELDIN_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER, player),
        f"{RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER}"
    )

    world.get_region(RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER, player).connect(
        world.get_region(RoomName.ELDIN_FIELD, player),
        f"{RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER} -> {RoomName.ELDIN_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER, player),
        f"{RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER}"
    )

    world.get_region(RoomName.NORTH_ELDIN_FIELD, player).connect(
        world.get_region(RoomName.ELDIN_FIELD, player),
        f"{RoomName.NORTH_ELDIN_FIELD} -> {RoomName.ELDIN_FIELD}"
    )

    world.get_region(RoomName.NORTH_ELDIN_FIELD, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE, player),
        f"{RoomName.NORTH_ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE}"
    )

    world.get_region(RoomName.NORTH_ELDIN_FIELD, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_GROTTO_PLATFORM, player),
        f"{RoomName.NORTH_ELDIN_FIELD} -> {RoomName.ELDIN_FIELD_GROTTO_PLATFORM}"
    )

    world.get_region(RoomName.NORTH_ELDIN_FIELD, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.NORTH_ELDIN_FIELD} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE, player).connect(
        world.get_region(RoomName.NORTH_ELDIN_FIELD, player),
        f"{RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE} -> {RoomName.NORTH_ELDIN_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE, player).connect(
        world.get_region(RoomName.HIDDEN_VILLAGE, player),
        f"{RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE} -> {RoomName.HIDDEN_VILLAGE}"
    )

    world.get_region(RoomName.ELDIN_FIELD_GROTTO_PLATFORM, player).connect(
        world.get_region(RoomName.NORTH_ELDIN_FIELD, player),
        f"{RoomName.ELDIN_FIELD_GROTTO_PLATFORM} -> {RoomName.NORTH_ELDIN_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD_GROTTO_PLATFORM, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_STALFOS_GROTTO, player),
        f"{RoomName.ELDIN_FIELD_GROTTO_PLATFORM} -> {RoomName.ELDIN_FIELD_STALFOS_GROTTO}"
    )

    world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE, player),
        f"{RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE}"
    )

    world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER, player),
        f"{RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER} -> {RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER}"
    )

    world.get_region(RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER, player),
        f"{RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER} -> {RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER}"
    )

    world.get_region(RoomName.ELDIN_FIELD_BOMSKIT_GROTTO, player).connect(
        world.get_region(RoomName.ELDIN_FIELD, player),
        f"{RoomName.ELDIN_FIELD_BOMSKIT_GROTTO} -> {RoomName.ELDIN_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO, player).connect(
        world.get_region(RoomName.ELDIN_FIELD, player),
        f"{RoomName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO} -> {RoomName.ELDIN_FIELD}"
    )

    world.get_region(RoomName.ELDIN_FIELD_STALFOS_GROTTO, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_GROTTO_PLATFORM, player),
        f"{RoomName.ELDIN_FIELD_STALFOS_GROTTO} -> {RoomName.ELDIN_FIELD_GROTTO_PLATFORM}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.UPPER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_VILLAGE_BEHIND_GATE, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_VILLAGE_BEHIND_GATE}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE_BEHIND_GATE, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_GORGE_BEHIND_GATE}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_GRAVEYARD, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_GRAVEYARD}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_MALO_MART, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_MALO_MART}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_BUG_HOUSE_DOOR, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_BUG_HOUSE_DOOR}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE}"
    )

    world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER, player),
        f"{RoomName.LOWER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER}"
    )

    world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_TOP_OF_WATCHTOWER, player),
        f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_TOP_OF_WATCHTOWER}"
    )

    world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER, player),
        f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER}"
    )

    world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR, player),
        f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR}"
    )

    world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT, player),
        f"{RoomName.UPPER_KAKARIKO_VILLAGE} -> {RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT}"
    )

    world.get_region(RoomName.KAKARIKO_TOP_OF_WATCHTOWER, player).connect(
        world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_TOP_OF_WATCHTOWER} -> {RoomName.UPPER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_TOP_OF_WATCHTOWER, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR, player),
        f"{RoomName.KAKARIKO_TOP_OF_WATCHTOWER} -> {RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_VILLAGE_BEHIND_GATE, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_VILLAGE_BEHIND_GATE} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_VILLAGE_BEHIND_GATE, player).connect(
        world.get_region(RoomName.ELDIN_FIELD, player),
        f"{RoomName.KAKARIKO_VILLAGE_BEHIND_GATE} -> {RoomName.ELDIN_FIELD}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BASEMENT, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY_BASEMENT}"
    )

    world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BASEMENT, player).connect(
        world.get_region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player),
        f"{RoomName.KAKARIKO_RENADOS_SANCTUARY_BASEMENT} -> {RoomName.KAKARIKO_RENADOS_SANCTUARY}"
    )

    world.get_region(RoomName.KAKARIKO_MALO_MART, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_MALO_MART} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_ELDE_INN, player),
        f"{RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR} -> {RoomName.KAKARIKO_ELDE_INN}"
    )

    world.get_region(RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_ELDE_INN, player),
        f"{RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR} -> {RoomName.KAKARIKO_ELDE_INN}"
    )

    world.get_region(RoomName.KAKARIKO_ELDE_INN, player).connect(
        world.get_region(RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR, player),
        f"{RoomName.KAKARIKO_ELDE_INN} -> {RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_ELDE_INN, player).connect(
        world.get_region(RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR, player),
        f"{RoomName.KAKARIKO_ELDE_INN} -> {RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_BUG_HOUSE_DOOR, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_BUG_HOUSE_DOOR} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_BUG_HOUSE_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_BUG_HOUSE, player),
        f"{RoomName.KAKARIKO_BUG_HOUSE_DOOR} -> {RoomName.KAKARIKO_BUG_HOUSE}"
    )

    world.get_region(RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE, player).connect(
        world.get_region(RoomName.KAKARIKO_BUG_HOUSE, player),
        f"{RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE} -> {RoomName.KAKARIKO_BUG_HOUSE}"
    )

    world.get_region(RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_BUG_HOUSE, player).connect(
        world.get_region(RoomName.KAKARIKO_BUG_HOUSE_DOOR, player),
        f"{RoomName.KAKARIKO_BUG_HOUSE} -> {RoomName.KAKARIKO_BUG_HOUSE_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_BUG_HOUSE, player).connect(
        world.get_region(RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE, player),
        f"{RoomName.KAKARIKO_BUG_HOUSE} -> {RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE}"
    )

    world.get_region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER, player).connect(
        world.get_region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER, player),
        f"{RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER} -> {RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER}"
    )

    world.get_region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER, player).connect(
        world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER} -> {RoomName.UPPER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER, player).connect(
        world.get_region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER, player),
        f"{RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER} -> {RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR, player).connect(
        world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR} -> {RoomName.UPPER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER, player),
        f"{RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR} -> {RoomName.KAKARIKO_WATCHTOWER}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT, player).connect(
        world.get_region(RoomName.UPPER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT} -> {RoomName.UPPER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER, player),
        f"{RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT} -> {RoomName.KAKARIKO_WATCHTOWER}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_TOP_OF_WATCHTOWER, player),
        f"{RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR} -> {RoomName.KAKARIKO_TOP_OF_WATCHTOWER}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER, player),
        f"{RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR} -> {RoomName.KAKARIKO_WATCHTOWER}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR, player),
        f"{RoomName.KAKARIKO_WATCHTOWER} -> {RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT, player),
        f"{RoomName.KAKARIKO_WATCHTOWER} -> {RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT}"
    )

    world.get_region(RoomName.KAKARIKO_WATCHTOWER, player).connect(
        world.get_region(RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR, player),
        f"{RoomName.KAKARIKO_WATCHTOWER} -> {RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR}"
    )

    world.get_region(RoomName.KAKARIKO_GRAVEYARD, player).connect(
        world.get_region(RoomName.LOWER_KAKARIKO_VILLAGE, player),
        f"{RoomName.KAKARIKO_GRAVEYARD} -> {RoomName.LOWER_KAKARIKO_VILLAGE}"
    )

    world.get_region(RoomName.KAKARIKO_GRAVEYARD, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.KAKARIKO_GRAVEYARD} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS_BEHIND_GATE, player),
        f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.SOUTH_FARON_WOODS_BEHIND_GATE}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA, player),
        f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.ORDON_BRIDGE, player),
        f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.ORDON_BRIDGE}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.FARON_FIELD, player),
        f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.FARON_FIELD}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.FARON_WOODS_COROS_HOUSE_LOWER, player),
        f"{RoomName.SOUTH_FARON_WOODS} -> {RoomName.FARON_WOODS_COROS_HOUSE_LOWER}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS_BEHIND_GATE, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS, player),
        f"{RoomName.SOUTH_FARON_WOODS_BEHIND_GATE} -> {RoomName.SOUTH_FARON_WOODS}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS_BEHIND_GATE, player).connect(
        world.get_region(RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE, player),
        f"{RoomName.SOUTH_FARON_WOODS_BEHIND_GATE} -> {RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS_COROS_LEDGE, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS, player),
        f"{RoomName.SOUTH_FARON_WOODS_COROS_LEDGE} -> {RoomName.SOUTH_FARON_WOODS}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS_COROS_LEDGE, player).connect(
        world.get_region(RoomName.FARON_WOODS_COROS_HOUSE_UPPER, player),
        f"{RoomName.SOUTH_FARON_WOODS_COROS_LEDGE} -> {RoomName.FARON_WOODS_COROS_HOUSE_UPPER}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS, player),
        f"{RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA} -> {RoomName.SOUTH_FARON_WOODS}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE, player),
        f"{RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA} -> {RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA, player),
        f"{RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE} -> {RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA}"
    )

    world.get_region(RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE, player).connect(
        world.get_region(RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST, player),
        f"{RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE} -> {RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST}"
    )

    world.get_region(RoomName.FARON_WOODS_COROS_HOUSE_LOWER, player).connect(
        world.get_region(RoomName.FARON_WOODS_COROS_HOUSE_UPPER, player),
        f"{RoomName.FARON_WOODS_COROS_HOUSE_LOWER} -> {RoomName.FARON_WOODS_COROS_HOUSE_UPPER}"
    )

    world.get_region(RoomName.FARON_WOODS_COROS_HOUSE_LOWER, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS, player),
        f"{RoomName.FARON_WOODS_COROS_HOUSE_LOWER} -> {RoomName.SOUTH_FARON_WOODS}"
    )

    world.get_region(RoomName.FARON_WOODS_COROS_HOUSE_UPPER, player).connect(
        world.get_region(RoomName.FARON_WOODS_COROS_HOUSE_LOWER, player),
        f"{RoomName.FARON_WOODS_COROS_HOUSE_UPPER} -> {RoomName.FARON_WOODS_COROS_HOUSE_LOWER}"
    )

    world.get_region(RoomName.FARON_WOODS_COROS_HOUSE_UPPER, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS_COROS_LEDGE, player),
        f"{RoomName.FARON_WOODS_COROS_HOUSE_UPPER} -> {RoomName.SOUTH_FARON_WOODS_COROS_LEDGE}"
    )

    world.get_region(RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS_BEHIND_GATE, player),
        f"{RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE} -> {RoomName.SOUTH_FARON_WOODS_BEHIND_GATE}"
    )

    world.get_region(RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE, player).connect(
        world.get_region(RoomName.FARON_WOODS_CAVE, player),
        f"{RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE} -> {RoomName.FARON_WOODS_CAVE}"
    )

    world.get_region(RoomName.FARON_WOODS_CAVE, player).connect(
        world.get_region(RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE, player),
        f"{RoomName.FARON_WOODS_CAVE} -> {RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE}"
    )

    world.get_region(RoomName.FARON_WOODS_CAVE, player).connect(
        world.get_region(RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE, player),
        f"{RoomName.FARON_WOODS_CAVE} -> {RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE}"
    )

    world.get_region(RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE, player).connect(
        world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player),
        f"{RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE} -> {RoomName.MIST_AREA_INSIDE_MIST}"
    )

    world.get_region(RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE, player).connect(
        world.get_region(RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST, player),
        f"{RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE} -> {RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST}"
    )

    world.get_region(RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE, player).connect(
        world.get_region(RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE, player),
        f"{RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE} -> {RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE}"
    )

    world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player).connect(
        world.get_region(RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE, player),
        f"{RoomName.MIST_AREA_INSIDE_MIST} -> {RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE}"
    )

    world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player).connect(
        world.get_region(RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST, player),
        f"{RoomName.MIST_AREA_INSIDE_MIST} -> {RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST}"
    )

    world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player).connect(
        world.get_region(RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE, player),
        f"{RoomName.MIST_AREA_INSIDE_MIST} -> {RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE}"
    )

    world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player).connect(
        world.get_region(RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS, player),
        f"{RoomName.MIST_AREA_INSIDE_MIST} -> {RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS}"
    )

    world.get_region(RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST, player).connect(
        world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player),
        f"{RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST} -> {RoomName.MIST_AREA_INSIDE_MIST}"
    )

    world.get_region(RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST, player).connect(
        world.get_region(RoomName.MIST_AREA_CENTER_STUMP, player),
        f"{RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST} -> {RoomName.MIST_AREA_CENTER_STUMP}"
    )

    world.get_region(RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST, player).connect(
        world.get_region(RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST, player),
        f"{RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST} -> {RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST}"
    )

    world.get_region(RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE, player),
        f"{RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST} -> {RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE}"
    )

    world.get_region(RoomName.MIST_AREA_CENTER_STUMP, player).connect(
        world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player),
        f"{RoomName.MIST_AREA_CENTER_STUMP} -> {RoomName.MIST_AREA_INSIDE_MIST}"
    )

    world.get_region(RoomName.MIST_AREA_CENTER_STUMP, player).connect(
        world.get_region(RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS, player),
        f"{RoomName.MIST_AREA_CENTER_STUMP} -> {RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS}"
    )

    world.get_region(RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE, player).connect(
        world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player),
        f"{RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE} -> {RoomName.MIST_AREA_INSIDE_MIST}"
    )

    world.get_region(RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE, player).connect(
        world.get_region(RoomName.MIST_AREA_FARON_MIST_CAVE, player),
        f"{RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE} -> {RoomName.MIST_AREA_FARON_MIST_CAVE}"
    )

    world.get_region(RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.MIST_AREA_INSIDE_MIST, player),
        f"{RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS} -> {RoomName.MIST_AREA_INSIDE_MIST}"
    )

    world.get_region(RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE, player),
        f"{RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS} -> {RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE}"
    )

    world.get_region(RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.NORTH_FARON_WOODS, player),
        f"{RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS} -> {RoomName.NORTH_FARON_WOODS}"
    )

    world.get_region(RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE, player).connect(
        world.get_region(RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE, player),
        f"{RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE} -> {RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE}"
    )

    world.get_region(RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE, player).connect(
        world.get_region(RoomName.FARON_WOODS_CAVE, player),
        f"{RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE} -> {RoomName.FARON_WOODS_CAVE}"
    )

    world.get_region(RoomName.MIST_AREA_FARON_MIST_CAVE, player).connect(
        world.get_region(RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE, player),
        f"{RoomName.MIST_AREA_FARON_MIST_CAVE} -> {RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE}"
    )

    world.get_region(RoomName.NORTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS, player),
        f"{RoomName.NORTH_FARON_WOODS} -> {RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS}"
    )

    world.get_region(RoomName.NORTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.LOST_WOODS, player),
        f"{RoomName.NORTH_FARON_WOODS} -> {RoomName.LOST_WOODS}"
    )

    world.get_region(RoomName.NORTH_FARON_WOODS, player).connect(
        world.get_region(RoomName.FOREST_TEMPLE_ENTRANCE, player),
        f"{RoomName.NORTH_FARON_WOODS} -> {RoomName.FOREST_TEMPLE_ENTRANCE}"
    )

    world.get_region(RoomName.FARON_FIELD, player).connect(
        world.get_region(RoomName.FARON_FIELD_BEHIND_BOULDER, player),
        f"{RoomName.FARON_FIELD} -> {RoomName.FARON_FIELD_BEHIND_BOULDER}"
    )

    world.get_region(RoomName.FARON_FIELD, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS, player),
        f"{RoomName.FARON_FIELD} -> {RoomName.SOUTH_FARON_WOODS}"
    )

    world.get_region(RoomName.FARON_FIELD, player).connect(
        world.get_region(RoomName.KAKARIKO_GORGE, player),
        f"{RoomName.FARON_FIELD} -> {RoomName.KAKARIKO_GORGE}"
    )

    world.get_region(RoomName.FARON_FIELD, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player),
        f"{RoomName.FARON_FIELD} -> {RoomName.LAKE_HYLIA_BRIDGE}"
    )

    world.get_region(RoomName.FARON_FIELD, player).connect(
        world.get_region(RoomName.FARON_FIELD_CORNER_GROTTO, player),
        f"{RoomName.FARON_FIELD} -> {RoomName.FARON_FIELD_CORNER_GROTTO}"
    )

    world.get_region(RoomName.FARON_FIELD, player).connect(
        world.get_region(RoomName.FARON_FIELD_FISHING_GROTTO, player),
        f"{RoomName.FARON_FIELD} -> {RoomName.FARON_FIELD_FISHING_GROTTO}"
    )

    world.get_region(RoomName.FARON_FIELD_BEHIND_BOULDER, player).connect(
        world.get_region(RoomName.FARON_FIELD, player),
        f"{RoomName.FARON_FIELD_BEHIND_BOULDER} -> {RoomName.FARON_FIELD}"
    )

    world.get_region(RoomName.FARON_FIELD_BEHIND_BOULDER, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_INSIDE_BOULDER, player),
        f"{RoomName.FARON_FIELD_BEHIND_BOULDER} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_INSIDE_BOULDER}"
    )

    world.get_region(RoomName.FARON_FIELD_CORNER_GROTTO, player).connect(
        world.get_region(RoomName.FARON_FIELD, player),
        f"{RoomName.FARON_FIELD_CORNER_GROTTO} -> {RoomName.FARON_FIELD}"
    )

    world.get_region(RoomName.FARON_FIELD_FISHING_GROTTO, player).connect(
        world.get_region(RoomName.FARON_FIELD, player),
        f"{RoomName.FARON_FIELD_FISHING_GROTTO} -> {RoomName.FARON_FIELD}"
    )

    world.get_region(RoomName.LOST_WOODS, player).connect(
        world.get_region(RoomName.LOST_WOODS_LOWER_BATTLE_ARENA, player),
        f"{RoomName.LOST_WOODS} -> {RoomName.LOST_WOODS_LOWER_BATTLE_ARENA}"
    )

    world.get_region(RoomName.LOST_WOODS, player).connect(
        world.get_region(RoomName.LOST_WOODS_UPPER_BATTLE_ARENA, player),
        f"{RoomName.LOST_WOODS} -> {RoomName.LOST_WOODS_UPPER_BATTLE_ARENA}"
    )

    world.get_region(RoomName.LOST_WOODS, player).connect(
        world.get_region(RoomName.NORTH_FARON_WOODS, player),
        f"{RoomName.LOST_WOODS} -> {RoomName.NORTH_FARON_WOODS}"
    )

    world.get_region(RoomName.LOST_WOODS_LOWER_BATTLE_ARENA, player).connect(
        world.get_region(RoomName.LOST_WOODS, player),
        f"{RoomName.LOST_WOODS_LOWER_BATTLE_ARENA} -> {RoomName.LOST_WOODS}"
    )

    world.get_region(RoomName.LOST_WOODS_LOWER_BATTLE_ARENA, player).connect(
        world.get_region(RoomName.SACRED_GROVE_LOWER, player),
        f"{RoomName.LOST_WOODS_LOWER_BATTLE_ARENA} -> {RoomName.SACRED_GROVE_LOWER}"
    )

    world.get_region(RoomName.LOST_WOODS_LOWER_BATTLE_ARENA, player).connect(
        world.get_region(RoomName.LOST_WOODS_BABA_SERPENT_GROTTO, player),
        f"{RoomName.LOST_WOODS_LOWER_BATTLE_ARENA} -> {RoomName.LOST_WOODS_BABA_SERPENT_GROTTO}"
    )

    world.get_region(RoomName.LOST_WOODS_UPPER_BATTLE_ARENA, player).connect(
        world.get_region(RoomName.SACRED_GROVE_BEFORE_BLOCK, player),
        f"{RoomName.LOST_WOODS_UPPER_BATTLE_ARENA} -> {RoomName.SACRED_GROVE_BEFORE_BLOCK}"
    )

    world.get_region(RoomName.LOST_WOODS_BABA_SERPENT_GROTTO, player).connect(
        world.get_region(RoomName.LOST_WOODS_LOWER_BATTLE_ARENA, player),
        f"{RoomName.LOST_WOODS_BABA_SERPENT_GROTTO} -> {RoomName.LOST_WOODS_LOWER_BATTLE_ARENA}"
    )

    world.get_region(RoomName.SACRED_GROVE_BEFORE_BLOCK, player).connect(
        world.get_region(RoomName.LOST_WOODS_UPPER_BATTLE_ARENA, player),
        f"{RoomName.SACRED_GROVE_BEFORE_BLOCK} -> {RoomName.LOST_WOODS_UPPER_BATTLE_ARENA}"
    )

    world.get_region(RoomName.SACRED_GROVE_BEFORE_BLOCK, player).connect(
        world.get_region(RoomName.SACRED_GROVE_UPPER, player),
        f"{RoomName.SACRED_GROVE_BEFORE_BLOCK} -> {RoomName.SACRED_GROVE_UPPER}"
    )

    world.get_region(RoomName.SACRED_GROVE_UPPER, player).connect(
        world.get_region(RoomName.SACRED_GROVE_LOWER, player),
        f"{RoomName.SACRED_GROVE_UPPER} -> {RoomName.SACRED_GROVE_LOWER}"
    )

    world.get_region(RoomName.SACRED_GROVE_UPPER, player).connect(
        world.get_region(RoomName.SACRED_GROVE_PAST, player),
        f"{RoomName.SACRED_GROVE_UPPER} -> {RoomName.SACRED_GROVE_PAST}"
    )

    world.get_region(RoomName.SACRED_GROVE_LOWER, player).connect(
        world.get_region(RoomName.LOST_WOODS_LOWER_BATTLE_ARENA, player),
        f"{RoomName.SACRED_GROVE_LOWER} -> {RoomName.LOST_WOODS_LOWER_BATTLE_ARENA}"
    )

    world.get_region(RoomName.SACRED_GROVE_LOWER, player).connect(
        world.get_region(RoomName.SACRED_GROVE_UPPER, player),
        f"{RoomName.SACRED_GROVE_LOWER} -> {RoomName.SACRED_GROVE_UPPER}"
    )

    world.get_region(RoomName.SACRED_GROVE_PAST, player).connect(
        world.get_region(RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW, player),
        f"{RoomName.SACRED_GROVE_PAST} -> {RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW}"
    )

    world.get_region(RoomName.SACRED_GROVE_PAST, player).connect(
        world.get_region(RoomName.SACRED_GROVE_UPPER, player),
        f"{RoomName.SACRED_GROVE_PAST} -> {RoomName.SACRED_GROVE_UPPER}"
    )

    world.get_region(RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW, player).connect(
        world.get_region(RoomName.SACRED_GROVE_PAST, player),
        f"{RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW} -> {RoomName.SACRED_GROVE_PAST}"
    )

    world.get_region(RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW, player).connect(
        world.get_region(RoomName.TEMPLE_OF_TIME_ENTRANCE, player),
        f"{RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW} -> {RoomName.TEMPLE_OF_TIME_ENTRANCE}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU, player),
        f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_12_21, player),
        f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_12_21}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_12_21, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_22_31, player),
        f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_12_21} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_22_31}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_22_31, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_32_41, player),
        f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_22_31} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_32_41}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_32_41, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_42_50, player),
        f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_32_41} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_42_50}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_42_50, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_LANAYRU_SPRING, player),
        f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_42_50} -> {RoomName.LAKE_HYLIA_LANAYRU_SPRING}"
    )

    world.get_region(RoomName.GERUDO_DESERT, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU, player),
        f"{RoomName.GERUDO_DESERT} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU}"
    )

    world.get_region(RoomName.GERUDO_DESERT, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_BASIN, player),
        f"{RoomName.GERUDO_DESERT} -> {RoomName.GERUDO_DESERT_BASIN}"
    )

    world.get_region(RoomName.GERUDO_DESERT, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_SKULLTULA_GROTTO, player),
        f"{RoomName.GERUDO_DESERT} -> {RoomName.GERUDO_DESERT_SKULLTULA_GROTTO}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU, player).connect(
        world.get_region(RoomName.GERUDO_DESERT, player),
        f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU} -> {RoomName.GERUDO_DESERT}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11, player),
        f"{RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU} -> {RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11}"
    )

    world.get_region(RoomName.GERUDO_DESERT_BASIN, player).connect(
        world.get_region(RoomName.GERUDO_DESERT, player),
        f"{RoomName.GERUDO_DESERT_BASIN} -> {RoomName.GERUDO_DESERT}"
    )

    world.get_region(RoomName.GERUDO_DESERT_BASIN, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE, player),
        f"{RoomName.GERUDO_DESERT_BASIN} -> {RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE}"
    )

    world.get_region(RoomName.GERUDO_DESERT_BASIN, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP, player),
        f"{RoomName.GERUDO_DESERT_BASIN} -> {RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP}"
    )

    world.get_region(RoomName.GERUDO_DESERT_BASIN, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_CHU_GROTTO, player),
        f"{RoomName.GERUDO_DESERT_BASIN} -> {RoomName.GERUDO_DESERT_CHU_GROTTO}"
    )

    world.get_region(RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_BASIN, player),
        f"{RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE} -> {RoomName.GERUDO_DESERT_BASIN}"
    )

    world.get_region(RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_ROCK_GROTTO, player),
        f"{RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE} -> {RoomName.GERUDO_DESERT_ROCK_GROTTO}"
    )

    world.get_region(RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_BASIN, player),
        f"{RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP} -> {RoomName.GERUDO_DESERT_BASIN}"
    )

    world.get_region(RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP, player).connect(
        world.get_region(RoomName.BULBLIN_CAMP, player),
        f"{RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP} -> {RoomName.BULBLIN_CAMP}"
    )

    world.get_region(RoomName.GERUDO_DESERT_SKULLTULA_GROTTO, player).connect(
        world.get_region(RoomName.GERUDO_DESERT, player),
        f"{RoomName.GERUDO_DESERT_SKULLTULA_GROTTO} -> {RoomName.GERUDO_DESERT}"
    )

    world.get_region(RoomName.GERUDO_DESERT_CHU_GROTTO, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_BASIN, player),
        f"{RoomName.GERUDO_DESERT_CHU_GROTTO} -> {RoomName.GERUDO_DESERT_BASIN}"
    )

    world.get_region(RoomName.GERUDO_DESERT_ROCK_GROTTO, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE, player),
        f"{RoomName.GERUDO_DESERT_ROCK_GROTTO} -> {RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE}"
    )

    world.get_region(RoomName.BULBLIN_CAMP, player).connect(
        world.get_region(RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP, player),
        f"{RoomName.BULBLIN_CAMP} -> {RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP}"
    )

    world.get_region(RoomName.BULBLIN_CAMP, player).connect(
        world.get_region(RoomName.OUTSIDE_ARBITERS_GROUNDS, player),
        f"{RoomName.BULBLIN_CAMP} -> {RoomName.OUTSIDE_ARBITERS_GROUNDS}"
    )

    world.get_region(RoomName.OUTSIDE_ARBITERS_GROUNDS, player).connect(
        world.get_region(RoomName.BULBLIN_CAMP, player),
        f"{RoomName.OUTSIDE_ARBITERS_GROUNDS} -> {RoomName.BULBLIN_CAMP}"
    )

    world.get_region(RoomName.OUTSIDE_ARBITERS_GROUNDS, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_ENTRANCE, player),
        f"{RoomName.OUTSIDE_ARBITERS_GROUNDS} -> {RoomName.ARBITERS_GROUNDS_ENTRANCE}"
    )

    world.get_region(RoomName.MIRROR_CHAMBER_LOWER, player).connect(
        world.get_region(RoomName.ARBITERS_GROUNDS_BOSS_ROOM, player),
        f"{RoomName.MIRROR_CHAMBER_LOWER} -> {RoomName.ARBITERS_GROUNDS_BOSS_ROOM}"
    )

    world.get_region(RoomName.MIRROR_CHAMBER_LOWER, player).connect(
        world.get_region(RoomName.MIRROR_CHAMBER_UPPER, player),
        f"{RoomName.MIRROR_CHAMBER_LOWER} -> {RoomName.MIRROR_CHAMBER_UPPER}"
    )

    world.get_region(RoomName.MIRROR_CHAMBER_UPPER, player).connect(
        world.get_region(RoomName.MIRROR_CHAMBER_LOWER, player),
        f"{RoomName.MIRROR_CHAMBER_UPPER} -> {RoomName.MIRROR_CHAMBER_LOWER}"
    )

    world.get_region(RoomName.MIRROR_CHAMBER_UPPER, player).connect(
        world.get_region(RoomName.MIRROR_CHAMBER_PORTAL, player),
        f"{RoomName.MIRROR_CHAMBER_UPPER} -> {RoomName.MIRROR_CHAMBER_PORTAL}"
    )

    world.get_region(RoomName.MIRROR_CHAMBER_PORTAL, player).connect(
        world.get_region(RoomName.MIRROR_CHAMBER_UPPER, player),
        f"{RoomName.MIRROR_CHAMBER_PORTAL} -> {RoomName.MIRROR_CHAMBER_UPPER}"
    )

    world.get_region(RoomName.MIRROR_CHAMBER_PORTAL, player).connect(
        world.get_region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player),
        f"{RoomName.MIRROR_CHAMBER_PORTAL} -> {RoomName.PALACE_OF_TWILIGHT_ENTRANCE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_WEST, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player),
        f"{RoomName.CASTLE_TOWN_WEST} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_WEST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_CENTER, player),
        f"{RoomName.CASTLE_TOWN_WEST} -> {RoomName.CASTLE_TOWN_CENTER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_WEST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SOUTH, player),
        f"{RoomName.CASTLE_TOWN_WEST} -> {RoomName.CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_WEST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_STAR_GAME, player),
        f"{RoomName.CASTLE_TOWN_WEST} -> {RoomName.CASTLE_TOWN_STAR_GAME}"
    )

    world.get_region(RoomName.CASTLE_TOWN_STAR_GAME, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_WEST, player),
        f"{RoomName.CASTLE_TOWN_STAR_GAME} -> {RoomName.CASTLE_TOWN_WEST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_CENTER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_WEST, player),
        f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_WEST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_CENTER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_NORTH, player),
        f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_NORTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_CENTER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_EAST, player),
        f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_EAST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_CENTER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SOUTH, player),
        f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_CENTER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR, player),
        f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_CENTER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR, player),
        f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_CENTER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_MALO_MART, player),
        f"{RoomName.CASTLE_TOWN_CENTER} -> {RoomName.CASTLE_TOWN_MALO_MART}"
    )

    world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_CENTER, player),
        f"{RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR} -> {RoomName.CASTLE_TOWN_CENTER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE, player),
        f"{RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR} -> {RoomName.CASTLE_TOWN_GORON_HOUSE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_CENTER, player),
        f"{RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR} -> {RoomName.CASTLE_TOWN_CENTER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE, player),
        f"{RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR} -> {RoomName.CASTLE_TOWN_GORON_HOUSE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR, player),
        f"{RoomName.CASTLE_TOWN_GORON_HOUSE} -> {RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR, player),
        f"{RoomName.CASTLE_TOWN_GORON_HOUSE} -> {RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_MALO_MART, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_CENTER, player),
        f"{RoomName.CASTLE_TOWN_MALO_MART} -> {RoomName.CASTLE_TOWN_CENTER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_NORTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR, player),
        f"{RoomName.CASTLE_TOWN_NORTH} -> {RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_NORTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_CENTER, player),
        f"{RoomName.CASTLE_TOWN_NORTH} -> {RoomName.CASTLE_TOWN_CENTER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_NORTH, player),
        f"{RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR} -> {RoomName.CASTLE_TOWN_NORTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER, player),
        f"{RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR} -> {RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR, player),
        f"{RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER} -> {RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER, player).connect(
        world.get_region(RoomName.HYRULE_CASTLE_ENTRANCE, player),
        f"{RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER} -> {RoomName.HYRULE_CASTLE_ENTRANCE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_EAST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_CENTER, player),
        f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_CENTER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_EAST, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_EAST, player),
        f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.OUTSIDE_CASTLE_TOWN_EAST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_EAST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SOUTH, player),
        f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_EAST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR, player),
        f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_EAST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR, player),
        f"{RoomName.CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_EAST, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY} -> {RoomName.CASTLE_TOWN_EAST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_EAST, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR} -> {RoomName.CASTLE_TOWN_EAST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_EAST, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR} -> {RoomName.CASTLE_TOWN_EAST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY, player),
        f"{RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER} -> {RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_WEST, player),
        f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_WEST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_CENTER, player),
        f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_CENTER}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_EAST, player),
        f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_EAST}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH, player),
        f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_AGITHAS_HOUSE, player),
        f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_AGITHAS_HOUSE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SEER_HOUSE, player),
        f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_SEER_HOUSE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_JOVANIS_HOUSE, player),
        f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_JOVANIS_HOUSE}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_TELMAS_BAR, player),
        f"{RoomName.CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_TELMAS_BAR}"
    )

    world.get_region(RoomName.CASTLE_TOWN_AGITHAS_HOUSE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SOUTH, player),
        f"{RoomName.CASTLE_TOWN_AGITHAS_HOUSE} -> {RoomName.CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_SEER_HOUSE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SOUTH, player),
        f"{RoomName.CASTLE_TOWN_SEER_HOUSE} -> {RoomName.CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_JOVANIS_HOUSE, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SOUTH, player),
        f"{RoomName.CASTLE_TOWN_JOVANIS_HOUSE} -> {RoomName.CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.CASTLE_TOWN_TELMAS_BAR, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SOUTH, player),
        f"{RoomName.CASTLE_TOWN_TELMAS_BAR} -> {RoomName.CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.LANAYRU_FIELD, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD_CAVE_ENTRANCE, player),
        f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_CAVE_ENTRANCE}"
    )

    world.get_region(RoomName.LANAYRU_FIELD, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD_BEHIND_BOULDER, player),
        f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_BEHIND_BOULDER}"
    )

    world.get_region(RoomName.LANAYRU_FIELD, player).connect(
        world.get_region(RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS, player),
        f"{RoomName.LANAYRU_FIELD} -> {RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS}"
    )

    world.get_region(RoomName.LANAYRU_FIELD, player).connect(
        world.get_region(RoomName.NORTH_ELDIN_FIELD, player),
        f"{RoomName.LANAYRU_FIELD} -> {RoomName.NORTH_ELDIN_FIELD}"
    )

    world.get_region(RoomName.LANAYRU_FIELD, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player),
        f"{RoomName.LANAYRU_FIELD} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST}"
    )

    world.get_region(RoomName.LANAYRU_FIELD, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD_CHU_GROTTO, player),
        f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_CHU_GROTTO}"
    )

    world.get_region(RoomName.LANAYRU_FIELD, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD_SKULLTULA_GROTTO, player),
        f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_SKULLTULA_GROTTO}"
    )

    world.get_region(RoomName.LANAYRU_FIELD, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD_POE_GROTTO, player),
        f"{RoomName.LANAYRU_FIELD} -> {RoomName.LANAYRU_FIELD_POE_GROTTO}"
    )

    world.get_region(RoomName.LANAYRU_FIELD_CAVE_ENTRANCE, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.LANAYRU_FIELD_CAVE_ENTRANCE} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.LANAYRU_FIELD_CAVE_ENTRANCE, player).connect(
        world.get_region(RoomName.LANAYRU_ICE_PUZZLE_CAVE, player),
        f"{RoomName.LANAYRU_FIELD_CAVE_ENTRANCE} -> {RoomName.LANAYRU_ICE_PUZZLE_CAVE}"
    )

    world.get_region(RoomName.LANAYRU_FIELD_BEHIND_BOULDER, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.LANAYRU_FIELD_BEHIND_BOULDER} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.LANAYRU_FIELD_BEHIND_BOULDER, player).connect(
        world.get_region(RoomName.ZORAS_DOMAIN_WEST_LEDGE, player),
        f"{RoomName.LANAYRU_FIELD_BEHIND_BOULDER} -> {RoomName.ZORAS_DOMAIN_WEST_LEDGE}"
    )

    world.get_region(RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player),
        f"{RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS} -> {RoomName.LAKE_HYLIA_BRIDGE}"
    )

    world.get_region(RoomName.LANAYRU_ICE_PUZZLE_CAVE, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD_CAVE_ENTRANCE, player),
        f"{RoomName.LANAYRU_ICE_PUZZLE_CAVE} -> {RoomName.LANAYRU_FIELD_CAVE_ENTRANCE}"
    )

    world.get_region(RoomName.LANAYRU_FIELD_CHU_GROTTO, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.LANAYRU_FIELD_CHU_GROTTO} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.LANAYRU_FIELD_SKULLTULA_GROTTO, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.LANAYRU_FIELD_SKULLTULA_GROTTO} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.LANAYRU_FIELD_POE_GROTTO, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.LANAYRU_FIELD_POE_GROTTO} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_WEST, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST} -> {RoomName.CASTLE_TOWN_WEST}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST} -> {RoomName.LAKE_HYLIA_BRIDGE}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_HELMASAUR_GROTTO, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST_HELMASAUR_GROTTO}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_HELMASAUR_GROTTO, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_WEST_HELMASAUR_GROTTO} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_EAST, player).connect(
        world.get_region(RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_EAST} -> {RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_EAST, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_EAST, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_EAST} -> {RoomName.CASTLE_TOWN_EAST}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.CASTLE_TOWN_SOUTH, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH} -> {RoomName.CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.FARON_FIELD_BEHIND_BOULDER, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH} -> {RoomName.FARON_FIELD_BEHIND_BOULDER}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_TEKTITE_GROTTO, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_TEKTITE_GROTTO}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_INSIDE_BOULDER, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_INSIDE_BOULDER} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_TEKTITE_GROTTO, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH, player),
        f"{RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_TEKTITE_GROTTO} -> {RoomName.OUTSIDE_CASTLE_TOWN_SOUTH}"
    )

    world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE, player),
        f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE}"
    )

    world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player).connect(
        world.get_region(RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS, player),
        f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS}"
    )

    world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player).connect(
        world.get_region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player),
        f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.OUTSIDE_CASTLE_TOWN_WEST}"
    )

    world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player).connect(
        world.get_region(RoomName.FARON_FIELD, player),
        f"{RoomName.LAKE_HYLIA_BRIDGE} -> {RoomName.FARON_FIELD}"
    )

    world.get_region(RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player),
        f"{RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE} -> {RoomName.LAKE_HYLIA_BRIDGE}"
    )

    world.get_region(RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO, player),
        f"{RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE} -> {RoomName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO}"
    )

    world.get_region(RoomName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE, player),
        f"{RoomName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO} -> {RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_CAVE_ENTRANCE, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_CAVE_ENTRANCE}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_BRIDGE, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_BRIDGE}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.GERUDO_DESERT, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.GERUDO_DESERT}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.UPPER_ZORAS_RIVER, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.UPPER_ZORAS_RIVER}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_LANAYRU_SPRING, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_LANAYRU_SPRING}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_SHELL_BLADE_GROTTO, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_SHELL_BLADE_GROTTO}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO}"
    )

    world.get_region(RoomName.LAKE_HYLIA, player).connect(
        world.get_region(RoomName.CITY_IN_THE_SKY_ENTRANCE, player),
        f"{RoomName.LAKE_HYLIA} -> {RoomName.CITY_IN_THE_SKY_ENTRANCE}"
    )

    world.get_region(RoomName.LAKE_HYLIA_CAVE_ENTRANCE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.LAKE_HYLIA_CAVE_ENTRANCE} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.LAKE_HYLIA_CAVE_ENTRANCE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_LONG_CAVE, player),
        f"{RoomName.LAKE_HYLIA_CAVE_ENTRANCE} -> {RoomName.LAKE_HYLIA_LONG_CAVE}"
    )

    world.get_region(RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE, player).connect(
        world.get_region(RoomName.LAKEBED_TEMPLE_ENTRANCE, player),
        f"{RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE} -> {RoomName.LAKEBED_TEMPLE_ENTRANCE}"
    )

    world.get_region(RoomName.LAKE_HYLIA_LANAYRU_SPRING, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.LAKE_HYLIA_LANAYRU_SPRING} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.LAKE_HYLIA_LONG_CAVE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA_CAVE_ENTRANCE, player),
        f"{RoomName.LAKE_HYLIA_LONG_CAVE} -> {RoomName.LAKE_HYLIA_CAVE_ENTRANCE}"
    )

    world.get_region(RoomName.LAKE_HYLIA_SHELL_BLADE_GROTTO, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.LAKE_HYLIA_SHELL_BLADE_GROTTO} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.UPPER_ZORAS_RIVER, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD, player),
        f"{RoomName.UPPER_ZORAS_RIVER} -> {RoomName.LANAYRU_FIELD}"
    )

    world.get_region(RoomName.UPPER_ZORAS_RIVER, player).connect(
        world.get_region(RoomName.FISHING_HOLE, player),
        f"{RoomName.UPPER_ZORAS_RIVER} -> {RoomName.FISHING_HOLE}"
    )

    world.get_region(RoomName.UPPER_ZORAS_RIVER, player).connect(
        world.get_region(RoomName.ZORAS_DOMAIN, player),
        f"{RoomName.UPPER_ZORAS_RIVER} -> {RoomName.ZORAS_DOMAIN}"
    )

    world.get_region(RoomName.UPPER_ZORAS_RIVER, player).connect(
        world.get_region(RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE, player),
        f"{RoomName.UPPER_ZORAS_RIVER} -> {RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE}"
    )

    world.get_region(RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE, player).connect(
        world.get_region(RoomName.UPPER_ZORAS_RIVER, player),
        f"{RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE} -> {RoomName.UPPER_ZORAS_RIVER}"
    )

    world.get_region(RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE, player).connect(
        world.get_region(RoomName.LAKE_HYLIA, player),
        f"{RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE} -> {RoomName.LAKE_HYLIA}"
    )

    world.get_region(RoomName.FISHING_HOLE, player).connect(
        world.get_region(RoomName.UPPER_ZORAS_RIVER, player),
        f"{RoomName.FISHING_HOLE} -> {RoomName.UPPER_ZORAS_RIVER}"
    )

    world.get_region(RoomName.FISHING_HOLE, player).connect(
        world.get_region(RoomName.FISHING_HOLE_HOUSE, player),
        f"{RoomName.FISHING_HOLE} -> {RoomName.FISHING_HOLE_HOUSE}"
    )

    world.get_region(RoomName.FISHING_HOLE_HOUSE, player).connect(
        world.get_region(RoomName.FISHING_HOLE, player),
        f"{RoomName.FISHING_HOLE_HOUSE} -> {RoomName.FISHING_HOLE}"
    )

    world.get_region(RoomName.ZORAS_DOMAIN, player).connect(
        world.get_region(RoomName.ZORAS_DOMAIN_WEST_LEDGE, player),
        f"{RoomName.ZORAS_DOMAIN} -> {RoomName.ZORAS_DOMAIN_WEST_LEDGE}"
    )

    world.get_region(RoomName.ZORAS_DOMAIN, player).connect(
        world.get_region(RoomName.UPPER_ZORAS_RIVER, player),
        f"{RoomName.ZORAS_DOMAIN} -> {RoomName.UPPER_ZORAS_RIVER}"
    )

    world.get_region(RoomName.ZORAS_DOMAIN, player).connect(
        world.get_region(RoomName.ZORAS_THRONE_ROOM, player),
        f"{RoomName.ZORAS_DOMAIN} -> {RoomName.ZORAS_THRONE_ROOM}"
    )

    world.get_region(RoomName.ZORAS_DOMAIN, player).connect(
        world.get_region(RoomName.SNOWPEAK_CLIMB_LOWER, player),
        f"{RoomName.ZORAS_DOMAIN} -> {RoomName.SNOWPEAK_CLIMB_LOWER}"
    )

    world.get_region(RoomName.ZORAS_DOMAIN_WEST_LEDGE, player).connect(
        world.get_region(RoomName.ZORAS_DOMAIN, player),
        f"{RoomName.ZORAS_DOMAIN_WEST_LEDGE} -> {RoomName.ZORAS_DOMAIN}"
    )

    world.get_region(RoomName.ZORAS_DOMAIN_WEST_LEDGE, player).connect(
        world.get_region(RoomName.LANAYRU_FIELD_BEHIND_BOULDER, player),
        f"{RoomName.ZORAS_DOMAIN_WEST_LEDGE} -> {RoomName.LANAYRU_FIELD_BEHIND_BOULDER}"
    )

    world.get_region(RoomName.ZORAS_THRONE_ROOM, player).connect(
        world.get_region(RoomName.ZORAS_DOMAIN, player),
        f"{RoomName.ZORAS_THRONE_ROOM} -> {RoomName.ZORAS_DOMAIN}"
    )

    world.get_region(RoomName.OUTSIDE_LINKS_HOUSE, player).connect(
        world.get_region(RoomName.ORDON_VILLAGE, player),
        f"{RoomName.OUTSIDE_LINKS_HOUSE} -> {RoomName.ORDON_VILLAGE}"
    )

    world.get_region(RoomName.OUTSIDE_LINKS_HOUSE, player).connect(
        world.get_region(RoomName.ORDON_SPRING, player),
        f"{RoomName.OUTSIDE_LINKS_HOUSE} -> {RoomName.ORDON_SPRING}"
    )

    world.get_region(RoomName.OUTSIDE_LINKS_HOUSE, player).connect(
        world.get_region(RoomName.ORDON_LINKS_HOUSE, player),
        f"{RoomName.OUTSIDE_LINKS_HOUSE} -> {RoomName.ORDON_LINKS_HOUSE}"
    )

    world.get_region(RoomName.ORDON_LINKS_HOUSE, player).connect(
        world.get_region(RoomName.OUTSIDE_LINKS_HOUSE, player),
        f"{RoomName.ORDON_LINKS_HOUSE} -> {RoomName.OUTSIDE_LINKS_HOUSE}"
    )

    world.get_region(RoomName.ORDON_VILLAGE, player).connect(
        world.get_region(RoomName.OUTSIDE_LINKS_HOUSE, player),
        f"{RoomName.ORDON_VILLAGE} -> {RoomName.OUTSIDE_LINKS_HOUSE}"
    )

    world.get_region(RoomName.ORDON_VILLAGE, player).connect(
        world.get_region(RoomName.ORDON_RANCH_ENTRANCE, player),
        f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_RANCH_ENTRANCE}"
    )

    world.get_region(RoomName.ORDON_VILLAGE, player).connect(
        world.get_region(RoomName.ORDON_SERAS_SHOP, player),
        f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_SERAS_SHOP}"
    )

    world.get_region(RoomName.ORDON_VILLAGE, player).connect(
        world.get_region(RoomName.ORDON_SHIELD_HOUSE, player),
        f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_SHIELD_HOUSE}"
    )

    world.get_region(RoomName.ORDON_VILLAGE, player).connect(
        world.get_region(RoomName.ORDON_SWORD_HOUSE, player),
        f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_SWORD_HOUSE}"
    )

    world.get_region(RoomName.ORDON_VILLAGE, player).connect(
        world.get_region(RoomName.ORDON_BOS_HOUSE_LEFT_DOOR, player),
        f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_BOS_HOUSE_LEFT_DOOR}"
    )

    world.get_region(RoomName.ORDON_VILLAGE, player).connect(
        world.get_region(RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR, player),
        f"{RoomName.ORDON_VILLAGE} -> {RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR}"
    )

    world.get_region(RoomName.ORDON_SERAS_SHOP, player).connect(
        world.get_region(RoomName.ORDON_VILLAGE, player),
        f"{RoomName.ORDON_SERAS_SHOP} -> {RoomName.ORDON_VILLAGE}"
    )

    world.get_region(RoomName.ORDON_SHIELD_HOUSE, player).connect(
        world.get_region(RoomName.ORDON_VILLAGE, player),
        f"{RoomName.ORDON_SHIELD_HOUSE} -> {RoomName.ORDON_VILLAGE}"
    )

    world.get_region(RoomName.ORDON_SWORD_HOUSE, player).connect(
        world.get_region(RoomName.ORDON_VILLAGE, player),
        f"{RoomName.ORDON_SWORD_HOUSE} -> {RoomName.ORDON_VILLAGE}"
    )

    world.get_region(RoomName.ORDON_BOS_HOUSE_LEFT_DOOR, player).connect(
        world.get_region(RoomName.ORDON_VILLAGE, player),
        f"{RoomName.ORDON_BOS_HOUSE_LEFT_DOOR} -> {RoomName.ORDON_VILLAGE}"
    )

    world.get_region(RoomName.ORDON_BOS_HOUSE_LEFT_DOOR, player).connect(
        world.get_region(RoomName.ORDON_BOS_HOUSE, player),
        f"{RoomName.ORDON_BOS_HOUSE_LEFT_DOOR} -> {RoomName.ORDON_BOS_HOUSE}"
    )

    world.get_region(RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.ORDON_VILLAGE, player),
        f"{RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR} -> {RoomName.ORDON_VILLAGE}"
    )

    world.get_region(RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR, player).connect(
        world.get_region(RoomName.ORDON_BOS_HOUSE, player),
        f"{RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR} -> {RoomName.ORDON_BOS_HOUSE}"
    )

    world.get_region(RoomName.ORDON_BOS_HOUSE, player).connect(
        world.get_region(RoomName.ORDON_BOS_HOUSE_LEFT_DOOR, player),
        f"{RoomName.ORDON_BOS_HOUSE} -> {RoomName.ORDON_BOS_HOUSE_LEFT_DOOR}"
    )

    world.get_region(RoomName.ORDON_BOS_HOUSE, player).connect(
        world.get_region(RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR, player),
        f"{RoomName.ORDON_BOS_HOUSE} -> {RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR}"
    )

    world.get_region(RoomName.ORDON_RANCH_ENTRANCE, player).connect(
        world.get_region(RoomName.ORDON_RANCH, player),
        f"{RoomName.ORDON_RANCH_ENTRANCE} -> {RoomName.ORDON_RANCH}"
    )

    world.get_region(RoomName.ORDON_RANCH_ENTRANCE, player).connect(
        world.get_region(RoomName.ORDON_VILLAGE, player),
        f"{RoomName.ORDON_RANCH_ENTRANCE} -> {RoomName.ORDON_VILLAGE}"
    )

    world.get_region(RoomName.ORDON_RANCH, player).connect(
        world.get_region(RoomName.ORDON_RANCH_ENTRANCE, player),
        f"{RoomName.ORDON_RANCH} -> {RoomName.ORDON_RANCH_ENTRANCE}"
    )

    world.get_region(RoomName.ORDON_RANCH, player).connect(
        world.get_region(RoomName.ORDON_RANCH_STABLE, player),
        f"{RoomName.ORDON_RANCH} -> {RoomName.ORDON_RANCH_STABLE}"
    )

    world.get_region(RoomName.ORDON_RANCH_STABLE, player).connect(
        world.get_region(RoomName.ORDON_RANCH, player),
        f"{RoomName.ORDON_RANCH_STABLE} -> {RoomName.ORDON_RANCH}"
    )

    world.get_region(RoomName.ORDON_RANCH_STABLE, player).connect(
        world.get_region(RoomName.ORDON_RANCH_GROTTO, player),
        f"{RoomName.ORDON_RANCH_STABLE} -> {RoomName.ORDON_RANCH_GROTTO}"
    )

    world.get_region(RoomName.ORDON_RANCH_GROTTO, player).connect(
        world.get_region(RoomName.ORDON_RANCH_STABLE, player),
        f"{RoomName.ORDON_RANCH_GROTTO} -> {RoomName.ORDON_RANCH_STABLE}"
    )

    world.get_region(RoomName.ORDON_SPRING, player).connect(
        world.get_region(RoomName.OUTSIDE_LINKS_HOUSE, player),
        f"{RoomName.ORDON_SPRING} -> {RoomName.OUTSIDE_LINKS_HOUSE}"
    )

    world.get_region(RoomName.ORDON_SPRING, player).connect(
        world.get_region(RoomName.ORDON_BRIDGE, player),
        f"{RoomName.ORDON_SPRING} -> {RoomName.ORDON_BRIDGE}"
    )

    world.get_region(RoomName.ORDON_BRIDGE, player).connect(
        world.get_region(RoomName.ORDON_SPRING, player),
        f"{RoomName.ORDON_BRIDGE} -> {RoomName.ORDON_SPRING}"
    )

    world.get_region(RoomName.ORDON_BRIDGE, player).connect(
        world.get_region(RoomName.SOUTH_FARON_WOODS, player),
        f"{RoomName.ORDON_BRIDGE} -> {RoomName.SOUTH_FARON_WOODS}"
    )

    world.get_region(RoomName.SNOWPEAK_CLIMB_LOWER, player).connect(
        world.get_region(RoomName.SNOWPEAK_CLIMB_UPPER, player),
        f"{RoomName.SNOWPEAK_CLIMB_LOWER} -> {RoomName.SNOWPEAK_CLIMB_UPPER}"
    )

    world.get_region(RoomName.SNOWPEAK_CLIMB_LOWER, player).connect(
        world.get_region(RoomName.ZORAS_DOMAIN, player),
        f"{RoomName.SNOWPEAK_CLIMB_LOWER} -> {RoomName.ZORAS_DOMAIN}"
    )

    world.get_region(RoomName.SNOWPEAK_CLIMB_UPPER, player).connect(
        world.get_region(RoomName.SNOWPEAK_CLIMB_LOWER, player),
        f"{RoomName.SNOWPEAK_CLIMB_UPPER} -> {RoomName.SNOWPEAK_CLIMB_LOWER}"
    )

    world.get_region(RoomName.SNOWPEAK_CLIMB_UPPER, player).connect(
        world.get_region(RoomName.SNOWPEAK_SUMMIT_UPPER, player),
        f"{RoomName.SNOWPEAK_CLIMB_UPPER} -> {RoomName.SNOWPEAK_SUMMIT_UPPER}"
    )

    world.get_region(RoomName.SNOWPEAK_CLIMB_UPPER, player).connect(
        world.get_region(RoomName.SNOWPEAK_ICE_KEESE_GROTTO, player),
        f"{RoomName.SNOWPEAK_CLIMB_UPPER} -> {RoomName.SNOWPEAK_ICE_KEESE_GROTTO}"
    )

    world.get_region(RoomName.SNOWPEAK_CLIMB_UPPER, player).connect(
        world.get_region(RoomName.SNOWPEAK_FREEZARD_GROTTO, player),
        f"{RoomName.SNOWPEAK_CLIMB_UPPER} -> {RoomName.SNOWPEAK_FREEZARD_GROTTO}"
    )

    world.get_region(RoomName.SNOWPEAK_ICE_KEESE_GROTTO, player).connect(
        world.get_region(RoomName.SNOWPEAK_CLIMB_UPPER, player),
        f"{RoomName.SNOWPEAK_ICE_KEESE_GROTTO} -> {RoomName.SNOWPEAK_CLIMB_UPPER}"
    )

    world.get_region(RoomName.SNOWPEAK_FREEZARD_GROTTO, player).connect(
        world.get_region(RoomName.SNOWPEAK_CLIMB_UPPER, player),
        f"{RoomName.SNOWPEAK_FREEZARD_GROTTO} -> {RoomName.SNOWPEAK_CLIMB_UPPER}"
    )

    world.get_region(RoomName.SNOWPEAK_SUMMIT_UPPER, player).connect(
        world.get_region(RoomName.SNOWPEAK_SUMMIT_LOWER, player),
        f"{RoomName.SNOWPEAK_SUMMIT_UPPER} -> {RoomName.SNOWPEAK_SUMMIT_LOWER}"
    )

    world.get_region(RoomName.SNOWPEAK_SUMMIT_UPPER, player).connect(
        world.get_region(RoomName.SNOWPEAK_CLIMB_UPPER, player),
        f"{RoomName.SNOWPEAK_SUMMIT_UPPER} -> {RoomName.SNOWPEAK_CLIMB_UPPER}"
    )

    world.get_region(RoomName.SNOWPEAK_SUMMIT_LOWER, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_LEFT_DOOR, player),
        f"{RoomName.SNOWPEAK_SUMMIT_LOWER} -> {RoomName.SNOWPEAK_RUINS_LEFT_DOOR}"
    )

    world.get_region(RoomName.SNOWPEAK_SUMMIT_LOWER, player).connect(
        world.get_region(RoomName.SNOWPEAK_RUINS_RIGHT_DOOR, player),
        f"{RoomName.SNOWPEAK_SUMMIT_LOWER} -> {RoomName.SNOWPEAK_RUINS_RIGHT_DOOR}"
    )
