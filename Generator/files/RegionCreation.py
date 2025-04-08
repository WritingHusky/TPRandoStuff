from typing import Dict
from BaseClasses import MultiWorld, Region
from .Locations import TPLocation, LOCATION_TABLE
from .Enums import RoomName, CheckName


def create_regions(world: MultiWorld, player: int) -> Dict[str, Region]:
    regions = {}

    # Create Menu region
    menu = Region("Menu", player, world)
    regions["Menu"] = menu
    world.regions.append(menu)

    arbiters_grounds_entrance = Region(RoomName.ARBITERS_GROUNDS_ENTRANCE, player, world)
    regions[RoomName.ARBITERS_GROUNDS_ENTRANCE] = arbiters_grounds_entrance
    world.regions.append(arbiters_grounds_entrance)

    arbiters_grounds_entrance.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_ENTRANCE_CHEST,
        arbiters_grounds_entrance,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_ENTRANCE_CHEST]
      )
    )

    arbiters_grounds_lobby = Region(RoomName.ARBITERS_GROUNDS_LOBBY, player, world)
    regions[RoomName.ARBITERS_GROUNDS_LOBBY] = arbiters_grounds_lobby
    world.regions.append(arbiters_grounds_lobby)

    arbiters_grounds_lobby.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_TORCH_ROOM_EAST_CHEST,
        arbiters_grounds_lobby,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_TORCH_ROOM_EAST_CHEST]
      )
    )

    arbiters_grounds_lobby.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_TORCH_ROOM_WEST_CHEST,
        arbiters_grounds_lobby,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_TORCH_ROOM_WEST_CHEST]
      )
    )

    arbiters_grounds_lobby.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_TORCH_ROOM_POE,
        arbiters_grounds_lobby,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_TORCH_ROOM_POE]
      )
    )

    arbiters_grounds_east_wing = Region(RoomName.ARBITERS_GROUNDS_EAST_WING, player, world)
    regions[RoomName.ARBITERS_GROUNDS_EAST_WING] = arbiters_grounds_east_wing
    world.regions.append(arbiters_grounds_east_wing)

    arbiters_grounds_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_EAST_LOWER_TURNABLE_REDEAD_CHEST,
        arbiters_grounds_east_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_EAST_LOWER_TURNABLE_REDEAD_CHEST]
      )
    )

    arbiters_grounds_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_EAST_UPPER_TURNABLE_CHEST,
        arbiters_grounds_east_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_EAST_UPPER_TURNABLE_CHEST]
      )
    )

    arbiters_grounds_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_EAST_UPPER_TURNABLE_REDEAD_CHEST,
        arbiters_grounds_east_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_EAST_UPPER_TURNABLE_REDEAD_CHEST]
      )
    )

    arbiters_grounds_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_GHOUL_RAT_ROOM_CHEST,
        arbiters_grounds_east_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_GHOUL_RAT_ROOM_CHEST]
      )
    )

    arbiters_grounds_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_EAST_TURNING_ROOM_POE,
        arbiters_grounds_east_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_EAST_TURNING_ROOM_POE]
      )
    )

    arbiters_grounds_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_HIDDEN_WALL_POE,
        arbiters_grounds_east_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_HIDDEN_WALL_POE]
      )
    )

    arbiters_grounds_west_wing = Region(RoomName.ARBITERS_GROUNDS_WEST_WING, player, world)
    regions[RoomName.ARBITERS_GROUNDS_WEST_WING] = arbiters_grounds_west_wing
    world.regions.append(arbiters_grounds_west_wing)

    arbiters_grounds_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_WEST_SMALL_CHEST_BEHIND_BLOCK,
        arbiters_grounds_west_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_WEST_SMALL_CHEST_BEHIND_BLOCK]
      )
    )

    arbiters_grounds_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_WEST_CHANDELIER_CHEST,
        arbiters_grounds_west_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_WEST_CHANDELIER_CHEST]
      )
    )

    arbiters_grounds_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_WEST_STALFOS_WEST_CHEST,
        arbiters_grounds_west_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_WEST_STALFOS_WEST_CHEST]
      )
    )

    arbiters_grounds_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_WEST_STALFOS_NORTHEAST_CHEST,
        arbiters_grounds_west_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_WEST_STALFOS_NORTHEAST_CHEST]
      )
    )

    arbiters_grounds_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_WEST_POE,
        arbiters_grounds_west_wing,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_WEST_POE]
      )
    )

    arbiters_grounds_after_poe_gate = Region(RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE, player, world)
    regions[RoomName.ARBITERS_GROUNDS_AFTER_POE_GATE] = arbiters_grounds_after_poe_gate
    world.regions.append(arbiters_grounds_after_poe_gate)

    arbiters_grounds_after_poe_gate.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_BIG_KEY_CHEST,
        arbiters_grounds_after_poe_gate,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_BIG_KEY_CHEST]
      )
    )

    arbiters_grounds_after_poe_gate.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_NORTH_TURNING_ROOM_CHEST,
        arbiters_grounds_after_poe_gate,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_NORTH_TURNING_ROOM_CHEST]
      )
    )

    arbiters_grounds_after_poe_gate.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_DEATH_SWORD_CHEST,
        arbiters_grounds_after_poe_gate,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_DEATH_SWORD_CHEST]
      )
    )

    arbiters_grounds_after_poe_gate.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_FIRST_SMALL_CHEST,
        arbiters_grounds_after_poe_gate,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_FIRST_SMALL_CHEST]
      )
    )

    arbiters_grounds_after_poe_gate.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_SECOND_SMALL_CHEST,
        arbiters_grounds_after_poe_gate,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_SECOND_SMALL_CHEST]
      )
    )

    arbiters_grounds_after_poe_gate.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_LOWER_CENTRAL_SMALL_CHEST,
        arbiters_grounds_after_poe_gate,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_LOWER_CENTRAL_SMALL_CHEST]
      )
    )

    arbiters_grounds_after_poe_gate.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_STALFOS_ALCOVE_CHEST,
        arbiters_grounds_after_poe_gate,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_STALFOS_ALCOVE_CHEST]
      )
    )

    arbiters_grounds_after_poe_gate.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_LOWER_NORTH_CHEST,
        arbiters_grounds_after_poe_gate,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_SPINNER_ROOM_LOWER_NORTH_CHEST]
      )
    )

    arbiters_grounds_boss_room = Region(RoomName.ARBITERS_GROUNDS_BOSS_ROOM, player, world)
    regions[RoomName.ARBITERS_GROUNDS_BOSS_ROOM] = arbiters_grounds_boss_room
    world.regions.append(arbiters_grounds_boss_room)

    arbiters_grounds_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_STALLORD_HEART_CONTAINER,
        arbiters_grounds_boss_room,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_STALLORD_HEART_CONTAINER]
      )
    )

    arbiters_grounds_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.ARBITERS_GROUNDS_DUNGEON_REWARD,
        arbiters_grounds_boss_room,
        LOCATION_TABLE[CheckName.ARBITERS_GROUNDS_DUNGEON_REWARD]
      )
    )

    city_in_the_sky_boss_room = Region(RoomName.CITY_IN_THE_SKY_BOSS_ROOM, player, world)
    regions[RoomName.CITY_IN_THE_SKY_BOSS_ROOM] = city_in_the_sky_boss_room
    world.regions.append(city_in_the_sky_boss_room)

    city_in_the_sky_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_ARGOROK_HEART_CONTAINER,
        city_in_the_sky_boss_room,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_ARGOROK_HEART_CONTAINER]
      )
    )

    city_in_the_sky_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_DUNGEON_REWARD,
        city_in_the_sky_boss_room,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_DUNGEON_REWARD]
      )
    )

    city_in_the_sky_central_tower_second_floor = Region(RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR, player, world)
    regions[RoomName.CITY_IN_THE_SKY_CENTRAL_TOWER_SECOND_FLOOR] = city_in_the_sky_central_tower_second_floor
    world.regions.append(city_in_the_sky_central_tower_second_floor)

    city_in_the_sky_central_tower_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_CENTRAL_OUTSIDE_LEDGE_CHEST,
        city_in_the_sky_central_tower_second_floor,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_CENTRAL_OUTSIDE_LEDGE_CHEST]
      )
    )

    city_in_the_sky_central_tower_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_CENTRAL_OUTSIDE_POE_ISLAND_CHEST,
        city_in_the_sky_central_tower_second_floor,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_CENTRAL_OUTSIDE_POE_ISLAND_CHEST]
      )
    )

    city_in_the_sky_central_tower_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_BIG_KEY_CHEST,
        city_in_the_sky_central_tower_second_floor,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_BIG_KEY_CHEST]
      )
    )

    city_in_the_sky_central_tower_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_CHEST_BELOW_BIG_KEY_CHEST,
        city_in_the_sky_central_tower_second_floor,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_CHEST_BELOW_BIG_KEY_CHEST]
      )
    )

    city_in_the_sky_central_tower_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_POE_ABOVE_CENTRAL_FAN,
        city_in_the_sky_central_tower_second_floor,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_POE_ABOVE_CENTRAL_FAN]
      )
    )

    city_in_the_sky_east_wing = Region(RoomName.CITY_IN_THE_SKY_EAST_WING, player, world)
    regions[RoomName.CITY_IN_THE_SKY_EAST_WING] = city_in_the_sky_east_wing
    world.regions.append(city_in_the_sky_east_wing)

    city_in_the_sky_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_EAST_FIRST_WING_CHEST_AFTER_FANS,
        city_in_the_sky_east_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_EAST_FIRST_WING_CHEST_AFTER_FANS]
      )
    )

    city_in_the_sky_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_EAST_WING_LOWER_LEVEL_CHEST,
        city_in_the_sky_east_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_EAST_WING_LOWER_LEVEL_CHEST]
      )
    )

    city_in_the_sky_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_EAST_TILE_WORM_SMALL_CHEST,
        city_in_the_sky_east_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_EAST_TILE_WORM_SMALL_CHEST]
      )
    )

    city_in_the_sky_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_EAST_WING_AFTER_DINALFOS_ALCOVE_CHEST,
        city_in_the_sky_east_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_EAST_WING_AFTER_DINALFOS_ALCOVE_CHEST]
      )
    )

    city_in_the_sky_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_EAST_WING_AFTER_DINALFOS_LEDGE_CHEST,
        city_in_the_sky_east_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_EAST_WING_AFTER_DINALFOS_LEDGE_CHEST]
      )
    )

    city_in_the_sky_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_AERALFOS_CHEST,
        city_in_the_sky_east_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_AERALFOS_CHEST]
      )
    )

    city_in_the_sky_entrance = Region(RoomName.CITY_IN_THE_SKY_ENTRANCE, player, world)
    regions[RoomName.CITY_IN_THE_SKY_ENTRANCE] = city_in_the_sky_entrance
    world.regions.append(city_in_the_sky_entrance)

    city_in_the_sky_entrance.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_UNDERWATER_WEST_CHEST,
        city_in_the_sky_entrance,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_UNDERWATER_WEST_CHEST]
      )
    )

    city_in_the_sky_entrance.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_UNDERWATER_EAST_CHEST,
        city_in_the_sky_entrance,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_UNDERWATER_EAST_CHEST]
      )
    )

    city_in_the_sky_lobby = Region(RoomName.CITY_IN_THE_SKY_LOBBY, player, world)
    regions[RoomName.CITY_IN_THE_SKY_LOBBY] = city_in_the_sky_lobby
    world.regions.append(city_in_the_sky_lobby)

    city_in_the_sky_north_wing = Region(RoomName.CITY_IN_THE_SKY_NORTH_WING, player, world)
    regions[RoomName.CITY_IN_THE_SKY_NORTH_WING] = city_in_the_sky_north_wing
    world.regions.append(city_in_the_sky_north_wing)

    city_in_the_sky_north_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_CHEST_BEHIND_NORTH_FAN,
        city_in_the_sky_north_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_CHEST_BEHIND_NORTH_FAN]
      )
    )

    city_in_the_sky_west_wing = Region(RoomName.CITY_IN_THE_SKY_WEST_WING, player, world)
    regions[RoomName.CITY_IN_THE_SKY_WEST_WING] = city_in_the_sky_west_wing
    world.regions.append(city_in_the_sky_west_wing)

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_WEST_WING_FIRST_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_WEST_WING_FIRST_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_WEST_WING_BABA_BALCONY_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_WEST_WING_BABA_BALCONY_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_WEST_WING_NARROW_LEDGE_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_WEST_WING_NARROW_LEDGE_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_WEST_WING_TILE_WORM_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_WEST_WING_TILE_WORM_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_BABA_TOWER_TOP_SMALL_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_BABA_TOWER_TOP_SMALL_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_BABA_TOWER_NARROW_LEDGE_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_BABA_TOWER_NARROW_LEDGE_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_BABA_TOWER_ALCOVE_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_BABA_TOWER_ALCOVE_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_WEST_GARDEN_CORNER_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_WEST_GARDEN_CORNER_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LONE_ISLAND_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LONE_ISLAND_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LOWER_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LOWER_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LEDGE_CHEST,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_WEST_GARDEN_LEDGE_CHEST]
      )
    )

    city_in_the_sky_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.CITY_IN_THE_SKY_GARDEN_ISLAND_POE,
        city_in_the_sky_west_wing,
        LOCATION_TABLE[CheckName.CITY_IN_THE_SKY_GARDEN_ISLAND_POE]
      )
    )

    forest_temple_boss_room = Region(RoomName.FOREST_TEMPLE_BOSS_ROOM, player, world)
    regions[RoomName.FOREST_TEMPLE_BOSS_ROOM] = forest_temple_boss_room
    world.regions.append(forest_temple_boss_room)

    forest_temple_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_DIABABA_HEART_CONTAINER,
        forest_temple_boss_room,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_DIABABA_HEART_CONTAINER]
      )
    )

    forest_temple_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_DUNGEON_REWARD,
        forest_temple_boss_room,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_DUNGEON_REWARD]
      )
    )

    forest_temple_east_wing = Region(RoomName.FOREST_TEMPLE_EAST_WING, player, world)
    regions[RoomName.FOREST_TEMPLE_EAST_WING] = forest_temple_east_wing
    world.regions.append(forest_temple_east_wing)

    forest_temple_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_SECOND_MONKEY_UNDER_BRIDGE_CHEST,
        forest_temple_east_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_SECOND_MONKEY_UNDER_BRIDGE_CHEST]
      )
    )

    forest_temple_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_BIG_KEY_CHEST,
        forest_temple_east_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_BIG_KEY_CHEST]
      )
    )

    forest_temple_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_EAST_WATER_CAVE_CHEST,
        forest_temple_east_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_EAST_WATER_CAVE_CHEST]
      )
    )

    forest_temple_entrance = Region(RoomName.FOREST_TEMPLE_ENTRANCE, player, world)
    regions[RoomName.FOREST_TEMPLE_ENTRANCE] = forest_temple_entrance
    world.regions.append(forest_temple_entrance)

    forest_temple_entrance.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_ENTRANCE_VINES_CHEST,
        forest_temple_entrance,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_ENTRANCE_VINES_CHEST]
      )
    )

    forest_temple_lobby = Region(RoomName.FOREST_TEMPLE_LOBBY, player, world)
    regions[RoomName.FOREST_TEMPLE_LOBBY] = forest_temple_lobby
    world.regions.append(forest_temple_lobby)

    forest_temple_lobby.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_CENTRAL_CHEST_BEHIND_STAIRS,
        forest_temple_lobby,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_CENTRAL_CHEST_BEHIND_STAIRS]
      )
    )

    forest_temple_lobby.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_CENTRAL_NORTH_CHEST,
        forest_temple_lobby,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_CENTRAL_NORTH_CHEST]
      )
    )

    forest_temple_lobby.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_CENTRAL_CHEST_HANGING_FROM_WEB,
        forest_temple_lobby,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_CENTRAL_CHEST_HANGING_FROM_WEB]
      )
    )

    forest_temple_north_wing = Region(RoomName.FOREST_TEMPLE_NORTH_WING, player, world)
    regions[RoomName.FOREST_TEMPLE_NORTH_WING] = forest_temple_north_wing
    world.regions.append(forest_temple_north_wing)

    forest_temple_north_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_WINDLESS_BRIDGE_CHEST,
        forest_temple_north_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_WINDLESS_BRIDGE_CHEST]
      )
    )

    forest_temple_north_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_NORTH_DEKU_LIKE_CHEST,
        forest_temple_north_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_NORTH_DEKU_LIKE_CHEST]
      )
    )

    forest_temple_north_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_EAST_TILE_WORM_CHEST,
        forest_temple_north_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_EAST_TILE_WORM_CHEST]
      )
    )

    forest_temple_west_wing = Region(RoomName.FOREST_TEMPLE_WEST_WING, player, world)
    regions[RoomName.FOREST_TEMPLE_WEST_WING] = forest_temple_west_wing
    world.regions.append(forest_temple_west_wing)

    forest_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_WEST_DEKU_LIKE_CHEST,
        forest_temple_west_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_WEST_DEKU_LIKE_CHEST]
      )
    )

    forest_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_TOTEM_POLE_CHEST,
        forest_temple_west_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_TOTEM_POLE_CHEST]
      )
    )

    forest_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_WEST_TILE_WORM_ROOM_VINES_CHEST,
        forest_temple_west_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_WEST_TILE_WORM_ROOM_VINES_CHEST]
      )
    )

    forest_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_WEST_TILE_WORM_CHEST_BEHIND_STAIRS,
        forest_temple_west_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_WEST_TILE_WORM_CHEST_BEHIND_STAIRS]
      )
    )

    forest_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_BIG_BABA_KEY,
        forest_temple_west_wing,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_BIG_BABA_KEY]
      )
    )

    ook = Region(RoomName.OOK, player, world)
    regions[RoomName.OOK] = ook
    world.regions.append(ook)

    ook.locations.append(
    TPLocation(
        player,
        CheckName.FOREST_TEMPLE_GALE_BOOMERANG,
        ook,
        LOCATION_TABLE[CheckName.FOREST_TEMPLE_GALE_BOOMERANG]
      )
    )

    goron_mines_boss_room = Region(RoomName.GORON_MINES_BOSS_ROOM, player, world)
    regions[RoomName.GORON_MINES_BOSS_ROOM] = goron_mines_boss_room
    world.regions.append(goron_mines_boss_room)

    goron_mines_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_FYRUS_HEART_CONTAINER,
        goron_mines_boss_room,
        LOCATION_TABLE[CheckName.GORON_MINES_FYRUS_HEART_CONTAINER]
      )
    )

    goron_mines_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_DUNGEON_REWARD,
        goron_mines_boss_room,
        LOCATION_TABLE[CheckName.GORON_MINES_DUNGEON_REWARD]
      )
    )

    goron_mines_crystal_switch_room = Region(RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM, player, world)
    regions[RoomName.GORON_MINES_CRYSTAL_SWITCH_ROOM] = goron_mines_crystal_switch_room
    world.regions.append(goron_mines_crystal_switch_room)

    goron_mines_crystal_switch_room.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_CRYSTAL_SWITCH_ROOM_UNDERWATER_CHEST,
        goron_mines_crystal_switch_room,
        LOCATION_TABLE[CheckName.GORON_MINES_CRYSTAL_SWITCH_ROOM_UNDERWATER_CHEST]
      )
    )

    goron_mines_crystal_switch_room.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_CRYSTAL_SWITCH_ROOM_SMALL_CHEST,
        goron_mines_crystal_switch_room,
        LOCATION_TABLE[CheckName.GORON_MINES_CRYSTAL_SWITCH_ROOM_SMALL_CHEST]
      )
    )

    goron_mines_crystal_switch_room.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_AFTER_CRYSTAL_SWITCH_ROOM_MAGNET_WALL_CHEST,
        goron_mines_crystal_switch_room,
        LOCATION_TABLE[CheckName.GORON_MINES_AFTER_CRYSTAL_SWITCH_ROOM_MAGNET_WALL_CHEST]
      )
    )

    goron_mines_entrance = Region(RoomName.GORON_MINES_ENTRANCE, player, world)
    regions[RoomName.GORON_MINES_ENTRANCE] = goron_mines_entrance
    world.regions.append(goron_mines_entrance)

    goron_mines_entrance.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_ENTRANCE_CHEST,
        goron_mines_entrance,
        LOCATION_TABLE[CheckName.GORON_MINES_ENTRANCE_CHEST]
      )
    )

    goron_mines_lower_west_wing = Region(RoomName.GORON_MINES_LOWER_WEST_WING, player, world)
    regions[RoomName.GORON_MINES_LOWER_WEST_WING] = goron_mines_lower_west_wing
    world.regions.append(goron_mines_lower_west_wing)

    goron_mines_lower_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_MAGNET_MAZE_CHEST,
        goron_mines_lower_west_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_MAGNET_MAZE_CHEST]
      )
    )

    goron_mines_lower_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_GOR_AMATO_CHEST,
        goron_mines_lower_west_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_GOR_AMATO_CHEST]
      )
    )

    goron_mines_lower_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_GOR_AMATO_SMALL_CHEST,
        goron_mines_lower_west_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_GOR_AMATO_SMALL_CHEST]
      )
    )

    goron_mines_lower_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_GOR_AMATO_KEY_SHARD,
        goron_mines_lower_west_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_GOR_AMATO_KEY_SHARD]
      )
    )

    goron_mines_magnet_room = Region(RoomName.GORON_MINES_MAGNET_ROOM, player, world)
    regions[RoomName.GORON_MINES_MAGNET_ROOM] = goron_mines_magnet_room
    world.regions.append(goron_mines_magnet_room)

    goron_mines_magnet_room.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_MAIN_MAGNET_ROOM_BOTTOM_CHEST,
        goron_mines_magnet_room,
        LOCATION_TABLE[CheckName.GORON_MINES_MAIN_MAGNET_ROOM_BOTTOM_CHEST]
      )
    )

    goron_mines_magnet_room.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_MAIN_MAGNET_ROOM_TOP_CHEST,
        goron_mines_magnet_room,
        LOCATION_TABLE[CheckName.GORON_MINES_MAIN_MAGNET_ROOM_TOP_CHEST]
      )
    )

    goron_mines_north_wing = Region(RoomName.GORON_MINES_NORTH_WING, player, world)
    regions[RoomName.GORON_MINES_NORTH_WING] = goron_mines_north_wing
    world.regions.append(goron_mines_north_wing)

    goron_mines_north_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_OUTSIDE_BEAMOS_CHEST,
        goron_mines_north_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_OUTSIDE_BEAMOS_CHEST]
      )
    )

    goron_mines_north_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_OUTSIDE_UNDERWATER_CHEST,
        goron_mines_north_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_OUTSIDE_UNDERWATER_CHEST]
      )
    )

    goron_mines_north_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_OUTSIDE_CLAWSHOT_CHEST,
        goron_mines_north_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_OUTSIDE_CLAWSHOT_CHEST]
      )
    )

    goron_mines_upper_east_wing = Region(RoomName.GORON_MINES_UPPER_EAST_WING, player, world)
    regions[RoomName.GORON_MINES_UPPER_EAST_WING] = goron_mines_upper_east_wing
    world.regions.append(goron_mines_upper_east_wing)

    goron_mines_upper_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_GOR_EBIZO_CHEST,
        goron_mines_upper_east_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_GOR_EBIZO_CHEST]
      )
    )

    goron_mines_upper_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_CHEST_BEFORE_DANGORO,
        goron_mines_upper_east_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_CHEST_BEFORE_DANGORO]
      )
    )

    goron_mines_upper_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_GOR_EBIZO_KEY_SHARD,
        goron_mines_upper_east_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_GOR_EBIZO_KEY_SHARD]
      )
    )

    goron_mines_upper_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_DANGORO_CHEST,
        goron_mines_upper_east_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_DANGORO_CHEST]
      )
    )

    goron_mines_upper_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_BEAMOS_ROOM_CHEST,
        goron_mines_upper_east_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_BEAMOS_ROOM_CHEST]
      )
    )

    goron_mines_upper_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_GOR_LIGGS_CHEST,
        goron_mines_upper_east_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_GOR_LIGGS_CHEST]
      )
    )

    goron_mines_upper_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.GORON_MINES_GOR_LIGGS_KEY_SHARD,
        goron_mines_upper_east_wing,
        LOCATION_TABLE[CheckName.GORON_MINES_GOR_LIGGS_KEY_SHARD]
      )
    )

    ganondorf_castle = Region(RoomName.GANONDORF_CASTLE, player, world)
    regions[RoomName.GANONDORF_CASTLE] = ganondorf_castle
    world.regions.append(ganondorf_castle)

    hyrule_castle_entrance = Region(RoomName.HYRULE_CASTLE_ENTRANCE, player, world)
    regions[RoomName.HYRULE_CASTLE_ENTRANCE] = hyrule_castle_entrance
    world.regions.append(hyrule_castle_entrance)

    hyrule_castle_graveyard = Region(RoomName.HYRULE_CASTLE_GRAVEYARD, player, world)
    regions[RoomName.HYRULE_CASTLE_GRAVEYARD] = hyrule_castle_graveyard
    world.regions.append(hyrule_castle_graveyard)

    hyrule_castle_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_RIGHT_CHEST,
        hyrule_castle_graveyard,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_RIGHT_CHEST]
      )
    )

    hyrule_castle_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_FRONT_LEFT_CHEST,
        hyrule_castle_graveyard,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_FRONT_LEFT_CHEST]
      )
    )

    hyrule_castle_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_BACK_LEFT_CHEST,
        hyrule_castle_graveyard,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_GRAVEYARD_GRAVE_SWITCH_ROOM_BACK_LEFT_CHEST]
      )
    )

    hyrule_castle_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_GRAVEYARD_OWL_STATUE_CHEST,
        hyrule_castle_graveyard,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_GRAVEYARD_OWL_STATUE_CHEST]
      )
    )

    hyrule_castle_inside_east_wing = Region(RoomName.HYRULE_CASTLE_INSIDE_EAST_WING, player, world)
    regions[RoomName.HYRULE_CASTLE_INSIDE_EAST_WING] = hyrule_castle_inside_east_wing
    world.regions.append(hyrule_castle_inside_east_wing)

    hyrule_castle_inside_west_wing = Region(RoomName.HYRULE_CASTLE_INSIDE_WEST_WING, player, world)
    regions[RoomName.HYRULE_CASTLE_INSIDE_WEST_WING] = hyrule_castle_inside_west_wing
    world.regions.append(hyrule_castle_inside_west_wing)

    hyrule_castle_main_hall = Region(RoomName.HYRULE_CASTLE_MAIN_HALL, player, world)
    regions[RoomName.HYRULE_CASTLE_MAIN_HALL] = hyrule_castle_main_hall
    world.regions.append(hyrule_castle_main_hall)

    hyrule_castle_main_hall.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_MAIN_HALL_NORTHEAST_CHEST,
        hyrule_castle_main_hall,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_MAIN_HALL_NORTHEAST_CHEST]
      )
    )

    hyrule_castle_main_hall.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_MAIN_HALL_SOUTHWEST_CHEST,
        hyrule_castle_main_hall,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_MAIN_HALL_SOUTHWEST_CHEST]
      )
    )

    hyrule_castle_main_hall.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_MAIN_HALL_NORTHWEST_CHEST,
        hyrule_castle_main_hall,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_MAIN_HALL_NORTHWEST_CHEST]
      )
    )

    hyrule_castle_main_hall.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_LANTERN_STAIRCASE_CHEST,
        hyrule_castle_main_hall,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_LANTERN_STAIRCASE_CHEST]
      )
    )

    hyrule_castle_outside_east_wing = Region(RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING, player, world)
    regions[RoomName.HYRULE_CASTLE_OUTSIDE_EAST_WING] = hyrule_castle_outside_east_wing
    world.regions.append(hyrule_castle_outside_east_wing)

    hyrule_castle_outside_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_EAST_WING_BOOMERANG_PUZZLE_CHEST,
        hyrule_castle_outside_east_wing,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_EAST_WING_BOOMERANG_PUZZLE_CHEST]
      )
    )

    hyrule_castle_outside_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_EAST_WING_BALCONY_CHEST,
        hyrule_castle_outside_east_wing,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_EAST_WING_BALCONY_CHEST]
      )
    )

    hyrule_castle_outside_west_wing = Region(RoomName.HYRULE_CASTLE_OUTSIDE_WEST_WING, player, world)
    regions[RoomName.HYRULE_CASTLE_OUTSIDE_WEST_WING] = hyrule_castle_outside_west_wing
    world.regions.append(hyrule_castle_outside_west_wing)

    hyrule_castle_outside_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_WEST_COURTYARD_NORTH_SMALL_CHEST,
        hyrule_castle_outside_west_wing,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_WEST_COURTYARD_NORTH_SMALL_CHEST]
      )
    )

    hyrule_castle_outside_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_WEST_COURTYARD_CENTRAL_SMALL_CHEST,
        hyrule_castle_outside_west_wing,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_WEST_COURTYARD_CENTRAL_SMALL_CHEST]
      )
    )

    hyrule_castle_outside_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_KING_BULBLIN_KEY,
        hyrule_castle_outside_west_wing,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_KING_BULBLIN_KEY]
      )
    )

    hyrule_castle_third_floor_balcony = Region(RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY, player, world)
    regions[RoomName.HYRULE_CASTLE_THIRD_FLOOR_BALCONY] = hyrule_castle_third_floor_balcony
    world.regions.append(hyrule_castle_third_floor_balcony)

    hyrule_castle_third_floor_balcony.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_SOUTHEAST_BALCONY_TOWER_CHEST,
        hyrule_castle_third_floor_balcony,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_SOUTHEAST_BALCONY_TOWER_CHEST]
      )
    )

    hyrule_castle_third_floor_balcony.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_BIG_KEY_CHEST,
        hyrule_castle_third_floor_balcony,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_BIG_KEY_CHEST]
      )
    )

    hyrule_castle_tower_climb = Region(RoomName.HYRULE_CASTLE_TOWER_CLIMB, player, world)
    regions[RoomName.HYRULE_CASTLE_TOWER_CLIMB] = hyrule_castle_tower_climb
    world.regions.append(hyrule_castle_tower_climb)

    hyrule_castle_treasure_room = Region(RoomName.HYRULE_CASTLE_TREASURE_ROOM, player, world)
    regions[RoomName.HYRULE_CASTLE_TREASURE_ROOM] = hyrule_castle_treasure_room
    world.regions.append(hyrule_castle_treasure_room)

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_EIGHTH_SMALL_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_EIGHTH_SMALL_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_SEVENTH_SMALL_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_SEVENTH_SMALL_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_SIXTH_SMALL_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_SIXTH_SMALL_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIFTH_SMALL_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIFTH_SMALL_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_FOURTH_SMALL_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_FOURTH_SMALL_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_THIRD_SMALL_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_THIRD_SMALL_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_SECOND_SMALL_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_SECOND_SMALL_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIRST_SMALL_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIRST_SMALL_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIFTH_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIFTH_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_FOURTH_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_FOURTH_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_THIRD_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_THIRD_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_SECOND_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_SECOND_CHEST]
      )
    )

    hyrule_castle_treasure_room.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIRST_CHEST,
        hyrule_castle_treasure_room,
        LOCATION_TABLE[CheckName.HYRULE_CASTLE_TREASURE_ROOM_FIRST_CHEST]
      )
    )

    lakebed_temple_boss_room = Region(RoomName.LAKEBED_TEMPLE_BOSS_ROOM, player, world)
    regions[RoomName.LAKEBED_TEMPLE_BOSS_ROOM] = lakebed_temple_boss_room
    world.regions.append(lakebed_temple_boss_room)

    lakebed_temple_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_MORPHEEL_HEART_CONTAINER,
        lakebed_temple_boss_room,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_MORPHEEL_HEART_CONTAINER]
      )
    )

    lakebed_temple_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_DUNGEON_REWARD,
        lakebed_temple_boss_room,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_DUNGEON_REWARD]
      )
    )

    lakebed_temple_central_room = Region(RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM, player, world)
    regions[RoomName.LAKEBED_TEMPLE_CENTRAL_ROOM] = lakebed_temple_central_room
    world.regions.append(lakebed_temple_central_room)

    lakebed_temple_central_room.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_SMALL_CHEST,
        lakebed_temple_central_room,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_SMALL_CHEST]
      )
    )

    lakebed_temple_central_room.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_CHEST,
        lakebed_temple_central_room,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_CHEST]
      )
    )

    lakebed_temple_central_room.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_CHANDELIER_CHEST,
        lakebed_temple_central_room,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_CHANDELIER_CHEST]
      )
    )

    lakebed_temple_central_room.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_SPIRE_CHEST,
        lakebed_temple_central_room,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_CENTRAL_ROOM_SPIRE_CHEST]
      )
    )

    lakebed_temple_east_wing_first_floor = Region(RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR, player, world)
    regions[RoomName.LAKEBED_TEMPLE_EAST_WING_FIRST_FLOOR] = lakebed_temple_east_wing_first_floor
    world.regions.append(lakebed_temple_east_wing_first_floor)

    lakebed_temple_east_wing_first_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_EAST_LOWER_WATERWHEEL_STALACTITE_CHEST,
        lakebed_temple_east_wing_first_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_EAST_LOWER_WATERWHEEL_STALACTITE_CHEST]
      )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_EAST_LOWER_WATERWHEEL_BRIDGE_CHEST,
        lakebed_temple_east_wing_first_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_EAST_LOWER_WATERWHEEL_BRIDGE_CHEST]
      )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_ALCOVE_CHEST,
        lakebed_temple_east_wing_first_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_ALCOVE_CHEST]
      )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_UNDERWATER_LEFT_CHEST,
        lakebed_temple_east_wing_first_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_UNDERWATER_LEFT_CHEST]
      )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_UNDERWATER_RIGHT_CHEST,
        lakebed_temple_east_wing_first_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_BEFORE_DEKU_TOAD_UNDERWATER_RIGHT_CHEST]
      )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_DEKU_TOAD_CHEST,
        lakebed_temple_east_wing_first_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_DEKU_TOAD_CHEST]
      )
    )

    lakebed_temple_east_wing_second_floor = Region(RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR, player, world)
    regions[RoomName.LAKEBED_TEMPLE_EAST_WING_SECOND_FLOOR] = lakebed_temple_east_wing_second_floor
    world.regions.append(lakebed_temple_east_wing_second_floor)

    lakebed_temple_east_wing_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_EAST_SECOND_FLOOR_SOUTHWEST_CHEST,
        lakebed_temple_east_wing_second_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_EAST_SECOND_FLOOR_SOUTHWEST_CHEST]
      )
    )

    lakebed_temple_east_wing_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_EAST_SECOND_FLOOR_SOUTHEAST_CHEST,
        lakebed_temple_east_wing_second_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_EAST_SECOND_FLOOR_SOUTHEAST_CHEST]
      )
    )

    lakebed_temple_east_wing_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_EAST_WATER_SUPPLY_SMALL_CHEST,
        lakebed_temple_east_wing_second_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_EAST_WATER_SUPPLY_SMALL_CHEST]
      )
    )

    lakebed_temple_east_wing_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_EAST_WATER_SUPPLY_CLAWSHOT_CHEST,
        lakebed_temple_east_wing_second_floor,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_EAST_WATER_SUPPLY_CLAWSHOT_CHEST]
      )
    )

    lakebed_temple_entrance = Region(RoomName.LAKEBED_TEMPLE_ENTRANCE, player, world)
    regions[RoomName.LAKEBED_TEMPLE_ENTRANCE] = lakebed_temple_entrance
    world.regions.append(lakebed_temple_entrance)

    lakebed_temple_entrance.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_LOBBY_LEFT_CHEST,
        lakebed_temple_entrance,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_LOBBY_LEFT_CHEST]
      )
    )

    lakebed_temple_entrance.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_LOBBY_REAR_CHEST,
        lakebed_temple_entrance,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_LOBBY_REAR_CHEST]
      )
    )

    lakebed_temple_entrance.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_STALACTITE_ROOM_CHEST,
        lakebed_temple_entrance,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_STALACTITE_ROOM_CHEST]
      )
    )

    lakebed_temple_west_wing = Region(RoomName.LAKEBED_TEMPLE_WEST_WING, player, world)
    regions[RoomName.LAKEBED_TEMPLE_WEST_WING] = lakebed_temple_west_wing
    world.regions.append(lakebed_temple_west_wing)

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_WEST_LOWER_SMALL_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_WEST_LOWER_SMALL_CHEST]
      )
    )

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_CENTRAL_SMALL_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_CENTRAL_SMALL_CHEST]
      )
    )

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_UNDERWATER_MAZE_SMALL_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_UNDERWATER_MAZE_SMALL_CHEST]
      )
    )

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_BIG_KEY_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_BIG_KEY_CHEST]
      )
    )

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_SOUTHWEST_UNDERWATER_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_SOUTHWEST_UNDERWATER_CHEST]
      )
    )

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_NORTHEAST_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_NORTHEAST_CHEST]
      )
    )

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_SOUTHEAST_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_WEST_SECOND_FLOOR_SOUTHEAST_CHEST]
      )
    )

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_WEST_WATER_SUPPLY_SMALL_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_WEST_WATER_SUPPLY_SMALL_CHEST]
      )
    )

    lakebed_temple_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.LAKEBED_TEMPLE_WEST_WATER_SUPPLY_CHEST,
        lakebed_temple_west_wing,
        LOCATION_TABLE[CheckName.LAKEBED_TEMPLE_WEST_WATER_SUPPLY_CHEST]
      )
    )

    palace_of_twilight_entrance = Region(RoomName.PALACE_OF_TWILIGHT_ENTRANCE, player, world)
    regions[RoomName.PALACE_OF_TWILIGHT_ENTRANCE] = palace_of_twilight_entrance
    world.regions.append(palace_of_twilight_entrance)

    palace_of_twilight_entrance.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_COLLECT_BOTH_SOLS,
        palace_of_twilight_entrance,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_COLLECT_BOTH_SOLS]
      )
    )

    palace_of_twilight_west_wing = Region(RoomName.PALACE_OF_TWILIGHT_WEST_WING, player, world)
    regions[RoomName.PALACE_OF_TWILIGHT_WEST_WING] = palace_of_twilight_west_wing
    world.regions.append(palace_of_twilight_west_wing)

    palace_of_twilight_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_WEST_WING_FIRST_ROOM_CENTRAL_CHEST,
        palace_of_twilight_west_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_WEST_WING_FIRST_ROOM_CENTRAL_CHEST]
      )
    )

    palace_of_twilight_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_WEST_WING_CHEST_BEHIND_WALL_OF_DARKNESS,
        palace_of_twilight_west_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_WEST_WING_CHEST_BEHIND_WALL_OF_DARKNESS]
      )
    )

    palace_of_twilight_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_CENTRAL_CHEST,
        palace_of_twilight_west_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_CENTRAL_CHEST]
      )
    )

    palace_of_twilight_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_LOWER_SOUTH_CHEST,
        palace_of_twilight_west_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_LOWER_SOUTH_CHEST]
      )
    )

    palace_of_twilight_west_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_SOUTHEAST_CHEST,
        palace_of_twilight_west_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_WEST_WING_SECOND_ROOM_SOUTHEAST_CHEST]
      )
    )

    palace_of_twilight_east_wing = Region(RoomName.PALACE_OF_TWILIGHT_EAST_WING, player, world)
    regions[RoomName.PALACE_OF_TWILIGHT_EAST_WING] = palace_of_twilight_east_wing
    world.regions.append(palace_of_twilight_east_wing)

    palace_of_twilight_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_NORTH_SMALL_CHEST,
        palace_of_twilight_east_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_NORTH_SMALL_CHEST]
      )
    )

    palace_of_twilight_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_ZANT_HEAD_CHEST,
        palace_of_twilight_east_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_ZANT_HEAD_CHEST]
      )
    )

    palace_of_twilight_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_EAST_ALCOVE,
        palace_of_twilight_east_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_EAST_ALCOVE]
      )
    )

    palace_of_twilight_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_WEST_ALCOVE,
        palace_of_twilight_east_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_EAST_WING_FIRST_ROOM_WEST_ALCOVE]
      )
    )

    palace_of_twilight_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_NORTHEAST_CHEST,
        palace_of_twilight_east_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_NORTHEAST_CHEST]
      )
    )

    palace_of_twilight_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_NORTHWEST_CHEST,
        palace_of_twilight_east_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_NORTHWEST_CHEST]
      )
    )

    palace_of_twilight_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_SOUTHWEST_CHEST,
        palace_of_twilight_east_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_SOUTHWEST_CHEST]
      )
    )

    palace_of_twilight_east_wing.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_SOUTHEAST_CHEST,
        palace_of_twilight_east_wing,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_EAST_WING_SECOND_ROOM_SOUTHEAST_CHEST]
      )
    )

    palace_of_twilight_central_first_room = Region(RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM, player, world)
    regions[RoomName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM] = palace_of_twilight_central_first_room
    world.regions.append(palace_of_twilight_central_first_room)

    palace_of_twilight_central_first_room.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM_CHEST,
        palace_of_twilight_central_first_room,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_CENTRAL_FIRST_ROOM_CHEST]
      )
    )

    palace_of_twilight_outside_room = Region(RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM, player, world)
    regions[RoomName.PALACE_OF_TWILIGHT_OUTSIDE_ROOM] = palace_of_twilight_outside_room
    world.regions.append(palace_of_twilight_outside_room)

    palace_of_twilight_outside_room.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_BIG_KEY_CHEST,
        palace_of_twilight_outside_room,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_BIG_KEY_CHEST]
      )
    )

    palace_of_twilight_outside_room.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_CENTRAL_OUTDOOR_CHEST,
        palace_of_twilight_outside_room,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_CENTRAL_OUTDOOR_CHEST]
      )
    )

    palace_of_twilight_north_tower = Region(RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER, player, world)
    regions[RoomName.PALACE_OF_TWILIGHT_NORTH_TOWER] = palace_of_twilight_north_tower
    world.regions.append(palace_of_twilight_north_tower)

    palace_of_twilight_north_tower.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_CENTRAL_TOWER_CHEST,
        palace_of_twilight_north_tower,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_CENTRAL_TOWER_CHEST]
      )
    )

    palace_of_twilight_boss_room = Region(RoomName.PALACE_OF_TWILIGHT_BOSS_ROOM, player, world)
    regions[RoomName.PALACE_OF_TWILIGHT_BOSS_ROOM] = palace_of_twilight_boss_room
    world.regions.append(palace_of_twilight_boss_room)

    palace_of_twilight_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.PALACE_OF_TWILIGHT_ZANT_HEART_CONTAINER,
        palace_of_twilight_boss_room,
        LOCATION_TABLE[CheckName.PALACE_OF_TWILIGHT_ZANT_HEART_CONTAINER]
      )
    )

    snowpeak_ruins_left_door = Region(RoomName.SNOWPEAK_RUINS_LEFT_DOOR, player, world)
    regions[RoomName.SNOWPEAK_RUINS_LEFT_DOOR] = snowpeak_ruins_left_door
    world.regions.append(snowpeak_ruins_left_door)

    snowpeak_ruins_right_door = Region(RoomName.SNOWPEAK_RUINS_RIGHT_DOOR, player, world)
    regions[RoomName.SNOWPEAK_RUINS_RIGHT_DOOR] = snowpeak_ruins_right_door
    world.regions.append(snowpeak_ruins_right_door)

    snowpeak_ruins_boss_room = Region(RoomName.SNOWPEAK_RUINS_BOSS_ROOM, player, world)
    regions[RoomName.SNOWPEAK_RUINS_BOSS_ROOM] = snowpeak_ruins_boss_room
    world.regions.append(snowpeak_ruins_boss_room)

    snowpeak_ruins_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_BLIZZETA_HEART_CONTAINER,
        snowpeak_ruins_boss_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_BLIZZETA_HEART_CONTAINER]
      )
    )

    snowpeak_ruins_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_DUNGEON_REWARD,
        snowpeak_ruins_boss_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_DUNGEON_REWARD]
      )
    )

    snowpeak_ruins_caged_freezard_room = Region(RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM, player, world)
    regions[RoomName.SNOWPEAK_RUINS_CAGED_FREEZARD_ROOM] = snowpeak_ruins_caged_freezard_room
    world.regions.append(snowpeak_ruins_caged_freezard_room)

    snowpeak_ruins_caged_freezard_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_BROKEN_FLOOR_CHEST,
        snowpeak_ruins_caged_freezard_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_BROKEN_FLOOR_CHEST]
      )
    )

    snowpeak_ruins_chapel = Region(RoomName.SNOWPEAK_RUINS_CHAPEL, player, world)
    regions[RoomName.SNOWPEAK_RUINS_CHAPEL] = snowpeak_ruins_chapel
    world.regions.append(snowpeak_ruins_chapel)

    snowpeak_ruins_chapel.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_CHAPEL_CHEST,
        snowpeak_ruins_chapel,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_CHAPEL_CHEST]
      )
    )

    snowpeak_ruins_darkhammer_room = Region(RoomName.SNOWPEAK_RUINS_DARKHAMMER_ROOM, player, world)
    regions[RoomName.SNOWPEAK_RUINS_DARKHAMMER_ROOM] = snowpeak_ruins_darkhammer_room
    world.regions.append(snowpeak_ruins_darkhammer_room)

    snowpeak_ruins_darkhammer_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_BALL_AND_CHAIN,
        snowpeak_ruins_darkhammer_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_BALL_AND_CHAIN]
      )
    )

    snowpeak_ruins_darkhammer_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_CHEST_AFTER_DARKHAMMER,
        snowpeak_ruins_darkhammer_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_CHEST_AFTER_DARKHAMMER]
      )
    )

    snowpeak_ruins_east_courtyard = Region(RoomName.SNOWPEAK_RUINS_EAST_COURTYARD, player, world)
    regions[RoomName.SNOWPEAK_RUINS_EAST_COURTYARD] = snowpeak_ruins_east_courtyard
    world.regions.append(snowpeak_ruins_east_courtyard)

    snowpeak_ruins_east_courtyard.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_EAST_COURTYARD_BURIED_CHEST,
        snowpeak_ruins_east_courtyard,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_EAST_COURTYARD_BURIED_CHEST]
      )
    )

    snowpeak_ruins_east_courtyard.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_EAST_COURTYARD_CHEST,
        snowpeak_ruins_east_courtyard,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_EAST_COURTYARD_CHEST]
      )
    )

    snowpeak_ruins_entrance = Region(RoomName.SNOWPEAK_RUINS_ENTRANCE, player, world)
    regions[RoomName.SNOWPEAK_RUINS_ENTRANCE] = snowpeak_ruins_entrance
    world.regions.append(snowpeak_ruins_entrance)

    snowpeak_ruins_entrance.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_LOBBY_CHANDELIER_CHEST,
        snowpeak_ruins_entrance,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_LOBBY_CHANDELIER_CHEST]
      )
    )

    snowpeak_ruins_entrance.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_LOBBY_WEST_ARMOR_CHEST,
        snowpeak_ruins_entrance,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_LOBBY_WEST_ARMOR_CHEST]
      )
    )

    snowpeak_ruins_entrance.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_LOBBY_EAST_ARMOR_CHEST,
        snowpeak_ruins_entrance,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_LOBBY_EAST_ARMOR_CHEST]
      )
    )

    snowpeak_ruins_entrance.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_LOBBY_ARMOR_POE,
        snowpeak_ruins_entrance,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_LOBBY_ARMOR_POE]
      )
    )

    snowpeak_ruins_entrance.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_LOBBY_POE,
        snowpeak_ruins_entrance,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_LOBBY_POE]
      )
    )

    snowpeak_ruins_northeast_chilfos_room_first_floor = Region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR, player, world)
    regions[RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_FIRST_FLOOR] = snowpeak_ruins_northeast_chilfos_room_first_floor
    world.regions.append(snowpeak_ruins_northeast_chilfos_room_first_floor)

    snowpeak_ruins_northeast_chilfos_room_first_floor.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_ORDON_PUMPKIN_CHEST,
        snowpeak_ruins_northeast_chilfos_room_first_floor,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_ORDON_PUMPKIN_CHEST]
      )
    )

    snowpeak_ruins_northeast_chilfos_room_second_floor = Region(RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR, player, world)
    regions[RoomName.SNOWPEAK_RUINS_NORTHEAST_CHILFOS_ROOM_SECOND_FLOOR] = snowpeak_ruins_northeast_chilfos_room_second_floor
    world.regions.append(snowpeak_ruins_northeast_chilfos_room_second_floor)

    snowpeak_ruins_northeast_chilfos_room_second_floor.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_NORTHEAST_CHANDELIER_CHEST,
        snowpeak_ruins_northeast_chilfos_room_second_floor,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_NORTHEAST_CHANDELIER_CHEST]
      )
    )

    snowpeak_ruins_second_floor_mini_freezard_room = Region(RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM, player, world)
    regions[RoomName.SNOWPEAK_RUINS_SECOND_FLOOR_MINI_FREEZARD_ROOM] = snowpeak_ruins_second_floor_mini_freezard_room
    world.regions.append(snowpeak_ruins_second_floor_mini_freezard_room)

    snowpeak_ruins_second_floor_mini_freezard_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_ICE_ROOM_POE,
        snowpeak_ruins_second_floor_mini_freezard_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_ICE_ROOM_POE]
      )
    )

    snowpeak_ruins_west_cannon_room = Region(RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM, player, world)
    regions[RoomName.SNOWPEAK_RUINS_WEST_CANNON_ROOM] = snowpeak_ruins_west_cannon_room
    world.regions.append(snowpeak_ruins_west_cannon_room)

    snowpeak_ruins_west_cannon_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_WEST_CANNON_ROOM_CENTRAL_CHEST,
        snowpeak_ruins_west_cannon_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_WEST_CANNON_ROOM_CENTRAL_CHEST]
      )
    )

    snowpeak_ruins_west_cannon_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_WEST_CANNON_ROOM_CORNER_CHEST,
        snowpeak_ruins_west_cannon_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_WEST_CANNON_ROOM_CORNER_CHEST]
      )
    )

    snowpeak_ruins_west_courtyard = Region(RoomName.SNOWPEAK_RUINS_WEST_COURTYARD, player, world)
    regions[RoomName.SNOWPEAK_RUINS_WEST_COURTYARD] = snowpeak_ruins_west_courtyard
    world.regions.append(snowpeak_ruins_west_courtyard)

    snowpeak_ruins_west_courtyard.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_WEST_COURTYARD_BURIED_CHEST,
        snowpeak_ruins_west_courtyard,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_WEST_COURTYARD_BURIED_CHEST]
      )
    )

    snowpeak_ruins_west_courtyard.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_COURTYARD_CENTRAL_CHEST,
        snowpeak_ruins_west_courtyard,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_COURTYARD_CENTRAL_CHEST]
      )
    )

    snowpeak_ruins_wooden_beam_room = Region(RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM, player, world)
    regions[RoomName.SNOWPEAK_RUINS_WOODEN_BEAM_ROOM] = snowpeak_ruins_wooden_beam_room
    world.regions.append(snowpeak_ruins_wooden_beam_room)

    snowpeak_ruins_wooden_beam_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_CENTRAL_CHEST,
        snowpeak_ruins_wooden_beam_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_CENTRAL_CHEST]
      )
    )

    snowpeak_ruins_wooden_beam_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_NORTHWEST_CHEST,
        snowpeak_ruins_wooden_beam_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_NORTHWEST_CHEST]
      )
    )

    snowpeak_ruins_wooden_beam_room.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_CHANDELIER_CHEST,
        snowpeak_ruins_wooden_beam_room,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_WOODEN_BEAM_CHANDELIER_CHEST]
      )
    )

    snowpeak_ruins_yeto_and_yeta = Region(RoomName.SNOWPEAK_RUINS_YETO_AND_YETA, player, world)
    regions[RoomName.SNOWPEAK_RUINS_YETO_AND_YETA] = snowpeak_ruins_yeto_and_yeta
    world.regions.append(snowpeak_ruins_yeto_and_yeta)

    snowpeak_ruins_yeto_and_yeta.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_RUINS_MANSION_MAP,
        snowpeak_ruins_yeto_and_yeta,
        LOCATION_TABLE[CheckName.SNOWPEAK_RUINS_MANSION_MAP]
      )
    )

    temple_of_time_armos_antechamber = Region(RoomName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER, player, world)
    regions[RoomName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER] = temple_of_time_armos_antechamber
    world.regions.append(temple_of_time_armos_antechamber)

    temple_of_time_armos_antechamber.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_EAST_CHEST,
        temple_of_time_armos_antechamber,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_EAST_CHEST]
      )
    )

    temple_of_time_armos_antechamber.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_NORTH_CHEST,
        temple_of_time_armos_antechamber,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_NORTH_CHEST]
      )
    )

    temple_of_time_armos_antechamber.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_STATUE_CHEST,
        temple_of_time_armos_antechamber,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_ARMOS_ANTECHAMBER_STATUE_CHEST]
      )
    )

    temple_of_time_boss_room = Region(RoomName.TEMPLE_OF_TIME_BOSS_ROOM, player, world)
    regions[RoomName.TEMPLE_OF_TIME_BOSS_ROOM] = temple_of_time_boss_room
    world.regions.append(temple_of_time_boss_room)

    temple_of_time_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_ARMOGOHMA_HEART_CONTAINER,
        temple_of_time_boss_room,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_ARMOGOHMA_HEART_CONTAINER]
      )
    )

    temple_of_time_boss_room.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_DUNGEON_REWARD,
        temple_of_time_boss_room,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_DUNGEON_REWARD]
      )
    )

    temple_of_time_central_mechanical_platform = Region(RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM, player, world)
    regions[RoomName.TEMPLE_OF_TIME_CENTRAL_MECHANICAL_PLATFORM] = temple_of_time_central_mechanical_platform
    world.regions.append(temple_of_time_central_mechanical_platform)

    temple_of_time_central_mechanical_platform.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_POE_BEHIND_GATE,
        temple_of_time_central_mechanical_platform,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_POE_BEHIND_GATE]
      )
    )

    temple_of_time_connecting_corridors = Region(RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS, player, world)
    regions[RoomName.TEMPLE_OF_TIME_CONNECTING_CORRIDORS] = temple_of_time_connecting_corridors
    world.regions.append(temple_of_time_connecting_corridors)

    temple_of_time_connecting_corridors.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_GOHMA_GATE_CHEST,
        temple_of_time_connecting_corridors,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_GOHMA_GATE_CHEST]
      )
    )

    temple_of_time_connecting_corridors.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_WINDOW_CHEST,
        temple_of_time_connecting_corridors,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_WINDOW_CHEST]
      )
    )

    temple_of_time_connecting_corridors.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_ARMOS_CHEST,
        temple_of_time_connecting_corridors,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_FIRST_STAIRCASE_ARMOS_CHEST]
      )
    )

    temple_of_time_crumbling_corridor = Region(RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR, player, world)
    regions[RoomName.TEMPLE_OF_TIME_CRUMBLING_CORRIDOR] = temple_of_time_crumbling_corridor
    world.regions.append(temple_of_time_crumbling_corridor)

    temple_of_time_darknut_arena = Region(RoomName.TEMPLE_OF_TIME_DARKNUT_ARENA, player, world)
    regions[RoomName.TEMPLE_OF_TIME_DARKNUT_ARENA] = temple_of_time_darknut_arena
    world.regions.append(temple_of_time_darknut_arena)

    temple_of_time_darknut_arena.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_DARKNUT_CHEST,
        temple_of_time_darknut_arena,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_DARKNUT_CHEST]
      )
    )

    temple_of_time_entrance = Region(RoomName.TEMPLE_OF_TIME_ENTRANCE, player, world)
    regions[RoomName.TEMPLE_OF_TIME_ENTRANCE] = temple_of_time_entrance
    world.regions.append(temple_of_time_entrance)

    temple_of_time_entrance.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_LOBBY_LANTERN_CHEST,
        temple_of_time_entrance,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_LOBBY_LANTERN_CHEST]
      )
    )

    temple_of_time_floor_switch_puzzle_room = Region(RoomName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM, player, world)
    regions[RoomName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM] = temple_of_time_floor_switch_puzzle_room
    world.regions.append(temple_of_time_floor_switch_puzzle_room)

    temple_of_time_floor_switch_puzzle_room.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_BIG_KEY_CHEST,
        temple_of_time_floor_switch_puzzle_room,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_BIG_KEY_CHEST]
      )
    )

    temple_of_time_floor_switch_puzzle_room.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM_UPPER_CHEST,
        temple_of_time_floor_switch_puzzle_room,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_FLOOR_SWITCH_PUZZLE_ROOM_UPPER_CHEST]
      )
    )

    temple_of_time_moving_wall_hallways = Region(RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS, player, world)
    regions[RoomName.TEMPLE_OF_TIME_MOVING_WALL_HALLWAYS] = temple_of_time_moving_wall_hallways
    world.regions.append(temple_of_time_moving_wall_hallways)

    temple_of_time_moving_wall_hallways.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_MOVING_WALL_BEAMOS_ROOM_CHEST,
        temple_of_time_moving_wall_hallways,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_MOVING_WALL_BEAMOS_ROOM_CHEST]
      )
    )

    temple_of_time_moving_wall_hallways.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_MOVING_WALL_DINALFOS_ROOM_CHEST,
        temple_of_time_moving_wall_hallways,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_MOVING_WALL_DINALFOS_ROOM_CHEST]
      )
    )

    temple_of_time_scales_of_time = Region(RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME, player, world)
    regions[RoomName.TEMPLE_OF_TIME_SCALES_OF_TIME] = temple_of_time_scales_of_time
    world.regions.append(temple_of_time_scales_of_time)

    temple_of_time_scales_of_time.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_SCALES_GOHMA_CHEST,
        temple_of_time_scales_of_time,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_SCALES_GOHMA_CHEST]
      )
    )

    temple_of_time_scales_of_time.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_SCALES_UPPER_CHEST,
        temple_of_time_scales_of_time,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_SCALES_UPPER_CHEST]
      )
    )

    temple_of_time_scales_of_time.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_POE_ABOVE_SCALES,
        temple_of_time_scales_of_time,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_POE_ABOVE_SCALES]
      )
    )

    temple_of_time_upper_spike_trap_corridor = Region(RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR, player, world)
    regions[RoomName.TEMPLE_OF_TIME_UPPER_SPIKE_TRAP_CORRIDOR] = temple_of_time_upper_spike_trap_corridor
    world.regions.append(temple_of_time_upper_spike_trap_corridor)

    temple_of_time_upper_spike_trap_corridor.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_GILLOUTINE_CHEST,
        temple_of_time_upper_spike_trap_corridor,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_GILLOUTINE_CHEST]
      )
    )

    temple_of_time_upper_spike_trap_corridor.locations.append(
    TPLocation(
        player,
        CheckName.TEMPLE_OF_TIME_CHEST_BEFORE_DARKNUT,
        temple_of_time_upper_spike_trap_corridor,
        LOCATION_TABLE[CheckName.TEMPLE_OF_TIME_CHEST_BEFORE_DARKNUT]
      )
    )

    death_mountain_near_kakariko = Region(RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO, player, world)
    regions[RoomName.DEATH_MOUNTAIN_NEAR_KAKARIKO] = death_mountain_near_kakariko
    world.regions.append(death_mountain_near_kakariko)

    death_mountain_trail = Region(RoomName.DEATH_MOUNTAIN_TRAIL, player, world)
    regions[RoomName.DEATH_MOUNTAIN_TRAIL] = death_mountain_trail
    world.regions.append(death_mountain_trail)

    death_mountain_trail.locations.append(
    TPLocation(
        player,
        CheckName.DEATH_MOUNTAIN_ALCOVE_CHEST,
        death_mountain_trail,
        LOCATION_TABLE[CheckName.DEATH_MOUNTAIN_ALCOVE_CHEST]
      )
    )

    death_mountain_trail.locations.append(
    TPLocation(
        player,
        CheckName.DEATH_MOUNTAIN_TRAIL_POE,
        death_mountain_trail,
        LOCATION_TABLE[CheckName.DEATH_MOUNTAIN_TRAIL_POE]
      )
    )

    death_mountain_volcano = Region(RoomName.DEATH_MOUNTAIN_VOLCANO, player, world)
    regions[RoomName.DEATH_MOUNTAIN_VOLCANO] = death_mountain_volcano
    world.regions.append(death_mountain_volcano)

    death_mountain_outside_sumo_hall = Region(RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL, player, world)
    regions[RoomName.DEATH_MOUNTAIN_OUTSIDE_SUMO_HALL] = death_mountain_outside_sumo_hall
    world.regions.append(death_mountain_outside_sumo_hall)

    death_mountain_elevator_lower = Region(RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER, player, world)
    regions[RoomName.DEATH_MOUNTAIN_ELEVATOR_LOWER] = death_mountain_elevator_lower
    world.regions.append(death_mountain_elevator_lower)

    death_mountain_sumo_hall = Region(RoomName.DEATH_MOUNTAIN_SUMO_HALL, player, world)
    regions[RoomName.DEATH_MOUNTAIN_SUMO_HALL] = death_mountain_sumo_hall
    world.regions.append(death_mountain_sumo_hall)

    death_mountain_sumo_hall_elevator = Region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR, player, world)
    regions[RoomName.DEATH_MOUNTAIN_SUMO_HALL_ELEVATOR] = death_mountain_sumo_hall_elevator
    world.regions.append(death_mountain_sumo_hall_elevator)

    death_mountain_sumo_hall_goron_mines_tunnel = Region(RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL, player, world)
    regions[RoomName.DEATH_MOUNTAIN_SUMO_HALL_GORON_MINES_TUNNEL] = death_mountain_sumo_hall_goron_mines_tunnel
    world.regions.append(death_mountain_sumo_hall_goron_mines_tunnel)

    hidden_village = Region(RoomName.HIDDEN_VILLAGE, player, world)
    regions[RoomName.HIDDEN_VILLAGE] = hidden_village
    world.regions.append(hidden_village)

    hidden_village.locations.append(
    TPLocation(
        player,
        CheckName.CATS_HIDE_AND_SEEK_MINIGAME,
        hidden_village,
        LOCATION_TABLE[CheckName.CATS_HIDE_AND_SEEK_MINIGAME]
      )
    )

    hidden_village.locations.append(
    TPLocation(
        player,
        CheckName.ILIA_CHARM,
        hidden_village,
        LOCATION_TABLE[CheckName.ILIA_CHARM]
      )
    )

    hidden_village.locations.append(
    TPLocation(
        player,
        CheckName.HIDDEN_VILLAGE_POE,
        hidden_village,
        LOCATION_TABLE[CheckName.HIDDEN_VILLAGE_POE]
      )
    )

    hidden_village_impaz_house = Region(RoomName.HIDDEN_VILLAGE_IMPAZ_HOUSE, player, world)
    regions[RoomName.HIDDEN_VILLAGE_IMPAZ_HOUSE] = hidden_village_impaz_house
    world.regions.append(hidden_village_impaz_house)

    hidden_village_impaz_house.locations.append(
    TPLocation(
        player,
        CheckName.SKYBOOK_FROM_IMPAZ,
        hidden_village_impaz_house,
        LOCATION_TABLE[CheckName.SKYBOOK_FROM_IMPAZ]
      )
    )

    kakariko_gorge = Region(RoomName.KAKARIKO_GORGE, player, world)
    regions[RoomName.KAKARIKO_GORGE] = kakariko_gorge
    world.regions.append(kakariko_gorge)

    kakariko_gorge.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GORGE_OWL_STATUE_CHEST,
        kakariko_gorge,
        LOCATION_TABLE[CheckName.KAKARIKO_GORGE_OWL_STATUE_CHEST]
      )
    )

    kakariko_gorge.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GORGE_DOUBLE_CLAWSHOT_CHEST,
        kakariko_gorge,
        LOCATION_TABLE[CheckName.KAKARIKO_GORGE_DOUBLE_CLAWSHOT_CHEST]
      )
    )

    kakariko_gorge.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GORGE_SPIRE_HEART_PIECE,
        kakariko_gorge,
        LOCATION_TABLE[CheckName.KAKARIKO_GORGE_SPIRE_HEART_PIECE]
      )
    )

    kakariko_gorge.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GORGE_OWL_STATUE_SKY_CHARACTER,
        kakariko_gorge,
        LOCATION_TABLE[CheckName.KAKARIKO_GORGE_OWL_STATUE_SKY_CHARACTER]
      )
    )

    kakariko_gorge.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GORGE_MALE_PILL_BUG,
        kakariko_gorge,
        LOCATION_TABLE[CheckName.KAKARIKO_GORGE_MALE_PILL_BUG]
      )
    )

    kakariko_gorge.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GORGE_FEMALE_PILL_BUG,
        kakariko_gorge,
        LOCATION_TABLE[CheckName.KAKARIKO_GORGE_FEMALE_PILL_BUG]
      )
    )

    kakariko_gorge.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GORGE_POE,
        kakariko_gorge,
        LOCATION_TABLE[CheckName.KAKARIKO_GORGE_POE]
      )
    )

    kakariko_gorge_cave_entrance = Region(RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE, player, world)
    regions[RoomName.KAKARIKO_GORGE_CAVE_ENTRANCE] = kakariko_gorge_cave_entrance
    world.regions.append(kakariko_gorge_cave_entrance)

    kakariko_gorge_behind_gate = Region(RoomName.KAKARIKO_GORGE_BEHIND_GATE, player, world)
    regions[RoomName.KAKARIKO_GORGE_BEHIND_GATE] = kakariko_gorge_behind_gate
    world.regions.append(kakariko_gorge_behind_gate)

    eldin_lantern_cave = Region(RoomName.ELDIN_LANTERN_CAVE, player, world)
    regions[RoomName.ELDIN_LANTERN_CAVE] = eldin_lantern_cave
    world.regions.append(eldin_lantern_cave)

    eldin_lantern_cave.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_LANTERN_CAVE_FIRST_CHEST,
        eldin_lantern_cave,
        LOCATION_TABLE[CheckName.ELDIN_LANTERN_CAVE_FIRST_CHEST]
      )
    )

    eldin_lantern_cave.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_LANTERN_CAVE_LANTERN_CHEST,
        eldin_lantern_cave,
        LOCATION_TABLE[CheckName.ELDIN_LANTERN_CAVE_LANTERN_CHEST]
      )
    )

    eldin_lantern_cave.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_LANTERN_CAVE_SECOND_CHEST,
        eldin_lantern_cave,
        LOCATION_TABLE[CheckName.ELDIN_LANTERN_CAVE_SECOND_CHEST]
      )
    )

    eldin_lantern_cave.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_LANTERN_CAVE_POE,
        eldin_lantern_cave,
        LOCATION_TABLE[CheckName.ELDIN_LANTERN_CAVE_POE]
      )
    )

    kakariko_gorge_keese_grotto = Region(RoomName.KAKARIKO_GORGE_KEESE_GROTTO, player, world)
    regions[RoomName.KAKARIKO_GORGE_KEESE_GROTTO] = kakariko_gorge_keese_grotto
    world.regions.append(kakariko_gorge_keese_grotto)

    eldin_field = Region(RoomName.ELDIN_FIELD, player, world)
    regions[RoomName.ELDIN_FIELD] = eldin_field
    world.regions.append(eldin_field)

    eldin_field.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_BOMB_ROCK_CHEST,
        eldin_field,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_BOMB_ROCK_CHEST]
      )
    )

    eldin_field.locations.append(
    TPLocation(
        player,
        CheckName.BRIDGE_OF_ELDIN_OWL_STATUE_CHEST,
        eldin_field,
        LOCATION_TABLE[CheckName.BRIDGE_OF_ELDIN_OWL_STATUE_CHEST]
      )
    )

    eldin_field.locations.append(
    TPLocation(
        player,
        CheckName.GORON_SPRINGWATER_RUSH,
        eldin_field,
        LOCATION_TABLE[CheckName.GORON_SPRINGWATER_RUSH]
      )
    )

    eldin_field.locations.append(
    TPLocation(
        player,
        CheckName.BRIDGE_OF_ELDIN_OWL_STATUE_SKY_CHARACTER,
        eldin_field,
        LOCATION_TABLE[CheckName.BRIDGE_OF_ELDIN_OWL_STATUE_SKY_CHARACTER]
      )
    )

    eldin_field.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_MALE_GRASSHOPPER,
        eldin_field,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_MALE_GRASSHOPPER]
      )
    )

    eldin_field.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_FEMALE_GRASSHOPPER,
        eldin_field,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_FEMALE_GRASSHOPPER]
      )
    )

    eldin_field.locations.append(
    TPLocation(
        player,
        CheckName.BRIDGE_OF_ELDIN_MALE_PHASMID,
        eldin_field,
        LOCATION_TABLE[CheckName.BRIDGE_OF_ELDIN_MALE_PHASMID]
      )
    )

    eldin_field.locations.append(
    TPLocation(
        player,
        CheckName.BRIDGE_OF_ELDIN_FEMALE_PHASMID,
        eldin_field,
        LOCATION_TABLE[CheckName.BRIDGE_OF_ELDIN_FEMALE_PHASMID]
      )
    )

    eldin_field_near_castle_town = Region(RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN, player, world)
    regions[RoomName.ELDIN_FIELD_NEAR_CASTLE_TOWN] = eldin_field_near_castle_town
    world.regions.append(eldin_field_near_castle_town)

    eldin_field_lava_cave_ledge = Region(RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE, player, world)
    regions[RoomName.ELDIN_FIELD_LAVA_CAVE_LEDGE] = eldin_field_lava_cave_ledge
    world.regions.append(eldin_field_lava_cave_ledge)

    eldin_field_from_lava_cave_lower = Region(RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER, player, world)
    regions[RoomName.ELDIN_FIELD_FROM_LAVA_CAVE_LOWER] = eldin_field_from_lava_cave_lower
    world.regions.append(eldin_field_from_lava_cave_lower)

    north_eldin_field = Region(RoomName.NORTH_ELDIN_FIELD, player, world)
    regions[RoomName.NORTH_ELDIN_FIELD] = north_eldin_field
    world.regions.append(north_eldin_field)

    eldin_field_outside_hidden_village = Region(RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE, player, world)
    regions[RoomName.ELDIN_FIELD_OUTSIDE_HIDDEN_VILLAGE] = eldin_field_outside_hidden_village
    world.regions.append(eldin_field_outside_hidden_village)

    eldin_field_grotto_platform = Region(RoomName.ELDIN_FIELD_GROTTO_PLATFORM, player, world)
    regions[RoomName.ELDIN_FIELD_GROTTO_PLATFORM] = eldin_field_grotto_platform
    world.regions.append(eldin_field_grotto_platform)

    eldin_field_lava_cave_upper = Region(RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER, player, world)
    regions[RoomName.ELDIN_FIELD_LAVA_CAVE_UPPER] = eldin_field_lava_cave_upper
    world.regions.append(eldin_field_lava_cave_upper)

    eldin_field_lava_cave_upper.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_STOCKCAVE_UPPER_CHEST,
        eldin_field_lava_cave_upper,
        LOCATION_TABLE[CheckName.ELDIN_STOCKCAVE_UPPER_CHEST]
      )
    )

    eldin_field_lava_cave_lower = Region(RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER, player, world)
    regions[RoomName.ELDIN_FIELD_LAVA_CAVE_LOWER] = eldin_field_lava_cave_lower
    world.regions.append(eldin_field_lava_cave_lower)

    eldin_field_lava_cave_lower.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_STOCKCAVE_LANTERN_CHEST,
        eldin_field_lava_cave_lower,
        LOCATION_TABLE[CheckName.ELDIN_STOCKCAVE_LANTERN_CHEST]
      )
    )

    eldin_field_lava_cave_lower.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_STOCKCAVE_LOWEST_CHEST,
        eldin_field_lava_cave_lower,
        LOCATION_TABLE[CheckName.ELDIN_STOCKCAVE_LOWEST_CHEST]
      )
    )

    eldin_field_bomskit_grotto = Region(RoomName.ELDIN_FIELD_BOMSKIT_GROTTO, player, world)
    regions[RoomName.ELDIN_FIELD_BOMSKIT_GROTTO] = eldin_field_bomskit_grotto
    world.regions.append(eldin_field_bomskit_grotto)

    eldin_field_bomskit_grotto.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_BOMSKIT_GROTTO_LEFT_CHEST,
        eldin_field_bomskit_grotto,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_BOMSKIT_GROTTO_LEFT_CHEST]
      )
    )

    eldin_field_bomskit_grotto.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_BOMSKIT_GROTTO_LANTERN_CHEST,
        eldin_field_bomskit_grotto,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_BOMSKIT_GROTTO_LANTERN_CHEST]
      )
    )

    eldin_field_water_bomb_fish_grotto = Region(RoomName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO, player, world)
    regions[RoomName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO] = eldin_field_water_bomb_fish_grotto
    world.regions.append(eldin_field_water_bomb_fish_grotto)

    eldin_field_water_bomb_fish_grotto.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO_CHEST,
        eldin_field_water_bomb_fish_grotto,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_WATER_BOMB_FISH_GROTTO_CHEST]
      )
    )

    eldin_field_stalfos_grotto = Region(RoomName.ELDIN_FIELD_STALFOS_GROTTO, player, world)
    regions[RoomName.ELDIN_FIELD_STALFOS_GROTTO] = eldin_field_stalfos_grotto
    world.regions.append(eldin_field_stalfos_grotto)

    eldin_field_stalfos_grotto.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_STALFOS_GROTTO_RIGHT_SMALL_CHEST,
        eldin_field_stalfos_grotto,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_STALFOS_GROTTO_RIGHT_SMALL_CHEST]
      )
    )

    eldin_field_stalfos_grotto.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_STALFOS_GROTTO_LEFT_SMALL_CHEST,
        eldin_field_stalfos_grotto,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_STALFOS_GROTTO_LEFT_SMALL_CHEST]
      )
    )

    eldin_field_stalfos_grotto.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_FIELD_STALFOS_GROTTO_STALFOS_CHEST,
        eldin_field_stalfos_grotto,
        LOCATION_TABLE[CheckName.ELDIN_FIELD_STALFOS_GROTTO_STALFOS_CHEST]
      )
    )

    lower_kakariko_village = Region(RoomName.LOWER_KAKARIKO_VILLAGE, player, world)
    regions[RoomName.LOWER_KAKARIKO_VILLAGE] = lower_kakariko_village
    world.regions.append(lower_kakariko_village)

    lower_kakariko_village.locations.append(
    TPLocation(
        player,
        CheckName.ELDIN_SPRING_UNDERWATER_CHEST,
        lower_kakariko_village,
        LOCATION_TABLE[CheckName.ELDIN_SPRING_UNDERWATER_CHEST]
      )
    )

    lower_kakariko_village.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_VILLAGE_BOMB_ROCK_SPIRE_HEART_PIECE,
        lower_kakariko_village,
        LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_BOMB_ROCK_SPIRE_HEART_PIECE]
      )
    )

    upper_kakariko_village = Region(RoomName.UPPER_KAKARIKO_VILLAGE, player, world)
    regions[RoomName.UPPER_KAKARIKO_VILLAGE] = upper_kakariko_village
    world.regions.append(upper_kakariko_village)

    upper_kakariko_village.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_VILLAGE_BOMB_SHOP_POE,
        upper_kakariko_village,
        LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_BOMB_SHOP_POE]
      )
    )

    upper_kakariko_village.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_VILLAGE_WATCHTOWER_POE,
        upper_kakariko_village,
        LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_WATCHTOWER_POE]
      )
    )

    upper_kakariko_village.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_WATCHTOWER_ALCOVE_CHEST,
        upper_kakariko_village,
        LOCATION_TABLE[CheckName.KAKARIKO_WATCHTOWER_ALCOVE_CHEST]
      )
    )

    kakariko_top_of_watchtower = Region(RoomName.KAKARIKO_TOP_OF_WATCHTOWER, player, world)
    regions[RoomName.KAKARIKO_TOP_OF_WATCHTOWER] = kakariko_top_of_watchtower
    world.regions.append(kakariko_top_of_watchtower)

    kakariko_top_of_watchtower.locations.append(
    TPLocation(
        player,
        CheckName.TALO_SHARPSHOOTING,
        kakariko_top_of_watchtower,
        LOCATION_TABLE[CheckName.TALO_SHARPSHOOTING]
      )
    )

    kakariko_village_behind_gate = Region(RoomName.KAKARIKO_VILLAGE_BEHIND_GATE, player, world)
    regions[RoomName.KAKARIKO_VILLAGE_BEHIND_GATE] = kakariko_village_behind_gate
    world.regions.append(kakariko_village_behind_gate)

    kakariko_renados_sanctuary_front_left_door = Region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR, player, world)
    regions[RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_LEFT_DOOR] = kakariko_renados_sanctuary_front_left_door
    world.regions.append(kakariko_renados_sanctuary_front_left_door)

    kakariko_renados_sanctuary_front_right_door = Region(RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR, player, world)
    regions[RoomName.KAKARIKO_RENADOS_SANCTUARY_FRONT_RIGHT_DOOR] = kakariko_renados_sanctuary_front_right_door
    world.regions.append(kakariko_renados_sanctuary_front_right_door)

    kakariko_renados_sanctuary_back_left_door = Region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR, player, world)
    regions[RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_LEFT_DOOR] = kakariko_renados_sanctuary_back_left_door
    world.regions.append(kakariko_renados_sanctuary_back_left_door)

    kakariko_renados_sanctuary_back_right_door = Region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR, player, world)
    regions[RoomName.KAKARIKO_RENADOS_SANCTUARY_BACK_RIGHT_DOOR] = kakariko_renados_sanctuary_back_right_door
    world.regions.append(kakariko_renados_sanctuary_back_right_door)

    kakariko_renados_sanctuary = Region(RoomName.KAKARIKO_RENADOS_SANCTUARY, player, world)
    regions[RoomName.KAKARIKO_RENADOS_SANCTUARY] = kakariko_renados_sanctuary
    world.regions.append(kakariko_renados_sanctuary)

    kakariko_renados_sanctuary.locations.append(
    TPLocation(
        player,
        CheckName.RENADOS_LETTER,
        kakariko_renados_sanctuary,
        LOCATION_TABLE[CheckName.RENADOS_LETTER]
      )
    )

    kakariko_renados_sanctuary.locations.append(
    TPLocation(
        player,
        CheckName.ILIA_MEMORY_REWARD,
        kakariko_renados_sanctuary,
        LOCATION_TABLE[CheckName.ILIA_MEMORY_REWARD]
      )
    )

    kakariko_renados_sanctuary_basement = Region(RoomName.KAKARIKO_RENADOS_SANCTUARY_BASEMENT, player, world)
    regions[RoomName.KAKARIKO_RENADOS_SANCTUARY_BASEMENT] = kakariko_renados_sanctuary_basement
    world.regions.append(kakariko_renados_sanctuary_basement)

    kakariko_malo_mart = Region(RoomName.KAKARIKO_MALO_MART, player, world)
    regions[RoomName.KAKARIKO_MALO_MART] = kakariko_malo_mart
    world.regions.append(kakariko_malo_mart)

    kakariko_malo_mart.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_VILLAGE_MALO_MART_HYLIAN_SHIELD,
        kakariko_malo_mart,
        LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_MALO_MART_HYLIAN_SHIELD]
      )
    )

    kakariko_malo_mart.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_VILLAGE_MALO_MART_HAWKEYE,
        kakariko_malo_mart,
        LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_MALO_MART_HAWKEYE]
      )
    )

    kakariko_malo_mart.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_VILLAGE_MALO_MART_RED_POTION,
        kakariko_malo_mart,
        LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_MALO_MART_RED_POTION]
      )
    )

    kakariko_malo_mart.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_VILLAGE_MALO_MART_WOODEN_SHIELD,
        kakariko_malo_mart,
        LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_MALO_MART_WOODEN_SHIELD]
      )
    )

    kakariko_elde_inn_left_door = Region(RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR, player, world)
    regions[RoomName.KAKARIKO_ELDE_INN_LEFT_DOOR] = kakariko_elde_inn_left_door
    world.regions.append(kakariko_elde_inn_left_door)

    kakariko_elde_inn_right_door = Region(RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR, player, world)
    regions[RoomName.KAKARIKO_ELDE_INN_RIGHT_DOOR] = kakariko_elde_inn_right_door
    world.regions.append(kakariko_elde_inn_right_door)

    kakariko_elde_inn = Region(RoomName.KAKARIKO_ELDE_INN, player, world)
    regions[RoomName.KAKARIKO_ELDE_INN] = kakariko_elde_inn
    world.regions.append(kakariko_elde_inn)

    kakariko_elde_inn.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_INN_CHEST,
        kakariko_elde_inn,
        LOCATION_TABLE[CheckName.KAKARIKO_INN_CHEST]
      )
    )

    kakariko_bug_house_door = Region(RoomName.KAKARIKO_BUG_HOUSE_DOOR, player, world)
    regions[RoomName.KAKARIKO_BUG_HOUSE_DOOR] = kakariko_bug_house_door
    world.regions.append(kakariko_bug_house_door)

    kakariko_bug_house_ceiling_hole = Region(RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE, player, world)
    regions[RoomName.KAKARIKO_BUG_HOUSE_CEILING_HOLE] = kakariko_bug_house_ceiling_hole
    world.regions.append(kakariko_bug_house_ceiling_hole)

    kakariko_bug_house = Region(RoomName.KAKARIKO_BUG_HOUSE, player, world)
    regions[RoomName.KAKARIKO_BUG_HOUSE] = kakariko_bug_house
    world.regions.append(kakariko_bug_house)

    kakariko_bug_house.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_VILLAGE_FEMALE_ANT,
        kakariko_bug_house,
        LOCATION_TABLE[CheckName.KAKARIKO_VILLAGE_FEMALE_ANT]
      )
    )

    kakariko_barnes_bomb_shop_lower = Region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER, player, world)
    regions[RoomName.KAKARIKO_BARNES_BOMB_SHOP_LOWER] = kakariko_barnes_bomb_shop_lower
    world.regions.append(kakariko_barnes_bomb_shop_lower)

    kakariko_barnes_bomb_shop_lower.locations.append(
    TPLocation(
        player,
        CheckName.BARNES_BOMB_BAG,
        kakariko_barnes_bomb_shop_lower,
        LOCATION_TABLE[CheckName.BARNES_BOMB_BAG]
      )
    )

    kakariko_barnes_bomb_shop_upper = Region(RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER, player, world)
    regions[RoomName.KAKARIKO_BARNES_BOMB_SHOP_UPPER] = kakariko_barnes_bomb_shop_upper
    world.regions.append(kakariko_barnes_bomb_shop_upper)

    kakariko_watchtower_lower_door = Region(RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR, player, world)
    regions[RoomName.KAKARIKO_WATCHTOWER_LOWER_DOOR] = kakariko_watchtower_lower_door
    world.regions.append(kakariko_watchtower_lower_door)

    kakariko_watchtower_dig_spot = Region(RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT, player, world)
    regions[RoomName.KAKARIKO_WATCHTOWER_DIG_SPOT] = kakariko_watchtower_dig_spot
    world.regions.append(kakariko_watchtower_dig_spot)

    kakariko_watchtower_upper_door = Region(RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR, player, world)
    regions[RoomName.KAKARIKO_WATCHTOWER_UPPER_DOOR] = kakariko_watchtower_upper_door
    world.regions.append(kakariko_watchtower_upper_door)

    kakariko_watchtower = Region(RoomName.KAKARIKO_WATCHTOWER, player, world)
    regions[RoomName.KAKARIKO_WATCHTOWER] = kakariko_watchtower
    world.regions.append(kakariko_watchtower)

    kakariko_watchtower.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_WATCHTOWER_CHEST,
        kakariko_watchtower,
        LOCATION_TABLE[CheckName.KAKARIKO_WATCHTOWER_CHEST]
      )
    )

    kakariko_graveyard = Region(RoomName.KAKARIKO_GRAVEYARD, player, world)
    regions[RoomName.KAKARIKO_GRAVEYARD] = kakariko_graveyard
    world.regions.append(kakariko_graveyard)

    kakariko_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GRAVEYARD_LANTERN_CHEST,
        kakariko_graveyard,
        LOCATION_TABLE[CheckName.KAKARIKO_GRAVEYARD_LANTERN_CHEST]
      )
    )

    kakariko_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.GIFT_FROM_RALIS,
        kakariko_graveyard,
        LOCATION_TABLE[CheckName.GIFT_FROM_RALIS]
      )
    )

    kakariko_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.RUTELAS_BLESSING,
        kakariko_graveyard,
        LOCATION_TABLE[CheckName.RUTELAS_BLESSING]
      )
    )

    kakariko_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GRAVEYARD_MALE_ANT,
        kakariko_graveyard,
        LOCATION_TABLE[CheckName.KAKARIKO_GRAVEYARD_MALE_ANT]
      )
    )

    kakariko_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GRAVEYARD_GRAVE_POE,
        kakariko_graveyard,
        LOCATION_TABLE[CheckName.KAKARIKO_GRAVEYARD_GRAVE_POE]
      )
    )

    kakariko_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GRAVEYARD_OPEN_POE,
        kakariko_graveyard,
        LOCATION_TABLE[CheckName.KAKARIKO_GRAVEYARD_OPEN_POE]
      )
    )

    kakariko_graveyard.locations.append(
    TPLocation(
        player,
        CheckName.KAKARIKO_GRAVEYARD_GOLDEN_WOLF,
        kakariko_graveyard,
        LOCATION_TABLE[CheckName.KAKARIKO_GRAVEYARD_GOLDEN_WOLF]
      )
    )

    south_faron_woods = Region(RoomName.SOUTH_FARON_WOODS, player, world)
    regions[RoomName.SOUTH_FARON_WOODS] = south_faron_woods
    world.regions.append(south_faron_woods)

    south_faron_woods.locations.append(
    TPLocation(
        player,
        CheckName.CORO_BOTTLE,
        south_faron_woods,
        LOCATION_TABLE[CheckName.CORO_BOTTLE]
      )
    )

    south_faron_woods_behind_gate = Region(RoomName.SOUTH_FARON_WOODS_BEHIND_GATE, player, world)
    regions[RoomName.SOUTH_FARON_WOODS_BEHIND_GATE] = south_faron_woods_behind_gate
    world.regions.append(south_faron_woods_behind_gate)

    south_faron_woods_coros_ledge = Region(RoomName.SOUTH_FARON_WOODS_COROS_LEDGE, player, world)
    regions[RoomName.SOUTH_FARON_WOODS_COROS_LEDGE] = south_faron_woods_coros_ledge
    world.regions.append(south_faron_woods_coros_ledge)

    south_faron_woods_owl_statue_area = Region(RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA, player, world)
    regions[RoomName.SOUTH_FARON_WOODS_OWL_STATUE_AREA] = south_faron_woods_owl_statue_area
    world.regions.append(south_faron_woods_owl_statue_area)

    south_faron_woods_owl_statue_area.locations.append(
    TPLocation(
        player,
        CheckName.FARON_WOODS_OWL_STATUE_SKY_CHARACTER,
        south_faron_woods_owl_statue_area,
        LOCATION_TABLE[CheckName.FARON_WOODS_OWL_STATUE_SKY_CHARACTER]
      )
    )

    south_faron_woods_above_owl_statue = Region(RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE, player, world)
    regions[RoomName.SOUTH_FARON_WOODS_ABOVE_OWL_STATUE] = south_faron_woods_above_owl_statue
    world.regions.append(south_faron_woods_above_owl_statue)

    faron_woods_coros_house_lower = Region(RoomName.FARON_WOODS_COROS_HOUSE_LOWER, player, world)
    regions[RoomName.FARON_WOODS_COROS_HOUSE_LOWER] = faron_woods_coros_house_lower
    world.regions.append(faron_woods_coros_house_lower)

    faron_woods_coros_house_upper = Region(RoomName.FARON_WOODS_COROS_HOUSE_UPPER, player, world)
    regions[RoomName.FARON_WOODS_COROS_HOUSE_UPPER] = faron_woods_coros_house_upper
    world.regions.append(faron_woods_coros_house_upper)

    faron_woods_cave_southern_entrance = Region(RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE, player, world)
    regions[RoomName.FARON_WOODS_CAVE_SOUTHERN_ENTRANCE] = faron_woods_cave_southern_entrance
    world.regions.append(faron_woods_cave_southern_entrance)

    faron_woods_cave = Region(RoomName.FARON_WOODS_CAVE, player, world)
    regions[RoomName.FARON_WOODS_CAVE] = faron_woods_cave
    world.regions.append(faron_woods_cave)

    faron_woods_cave.locations.append(
    TPLocation(
        player,
        CheckName.SOUTH_FARON_CAVE_CHEST,
        faron_woods_cave,
        LOCATION_TABLE[CheckName.SOUTH_FARON_CAVE_CHEST]
      )
    )

    mist_area_near_faron_woods_cave = Region(RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE, player, world)
    regions[RoomName.MIST_AREA_NEAR_FARON_WOODS_CAVE] = mist_area_near_faron_woods_cave
    world.regions.append(mist_area_near_faron_woods_cave)

    mist_area_inside_mist = Region(RoomName.MIST_AREA_INSIDE_MIST, player, world)
    regions[RoomName.MIST_AREA_INSIDE_MIST] = mist_area_inside_mist
    world.regions.append(mist_area_inside_mist)

    mist_area_inside_mist.locations.append(
    TPLocation(
        player,
        CheckName.FARON_MIST_STUMP_CHEST,
        mist_area_inside_mist,
        LOCATION_TABLE[CheckName.FARON_MIST_STUMP_CHEST]
      )
    )

    mist_area_inside_mist.locations.append(
    TPLocation(
        player,
        CheckName.FARON_MIST_NORTH_CHEST,
        mist_area_inside_mist,
        LOCATION_TABLE[CheckName.FARON_MIST_NORTH_CHEST]
      )
    )

    mist_area_inside_mist.locations.append(
    TPLocation(
        player,
        CheckName.FARON_MIST_SOUTH_CHEST,
        mist_area_inside_mist,
        LOCATION_TABLE[CheckName.FARON_MIST_SOUTH_CHEST]
      )
    )

    mist_area_under_owl_statue_chest = Region(RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST, player, world)
    regions[RoomName.MIST_AREA_UNDER_OWL_STATUE_CHEST] = mist_area_under_owl_statue_chest
    world.regions.append(mist_area_under_owl_statue_chest)

    mist_area_near_owl_statue_chest = Region(RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST, player, world)
    regions[RoomName.MIST_AREA_NEAR_OWL_STATUE_CHEST] = mist_area_near_owl_statue_chest
    world.regions.append(mist_area_near_owl_statue_chest)

    mist_area_near_owl_statue_chest.locations.append(
    TPLocation(
        player,
        CheckName.FARON_WOODS_OWL_STATUE_CHEST,
        mist_area_near_owl_statue_chest,
        LOCATION_TABLE[CheckName.FARON_WOODS_OWL_STATUE_CHEST]
      )
    )

    mist_area_center_stump = Region(RoomName.MIST_AREA_CENTER_STUMP, player, world)
    regions[RoomName.MIST_AREA_CENTER_STUMP] = mist_area_center_stump
    world.regions.append(mist_area_center_stump)

    mist_area_center_stump.locations.append(
    TPLocation(
        player,
        CheckName.FARON_MIST_POE,
        mist_area_center_stump,
        LOCATION_TABLE[CheckName.FARON_MIST_POE]
      )
    )

    mist_area_outside_faron_mist_cave = Region(RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE, player, world)
    regions[RoomName.MIST_AREA_OUTSIDE_FARON_MIST_CAVE] = mist_area_outside_faron_mist_cave
    world.regions.append(mist_area_outside_faron_mist_cave)

    mist_area_near_north_faron_woods = Region(RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS, player, world)
    regions[RoomName.MIST_AREA_NEAR_NORTH_FARON_WOODS] = mist_area_near_north_faron_woods
    world.regions.append(mist_area_near_north_faron_woods)

    faron_woods_cave_northern_entrance = Region(RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE, player, world)
    regions[RoomName.FARON_WOODS_CAVE_NORTHERN_ENTRANCE] = faron_woods_cave_northern_entrance
    world.regions.append(faron_woods_cave_northern_entrance)

    mist_area_faron_mist_cave = Region(RoomName.MIST_AREA_FARON_MIST_CAVE, player, world)
    regions[RoomName.MIST_AREA_FARON_MIST_CAVE] = mist_area_faron_mist_cave
    world.regions.append(mist_area_faron_mist_cave)

    mist_area_faron_mist_cave.locations.append(
    TPLocation(
        player,
        CheckName.FARON_MIST_CAVE_OPEN_CHEST,
        mist_area_faron_mist_cave,
        LOCATION_TABLE[CheckName.FARON_MIST_CAVE_OPEN_CHEST]
      )
    )

    mist_area_faron_mist_cave.locations.append(
    TPLocation(
        player,
        CheckName.FARON_MIST_CAVE_LANTERN_CHEST,
        mist_area_faron_mist_cave,
        LOCATION_TABLE[CheckName.FARON_MIST_CAVE_LANTERN_CHEST]
      )
    )

    north_faron_woods = Region(RoomName.NORTH_FARON_WOODS, player, world)
    regions[RoomName.NORTH_FARON_WOODS] = north_faron_woods
    world.regions.append(north_faron_woods)

    north_faron_woods.locations.append(
    TPLocation(
        player,
        CheckName.NORTH_FARON_WOODS_DEKU_BABA_CHEST,
        north_faron_woods,
        LOCATION_TABLE[CheckName.NORTH_FARON_WOODS_DEKU_BABA_CHEST]
      )
    )

    north_faron_woods.locations.append(
    TPLocation(
        player,
        CheckName.FARON_WOODS_GOLDEN_WOLF,
        north_faron_woods,
        LOCATION_TABLE[CheckName.FARON_WOODS_GOLDEN_WOLF]
      )
    )

    faron_field = Region(RoomName.FARON_FIELD, player, world)
    regions[RoomName.FARON_FIELD] = faron_field
    world.regions.append(faron_field)

    faron_field.locations.append(
    TPLocation(
        player,
        CheckName.FARON_FIELD_BRIDGE_CHEST,
        faron_field,
        LOCATION_TABLE[CheckName.FARON_FIELD_BRIDGE_CHEST]
      )
    )

    faron_field.locations.append(
    TPLocation(
        player,
        CheckName.FARON_FIELD_TREE_HEART_PIECE,
        faron_field,
        LOCATION_TABLE[CheckName.FARON_FIELD_TREE_HEART_PIECE]
      )
    )

    faron_field.locations.append(
    TPLocation(
        player,
        CheckName.FARON_FIELD_MALE_BEETLE,
        faron_field,
        LOCATION_TABLE[CheckName.FARON_FIELD_MALE_BEETLE]
      )
    )

    faron_field.locations.append(
    TPLocation(
        player,
        CheckName.FARON_FIELD_FEMALE_BEETLE,
        faron_field,
        LOCATION_TABLE[CheckName.FARON_FIELD_FEMALE_BEETLE]
      )
    )

    faron_field.locations.append(
    TPLocation(
        player,
        CheckName.FARON_FIELD_POE,
        faron_field,
        LOCATION_TABLE[CheckName.FARON_FIELD_POE]
      )
    )

    faron_field_behind_boulder = Region(RoomName.FARON_FIELD_BEHIND_BOULDER, player, world)
    regions[RoomName.FARON_FIELD_BEHIND_BOULDER] = faron_field_behind_boulder
    world.regions.append(faron_field_behind_boulder)

    faron_field_corner_grotto = Region(RoomName.FARON_FIELD_CORNER_GROTTO, player, world)
    regions[RoomName.FARON_FIELD_CORNER_GROTTO] = faron_field_corner_grotto
    world.regions.append(faron_field_corner_grotto)

    faron_field_corner_grotto.locations.append(
    TPLocation(
        player,
        CheckName.FARON_FIELD_CORNER_GROTTO_RIGHT_CHEST,
        faron_field_corner_grotto,
        LOCATION_TABLE[CheckName.FARON_FIELD_CORNER_GROTTO_RIGHT_CHEST]
      )
    )

    faron_field_corner_grotto.locations.append(
    TPLocation(
        player,
        CheckName.FARON_FIELD_CORNER_GROTTO_LEFT_CHEST,
        faron_field_corner_grotto,
        LOCATION_TABLE[CheckName.FARON_FIELD_CORNER_GROTTO_LEFT_CHEST]
      )
    )

    faron_field_corner_grotto.locations.append(
    TPLocation(
        player,
        CheckName.FARON_FIELD_CORNER_GROTTO_REAR_CHEST,
        faron_field_corner_grotto,
        LOCATION_TABLE[CheckName.FARON_FIELD_CORNER_GROTTO_REAR_CHEST]
      )
    )

    faron_field_fishing_grotto = Region(RoomName.FARON_FIELD_FISHING_GROTTO, player, world)
    regions[RoomName.FARON_FIELD_FISHING_GROTTO] = faron_field_fishing_grotto
    world.regions.append(faron_field_fishing_grotto)

    lost_woods = Region(RoomName.LOST_WOODS, player, world)
    regions[RoomName.LOST_WOODS] = lost_woods
    world.regions.append(lost_woods)

    lost_woods.locations.append(
    TPLocation(
        player,
        CheckName.LOST_WOODS_LANTERN_CHEST,
        lost_woods,
        LOCATION_TABLE[CheckName.LOST_WOODS_LANTERN_CHEST]
      )
    )

    lost_woods.locations.append(
    TPLocation(
        player,
        CheckName.LOST_WOODS_WATERFALL_POE,
        lost_woods,
        LOCATION_TABLE[CheckName.LOST_WOODS_WATERFALL_POE]
      )
    )

    lost_woods_lower_battle_arena = Region(RoomName.LOST_WOODS_LOWER_BATTLE_ARENA, player, world)
    regions[RoomName.LOST_WOODS_LOWER_BATTLE_ARENA] = lost_woods_lower_battle_arena
    world.regions.append(lost_woods_lower_battle_arena)

    lost_woods_lower_battle_arena.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_SPINNER_CHEST,
        lost_woods_lower_battle_arena,
        LOCATION_TABLE[CheckName.SACRED_GROVE_SPINNER_CHEST]
      )
    )

    lost_woods_lower_battle_arena.locations.append(
    TPLocation(
        player,
        CheckName.LOST_WOODS_BOULDER_POE,
        lost_woods_lower_battle_arena,
        LOCATION_TABLE[CheckName.LOST_WOODS_BOULDER_POE]
      )
    )

    lost_woods_upper_battle_arena = Region(RoomName.LOST_WOODS_UPPER_BATTLE_ARENA, player, world)
    regions[RoomName.LOST_WOODS_UPPER_BATTLE_ARENA] = lost_woods_upper_battle_arena
    world.regions.append(lost_woods_upper_battle_arena)

    lost_woods_baba_serpent_grotto = Region(RoomName.LOST_WOODS_BABA_SERPENT_GROTTO, player, world)
    regions[RoomName.LOST_WOODS_BABA_SERPENT_GROTTO] = lost_woods_baba_serpent_grotto
    world.regions.append(lost_woods_baba_serpent_grotto)

    lost_woods_baba_serpent_grotto.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_BABA_SERPENT_GROTTO_CHEST,
        lost_woods_baba_serpent_grotto,
        LOCATION_TABLE[CheckName.SACRED_GROVE_BABA_SERPENT_GROTTO_CHEST]
      )
    )

    sacred_grove_before_block = Region(RoomName.SACRED_GROVE_BEFORE_BLOCK, player, world)
    regions[RoomName.SACRED_GROVE_BEFORE_BLOCK] = sacred_grove_before_block
    world.regions.append(sacred_grove_before_block)

    sacred_grove_upper = Region(RoomName.SACRED_GROVE_UPPER, player, world)
    regions[RoomName.SACRED_GROVE_UPPER] = sacred_grove_upper
    world.regions.append(sacred_grove_upper)

    sacred_grove_lower = Region(RoomName.SACRED_GROVE_LOWER, player, world)
    regions[RoomName.SACRED_GROVE_LOWER] = sacred_grove_lower
    world.regions.append(sacred_grove_lower)

    sacred_grove_lower.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_MALE_SNAIL,
        sacred_grove_lower,
        LOCATION_TABLE[CheckName.SACRED_GROVE_MALE_SNAIL]
      )
    )

    sacred_grove_lower.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_MASTER_SWORD_POE,
        sacred_grove_lower,
        LOCATION_TABLE[CheckName.SACRED_GROVE_MASTER_SWORD_POE]
      )
    )

    sacred_grove_lower.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_PEDESTAL_MASTER_SWORD,
        sacred_grove_lower,
        LOCATION_TABLE[CheckName.SACRED_GROVE_PEDESTAL_MASTER_SWORD]
      )
    )

    sacred_grove_lower.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_PEDESTAL_SHADOW_CRYSTAL,
        sacred_grove_lower,
        LOCATION_TABLE[CheckName.SACRED_GROVE_PEDESTAL_SHADOW_CRYSTAL]
      )
    )

    sacred_grove_past = Region(RoomName.SACRED_GROVE_PAST, player, world)
    regions[RoomName.SACRED_GROVE_PAST] = sacred_grove_past
    world.regions.append(sacred_grove_past)

    sacred_grove_past.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_PAST_OWL_STATUE_CHEST,
        sacred_grove_past,
        LOCATION_TABLE[CheckName.SACRED_GROVE_PAST_OWL_STATUE_CHEST]
      )
    )

    sacred_grove_past.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_FEMALE_SNAIL,
        sacred_grove_past,
        LOCATION_TABLE[CheckName.SACRED_GROVE_FEMALE_SNAIL]
      )
    )

    sacred_grove_past.locations.append(
    TPLocation(
        player,
        CheckName.SACRED_GROVE_TEMPLE_OF_TIME_OWL_STATUE_POE,
        sacred_grove_past,
        LOCATION_TABLE[CheckName.SACRED_GROVE_TEMPLE_OF_TIME_OWL_STATUE_POE]
      )
    )

    sacred_grove_past_behind_window = Region(RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW, player, world)
    regions[RoomName.SACRED_GROVE_PAST_BEHIND_WINDOW] = sacred_grove_past_behind_window
    world.regions.append(sacred_grove_past_behind_window)

    gerudo_desert_cave_of_ordeals_floors_01_11 = Region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11, player, world)
    regions[RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_01_11] = gerudo_desert_cave_of_ordeals_floors_01_11
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_01_11)

    gerudo_desert_cave_of_ordeals_floors_12_21 = Region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_12_21, player, world)
    regions[RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_12_21] = gerudo_desert_cave_of_ordeals_floors_12_21
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_12_21)

    gerudo_desert_cave_of_ordeals_floors_12_21.locations.append(
    TPLocation(
        player,
        CheckName.CAVE_OF_ORDEALS_FLOOR_17_POE,
        gerudo_desert_cave_of_ordeals_floors_12_21,
        LOCATION_TABLE[CheckName.CAVE_OF_ORDEALS_FLOOR_17_POE]
      )
    )

    gerudo_desert_cave_of_ordeals_floors_22_31 = Region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_22_31, player, world)
    regions[RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_22_31] = gerudo_desert_cave_of_ordeals_floors_22_31
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_22_31)

    gerudo_desert_cave_of_ordeals_floors_32_41 = Region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_32_41, player, world)
    regions[RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_32_41] = gerudo_desert_cave_of_ordeals_floors_32_41
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_32_41)

    gerudo_desert_cave_of_ordeals_floors_32_41.locations.append(
    TPLocation(
        player,
        CheckName.CAVE_OF_ORDEALS_FLOOR_33_POE,
        gerudo_desert_cave_of_ordeals_floors_32_41,
        LOCATION_TABLE[CheckName.CAVE_OF_ORDEALS_FLOOR_33_POE]
      )
    )

    gerudo_desert_cave_of_ordeals_floors_42_50 = Region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_42_50, player, world)
    regions[RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_FLOORS_42_50] = gerudo_desert_cave_of_ordeals_floors_42_50
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_42_50)

    gerudo_desert_cave_of_ordeals_floors_42_50.locations.append(
    TPLocation(
        player,
        CheckName.CAVE_OF_ORDEALS_FLOOR_44_POE,
        gerudo_desert_cave_of_ordeals_floors_42_50,
        LOCATION_TABLE[CheckName.CAVE_OF_ORDEALS_FLOOR_44_POE]
      )
    )

    gerudo_desert_cave_of_ordeals_floors_42_50.locations.append(
    TPLocation(
        player,
        CheckName.CAVE_OF_ORDEALS_GREAT_FAIRY_REWARD,
        gerudo_desert_cave_of_ordeals_floors_42_50,
        LOCATION_TABLE[CheckName.CAVE_OF_ORDEALS_GREAT_FAIRY_REWARD]
      )
    )

    gerudo_desert = Region(RoomName.GERUDO_DESERT, player, world)
    regions[RoomName.GERUDO_DESERT] = gerudo_desert
    world.regions.append(gerudo_desert)

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_PEAHAT_LEDGE_CHEST,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_PEAHAT_LEDGE_CHEST]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_EAST_CANYON_CHEST,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_EAST_CANYON_CHEST]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_LONE_SMALL_CHEST,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_LONE_SMALL_CHEST]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_WEST_CANYON_CHEST,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_WEST_CANYON_CHEST]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_SOUTH_CHEST_BEHIND_WOODEN_GATES,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_SOUTH_CHEST_BEHIND_WOODEN_GATES]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_OWL_STATUE_CHEST,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_OWL_STATUE_CHEST]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_OWL_STATUE_SKY_CHARACTER,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_OWL_STATUE_SKY_CHARACTER]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_MALE_DAYFLY,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_MALE_DAYFLY]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_FEMALE_DAYFLY,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_FEMALE_DAYFLY]
      )
    )

    gerudo_desert.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_EAST_POE,
        gerudo_desert,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_EAST_POE]
      )
    )

    gerudo_desert_cave_of_ordeals_plateau = Region(RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU, player, world)
    regions[RoomName.GERUDO_DESERT_CAVE_OF_ORDEALS_PLATEAU] = gerudo_desert_cave_of_ordeals_plateau
    world.regions.append(gerudo_desert_cave_of_ordeals_plateau)

    gerudo_desert_cave_of_ordeals_plateau.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_POE_ABOVE_CAVE_OF_ORDEALS,
        gerudo_desert_cave_of_ordeals_plateau,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_POE_ABOVE_CAVE_OF_ORDEALS]
      )
    )

    gerudo_desert_basin = Region(RoomName.GERUDO_DESERT_BASIN, player, world)
    regions[RoomName.GERUDO_DESERT_BASIN] = gerudo_desert_basin
    world.regions.append(gerudo_desert_basin)

    gerudo_desert_basin.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_NORTHEAST_CHEST_BEHIND_GATES,
        gerudo_desert_basin,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_NORTHEAST_CHEST_BEHIND_GATES]
      )
    )

    gerudo_desert_basin.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_CAMPFIRE_NORTH_CHEST,
        gerudo_desert_basin,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_CAMPFIRE_NORTH_CHEST]
      )
    )

    gerudo_desert_basin.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_CAMPFIRE_EAST_CHEST,
        gerudo_desert_basin,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_CAMPFIRE_EAST_CHEST]
      )
    )

    gerudo_desert_basin.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_CAMPFIRE_WEST_CHEST,
        gerudo_desert_basin,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_CAMPFIRE_WEST_CHEST]
      )
    )

    gerudo_desert_basin.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_NORTHWEST_CHEST_BEHIND_GATES,
        gerudo_desert_basin,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_NORTHWEST_CHEST_BEHIND_GATES]
      )
    )

    gerudo_desert_north_east_ledge = Region(RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE, player, world)
    regions[RoomName.GERUDO_DESERT_NORTH_EAST_LEDGE] = gerudo_desert_north_east_ledge
    world.regions.append(gerudo_desert_north_east_ledge)

    gerudo_desert_north_east_ledge.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_NORTH_PEAHAT_POE,
        gerudo_desert_north_east_ledge,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_NORTH_PEAHAT_POE]
      )
    )

    gerudo_desert_outside_bulblin_camp = Region(RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP, player, world)
    regions[RoomName.GERUDO_DESERT_OUTSIDE_BULBLIN_CAMP] = gerudo_desert_outside_bulblin_camp
    world.regions.append(gerudo_desert_outside_bulblin_camp)

    gerudo_desert_outside_bulblin_camp.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_NORTH_SMALL_CHEST_BEFORE_BULBLIN_CAMP,
        gerudo_desert_outside_bulblin_camp,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_NORTH_SMALL_CHEST_BEFORE_BULBLIN_CAMP]
      )
    )

    gerudo_desert_outside_bulblin_camp.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_BULBLIN_CAMP_POE,
        gerudo_desert_outside_bulblin_camp,
        LOCATION_TABLE[CheckName.OUTSIDE_BULBLIN_CAMP_POE]
      )
    )

    gerudo_desert_outside_bulblin_camp.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_GOLDEN_WOLF,
        gerudo_desert_outside_bulblin_camp,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_GOLDEN_WOLF]
      )
    )

    gerudo_desert_skulltula_grotto = Region(RoomName.GERUDO_DESERT_SKULLTULA_GROTTO, player, world)
    regions[RoomName.GERUDO_DESERT_SKULLTULA_GROTTO] = gerudo_desert_skulltula_grotto
    world.regions.append(gerudo_desert_skulltula_grotto)

    gerudo_desert_skulltula_grotto.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_SKULLTULA_GROTTO_CHEST,
        gerudo_desert_skulltula_grotto,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_SKULLTULA_GROTTO_CHEST]
      )
    )

    gerudo_desert_chu_grotto = Region(RoomName.GERUDO_DESERT_CHU_GROTTO, player, world)
    regions[RoomName.GERUDO_DESERT_CHU_GROTTO] = gerudo_desert_chu_grotto
    world.regions.append(gerudo_desert_chu_grotto)

    gerudo_desert_rock_grotto = Region(RoomName.GERUDO_DESERT_ROCK_GROTTO, player, world)
    regions[RoomName.GERUDO_DESERT_ROCK_GROTTO] = gerudo_desert_rock_grotto
    world.regions.append(gerudo_desert_rock_grotto)

    gerudo_desert_rock_grotto.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_ROCK_GROTTO_LANTERN_CHEST,
        gerudo_desert_rock_grotto,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_ROCK_GROTTO_LANTERN_CHEST]
      )
    )

    gerudo_desert_rock_grotto.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_ROCK_GROTTO_FIRST_POE,
        gerudo_desert_rock_grotto,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_ROCK_GROTTO_FIRST_POE]
      )
    )

    gerudo_desert_rock_grotto.locations.append(
    TPLocation(
        player,
        CheckName.GERUDO_DESERT_ROCK_GROTTO_SECOND_POE,
        gerudo_desert_rock_grotto,
        LOCATION_TABLE[CheckName.GERUDO_DESERT_ROCK_GROTTO_SECOND_POE]
      )
    )

    bulblin_camp = Region(RoomName.BULBLIN_CAMP, player, world)
    regions[RoomName.BULBLIN_CAMP] = bulblin_camp
    world.regions.append(bulblin_camp)

    bulblin_camp.locations.append(
    TPLocation(
        player,
        CheckName.BULBLIN_CAMP_FIRST_CHEST_UNDER_TOWER_AT_ENTRANCE,
        bulblin_camp,
        LOCATION_TABLE[CheckName.BULBLIN_CAMP_FIRST_CHEST_UNDER_TOWER_AT_ENTRANCE]
      )
    )

    bulblin_camp.locations.append(
    TPLocation(
        player,
        CheckName.BULBLIN_CAMP_SMALL_CHEST_IN_BACK_OF_CAMP,
        bulblin_camp,
        LOCATION_TABLE[CheckName.BULBLIN_CAMP_SMALL_CHEST_IN_BACK_OF_CAMP]
      )
    )

    bulblin_camp.locations.append(
    TPLocation(
        player,
        CheckName.BULBLIN_CAMP_ROASTED_BOAR,
        bulblin_camp,
        LOCATION_TABLE[CheckName.BULBLIN_CAMP_ROASTED_BOAR]
      )
    )

    bulblin_camp.locations.append(
    TPLocation(
        player,
        CheckName.BULBLIN_CAMP_POE,
        bulblin_camp,
        LOCATION_TABLE[CheckName.BULBLIN_CAMP_POE]
      )
    )

    bulblin_camp.locations.append(
    TPLocation(
        player,
        CheckName.BULBLIN_GUARD_KEY,
        bulblin_camp,
        LOCATION_TABLE[CheckName.BULBLIN_GUARD_KEY]
      )
    )

    outside_arbiters_grounds = Region(RoomName.OUTSIDE_ARBITERS_GROUNDS, player, world)
    regions[RoomName.OUTSIDE_ARBITERS_GROUNDS] = outside_arbiters_grounds
    world.regions.append(outside_arbiters_grounds)

    outside_arbiters_grounds.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_ARBITERS_GROUNDS_LANTERN_CHEST,
        outside_arbiters_grounds,
        LOCATION_TABLE[CheckName.OUTSIDE_ARBITERS_GROUNDS_LANTERN_CHEST]
      )
    )

    outside_arbiters_grounds.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_ARBITERS_GROUNDS_POE,
        outside_arbiters_grounds,
        LOCATION_TABLE[CheckName.OUTSIDE_ARBITERS_GROUNDS_POE]
      )
    )

    mirror_chamber_lower = Region(RoomName.MIRROR_CHAMBER_LOWER, player, world)
    regions[RoomName.MIRROR_CHAMBER_LOWER] = mirror_chamber_lower
    world.regions.append(mirror_chamber_lower)

    mirror_chamber_upper = Region(RoomName.MIRROR_CHAMBER_UPPER, player, world)
    regions[RoomName.MIRROR_CHAMBER_UPPER] = mirror_chamber_upper
    world.regions.append(mirror_chamber_upper)

    mirror_chamber_portal = Region(RoomName.MIRROR_CHAMBER_PORTAL, player, world)
    regions[RoomName.MIRROR_CHAMBER_PORTAL] = mirror_chamber_portal
    world.regions.append(mirror_chamber_portal)

    castle_town_west = Region(RoomName.CASTLE_TOWN_WEST, player, world)
    regions[RoomName.CASTLE_TOWN_WEST] = castle_town_west
    world.regions.append(castle_town_west)

    castle_town_west.locations.append(
    TPLocation(
        player,
        CheckName.CHARLO_DONATION_BLESSING,
        castle_town_west,
        LOCATION_TABLE[CheckName.CHARLO_DONATION_BLESSING]
      )
    )

    castle_town_star_game = Region(RoomName.CASTLE_TOWN_STAR_GAME, player, world)
    regions[RoomName.CASTLE_TOWN_STAR_GAME] = castle_town_star_game
    world.regions.append(castle_town_star_game)

    castle_town_star_game.locations.append(
    TPLocation(
        player,
        CheckName.STAR_PRIZE_1,
        castle_town_star_game,
        LOCATION_TABLE[CheckName.STAR_PRIZE_1]
      )
    )

    castle_town_star_game.locations.append(
    TPLocation(
        player,
        CheckName.STAR_PRIZE_2,
        castle_town_star_game,
        LOCATION_TABLE[CheckName.STAR_PRIZE_2]
      )
    )

    castle_town_center = Region(RoomName.CASTLE_TOWN_CENTER, player, world)
    regions[RoomName.CASTLE_TOWN_CENTER] = castle_town_center
    world.regions.append(castle_town_center)

    castle_town_goron_house_left_door = Region(RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR, player, world)
    regions[RoomName.CASTLE_TOWN_GORON_HOUSE_LEFT_DOOR] = castle_town_goron_house_left_door
    world.regions.append(castle_town_goron_house_left_door)

    castle_town_goron_house_right_door = Region(RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR, player, world)
    regions[RoomName.CASTLE_TOWN_GORON_HOUSE_RIGHT_DOOR] = castle_town_goron_house_right_door
    world.regions.append(castle_town_goron_house_right_door)

    castle_town_goron_house = Region(RoomName.CASTLE_TOWN_GORON_HOUSE, player, world)
    regions[RoomName.CASTLE_TOWN_GORON_HOUSE] = castle_town_goron_house
    world.regions.append(castle_town_goron_house)

    castle_town_malo_mart = Region(RoomName.CASTLE_TOWN_MALO_MART, player, world)
    regions[RoomName.CASTLE_TOWN_MALO_MART] = castle_town_malo_mart
    world.regions.append(castle_town_malo_mart)

    castle_town_malo_mart.locations.append(
    TPLocation(
        player,
        CheckName.CASTLE_TOWN_MALO_MART_MAGIC_ARMOR,
        castle_town_malo_mart,
        LOCATION_TABLE[CheckName.CASTLE_TOWN_MALO_MART_MAGIC_ARMOR]
      )
    )

    castle_town_north = Region(RoomName.CASTLE_TOWN_NORTH, player, world)
    regions[RoomName.CASTLE_TOWN_NORTH] = castle_town_north
    world.regions.append(castle_town_north)

    castle_town_north_behind_first_door = Region(RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR, player, world)
    regions[RoomName.CASTLE_TOWN_NORTH_BEHIND_FIRST_DOOR] = castle_town_north_behind_first_door
    world.regions.append(castle_town_north_behind_first_door)

    castle_town_north_behind_first_door.locations.append(
    TPLocation(
        player,
        CheckName.NORTH_CASTLE_TOWN_GOLDEN_WOLF,
        castle_town_north_behind_first_door,
        LOCATION_TABLE[CheckName.NORTH_CASTLE_TOWN_GOLDEN_WOLF]
      )
    )

    castle_town_north_inside_barrier = Region(RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER, player, world)
    regions[RoomName.CASTLE_TOWN_NORTH_INSIDE_BARRIER] = castle_town_north_inside_barrier
    world.regions.append(castle_town_north_inside_barrier)

    castle_town_east = Region(RoomName.CASTLE_TOWN_EAST, player, world)
    regions[RoomName.CASTLE_TOWN_EAST] = castle_town_east
    world.regions.append(castle_town_east)

    castle_town_doctors_office_balcony = Region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY, player, world)
    regions[RoomName.CASTLE_TOWN_DOCTORS_OFFICE_BALCONY] = castle_town_doctors_office_balcony
    world.regions.append(castle_town_doctors_office_balcony)

    castle_town_doctors_office_balcony.locations.append(
    TPLocation(
        player,
        CheckName.DOCTORS_OFFICE_BALCONY_CHEST,
        castle_town_doctors_office_balcony,
        LOCATION_TABLE[CheckName.DOCTORS_OFFICE_BALCONY_CHEST]
      )
    )

    castle_town_doctors_office_left_door = Region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR, player, world)
    regions[RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LEFT_DOOR] = castle_town_doctors_office_left_door
    world.regions.append(castle_town_doctors_office_left_door)

    castle_town_doctors_office_right_door = Region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR, player, world)
    regions[RoomName.CASTLE_TOWN_DOCTORS_OFFICE_RIGHT_DOOR] = castle_town_doctors_office_right_door
    world.regions.append(castle_town_doctors_office_right_door)

    castle_town_doctors_office_entrance = Region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE, player, world)
    regions[RoomName.CASTLE_TOWN_DOCTORS_OFFICE_ENTRANCE] = castle_town_doctors_office_entrance
    world.regions.append(castle_town_doctors_office_entrance)

    castle_town_doctors_office_lower = Region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER, player, world)
    regions[RoomName.CASTLE_TOWN_DOCTORS_OFFICE_LOWER] = castle_town_doctors_office_lower
    world.regions.append(castle_town_doctors_office_lower)

    castle_town_doctors_office_upper = Region(RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER, player, world)
    regions[RoomName.CASTLE_TOWN_DOCTORS_OFFICE_UPPER] = castle_town_doctors_office_upper
    world.regions.append(castle_town_doctors_office_upper)

    castle_town_south = Region(RoomName.CASTLE_TOWN_SOUTH, player, world)
    regions[RoomName.CASTLE_TOWN_SOUTH] = castle_town_south
    world.regions.append(castle_town_south)

    castle_town_agithas_house = Region(RoomName.CASTLE_TOWN_AGITHAS_HOUSE, player, world)
    regions[RoomName.CASTLE_TOWN_AGITHAS_HOUSE] = castle_town_agithas_house
    world.regions.append(castle_town_agithas_house)

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_ANT_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_ANT_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_BEETLE_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_BEETLE_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_BUTTERFLY_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_BUTTERFLY_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_DAYFLY_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_DAYFLY_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_DRAGONFLY_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_DRAGONFLY_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_GRASSHOPPER_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_GRASSHOPPER_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_LADYBUG_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_LADYBUG_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_MANTIS_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_MANTIS_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_PHASMID_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_PHASMID_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_PILL_BUG_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_PILL_BUG_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_SNAIL_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_SNAIL_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_FEMALE_STAG_BEETLE_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_FEMALE_STAG_BEETLE_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_ANT_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_ANT_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_BEETLE_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_BEETLE_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_BUTTERFLY_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_BUTTERFLY_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_DAYFLY_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_DAYFLY_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_DRAGONFLY_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_DRAGONFLY_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_GRASSHOPPER_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_GRASSHOPPER_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_LADYBUG_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_LADYBUG_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_MANTIS_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_MANTIS_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_PHASMID_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_PHASMID_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_PILL_BUG_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_PILL_BUG_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_SNAIL_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_SNAIL_REWARD]
      )
    )

    castle_town_agithas_house.locations.append(
    TPLocation(
        player,
        CheckName.AGITHA_MALE_STAG_BEETLE_REWARD,
        castle_town_agithas_house,
        LOCATION_TABLE[CheckName.AGITHA_MALE_STAG_BEETLE_REWARD]
      )
    )

    castle_town_seer_house = Region(RoomName.CASTLE_TOWN_SEER_HOUSE, player, world)
    regions[RoomName.CASTLE_TOWN_SEER_HOUSE] = castle_town_seer_house
    world.regions.append(castle_town_seer_house)

    castle_town_jovanis_house = Region(RoomName.CASTLE_TOWN_JOVANIS_HOUSE, player, world)
    regions[RoomName.CASTLE_TOWN_JOVANIS_HOUSE] = castle_town_jovanis_house
    world.regions.append(castle_town_jovanis_house)

    castle_town_jovanis_house.locations.append(
    TPLocation(
        player,
        CheckName.JOVANI_HOUSE_POE,
        castle_town_jovanis_house,
        LOCATION_TABLE[CheckName.JOVANI_HOUSE_POE]
      )
    )

    castle_town_jovanis_house.locations.append(
    TPLocation(
        player,
        CheckName.JOVANI_20_POE_SOUL_REWARD,
        castle_town_jovanis_house,
        LOCATION_TABLE[CheckName.JOVANI_20_POE_SOUL_REWARD]
      )
    )

    castle_town_jovanis_house.locations.append(
    TPLocation(
        player,
        CheckName.JOVANI_60_POE_SOUL_REWARD,
        castle_town_jovanis_house,
        LOCATION_TABLE[CheckName.JOVANI_60_POE_SOUL_REWARD]
      )
    )

    castle_town_telmas_bar = Region(RoomName.CASTLE_TOWN_TELMAS_BAR, player, world)
    regions[RoomName.CASTLE_TOWN_TELMAS_BAR] = castle_town_telmas_bar
    world.regions.append(castle_town_telmas_bar)

    castle_town_telmas_bar.locations.append(
    TPLocation(
        player,
        CheckName.TELMA_INVOICE,
        castle_town_telmas_bar,
        LOCATION_TABLE[CheckName.TELMA_INVOICE]
      )
    )

    lanayru_field = Region(RoomName.LANAYRU_FIELD, player, world)
    regions[RoomName.LANAYRU_FIELD] = lanayru_field
    world.regions.append(lanayru_field)

    lanayru_field.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_FIELD_BEHIND_GATE_UNDERWATER_CHEST,
        lanayru_field,
        LOCATION_TABLE[CheckName.LANAYRU_FIELD_BEHIND_GATE_UNDERWATER_CHEST]
      )
    )

    lanayru_field.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_FIELD_MALE_STAG_BEETLE,
        lanayru_field,
        LOCATION_TABLE[CheckName.LANAYRU_FIELD_MALE_STAG_BEETLE]
      )
    )

    lanayru_field.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_FIELD_FEMALE_STAG_BEETLE,
        lanayru_field,
        LOCATION_TABLE[CheckName.LANAYRU_FIELD_FEMALE_STAG_BEETLE]
      )
    )

    lanayru_field.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_FIELD_BRIDGE_POE,
        lanayru_field,
        LOCATION_TABLE[CheckName.LANAYRU_FIELD_BRIDGE_POE]
      )
    )

    lanayru_field_cave_entrance = Region(RoomName.LANAYRU_FIELD_CAVE_ENTRANCE, player, world)
    regions[RoomName.LANAYRU_FIELD_CAVE_ENTRANCE] = lanayru_field_cave_entrance
    world.regions.append(lanayru_field_cave_entrance)

    lanayru_field_behind_boulder = Region(RoomName.LANAYRU_FIELD_BEHIND_BOULDER, player, world)
    regions[RoomName.LANAYRU_FIELD_BEHIND_BOULDER] = lanayru_field_behind_boulder
    world.regions.append(lanayru_field_behind_boulder)

    hyrule_field_near_spinner_rails = Region(RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS, player, world)
    regions[RoomName.HYRULE_FIELD_NEAR_SPINNER_RAILS] = hyrule_field_near_spinner_rails
    world.regions.append(hyrule_field_near_spinner_rails)

    hyrule_field_near_spinner_rails.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_FIELD_SPINNER_TRACK_CHEST,
        hyrule_field_near_spinner_rails,
        LOCATION_TABLE[CheckName.LANAYRU_FIELD_SPINNER_TRACK_CHEST]
      )
    )

    lanayru_ice_puzzle_cave = Region(RoomName.LANAYRU_ICE_PUZZLE_CAVE, player, world)
    regions[RoomName.LANAYRU_ICE_PUZZLE_CAVE] = lanayru_ice_puzzle_cave
    world.regions.append(lanayru_ice_puzzle_cave)

    lanayru_ice_puzzle_cave.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_ICE_BLOCK_PUZZLE_CAVE_CHEST,
        lanayru_ice_puzzle_cave,
        LOCATION_TABLE[CheckName.LANAYRU_ICE_BLOCK_PUZZLE_CAVE_CHEST]
      )
    )

    lanayru_field_chu_grotto = Region(RoomName.LANAYRU_FIELD_CHU_GROTTO, player, world)
    regions[RoomName.LANAYRU_FIELD_CHU_GROTTO] = lanayru_field_chu_grotto
    world.regions.append(lanayru_field_chu_grotto)

    lanayru_field_skulltula_grotto = Region(RoomName.LANAYRU_FIELD_SKULLTULA_GROTTO, player, world)
    regions[RoomName.LANAYRU_FIELD_SKULLTULA_GROTTO] = lanayru_field_skulltula_grotto
    world.regions.append(lanayru_field_skulltula_grotto)

    lanayru_field_skulltula_grotto.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_FIELD_SKULLTULA_GROTTO_CHEST,
        lanayru_field_skulltula_grotto,
        LOCATION_TABLE[CheckName.LANAYRU_FIELD_SKULLTULA_GROTTO_CHEST]
      )
    )

    lanayru_field_poe_grotto = Region(RoomName.LANAYRU_FIELD_POE_GROTTO, player, world)
    regions[RoomName.LANAYRU_FIELD_POE_GROTTO] = lanayru_field_poe_grotto
    world.regions.append(lanayru_field_poe_grotto)

    lanayru_field_poe_grotto.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_FIELD_POE_GROTTO_LEFT_POE,
        lanayru_field_poe_grotto,
        LOCATION_TABLE[CheckName.LANAYRU_FIELD_POE_GROTTO_LEFT_POE]
      )
    )

    lanayru_field_poe_grotto.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_FIELD_POE_GROTTO_RIGHT_POE,
        lanayru_field_poe_grotto,
        LOCATION_TABLE[CheckName.LANAYRU_FIELD_POE_GROTTO_RIGHT_POE]
      )
    )

    outside_castle_town_west = Region(RoomName.OUTSIDE_CASTLE_TOWN_WEST, player, world)
    regions[RoomName.OUTSIDE_CASTLE_TOWN_WEST] = outside_castle_town_west
    world.regions.append(outside_castle_town_west)

    outside_castle_town_west.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_FIELD_AMPHITHEATER_OWL_STATUE_CHEST,
        outside_castle_town_west,
        LOCATION_TABLE[CheckName.HYRULE_FIELD_AMPHITHEATER_OWL_STATUE_CHEST]
      )
    )

    outside_castle_town_west.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_FIELD_AMPHITHEATER_OWL_STATUE_SKY_CHARACTER,
        outside_castle_town_west,
        LOCATION_TABLE[CheckName.HYRULE_FIELD_AMPHITHEATER_OWL_STATUE_SKY_CHARACTER]
      )
    )

    outside_castle_town_west.locations.append(
    TPLocation(
        player,
        CheckName.WEST_HYRULE_FIELD_MALE_BUTTERFLY,
        outside_castle_town_west,
        LOCATION_TABLE[CheckName.WEST_HYRULE_FIELD_MALE_BUTTERFLY]
      )
    )

    outside_castle_town_west.locations.append(
    TPLocation(
        player,
        CheckName.WEST_HYRULE_FIELD_FEMALE_BUTTERFLY,
        outside_castle_town_west,
        LOCATION_TABLE[CheckName.WEST_HYRULE_FIELD_FEMALE_BUTTERFLY]
      )
    )

    outside_castle_town_west.locations.append(
    TPLocation(
        player,
        CheckName.HYRULE_FIELD_AMPHITHEATER_POE,
        outside_castle_town_west,
        LOCATION_TABLE[CheckName.HYRULE_FIELD_AMPHITHEATER_POE]
      )
    )

    outside_castle_town_west.locations.append(
    TPLocation(
        player,
        CheckName.WEST_HYRULE_FIELD_GOLDEN_WOLF,
        outside_castle_town_west,
        LOCATION_TABLE[CheckName.WEST_HYRULE_FIELD_GOLDEN_WOLF]
      )
    )

    outside_castle_town_west_grotto_ledge = Region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE, player, world)
    regions[RoomName.OUTSIDE_CASTLE_TOWN_WEST_GROTTO_LEDGE] = outside_castle_town_west_grotto_ledge
    world.regions.append(outside_castle_town_west_grotto_ledge)

    outside_castle_town_west_helmasaur_grotto = Region(RoomName.OUTSIDE_CASTLE_TOWN_WEST_HELMASAUR_GROTTO, player, world)
    regions[RoomName.OUTSIDE_CASTLE_TOWN_WEST_HELMASAUR_GROTTO] = outside_castle_town_west_helmasaur_grotto
    world.regions.append(outside_castle_town_west_helmasaur_grotto)

    outside_castle_town_west_helmasaur_grotto.locations.append(
    TPLocation(
        player,
        CheckName.WEST_HYRULE_FIELD_HELMASAUR_GROTTO_CHEST,
        outside_castle_town_west_helmasaur_grotto,
        LOCATION_TABLE[CheckName.WEST_HYRULE_FIELD_HELMASAUR_GROTTO_CHEST]
      )
    )

    outside_castle_town_east = Region(RoomName.OUTSIDE_CASTLE_TOWN_EAST, player, world)
    regions[RoomName.OUTSIDE_CASTLE_TOWN_EAST] = outside_castle_town_east
    world.regions.append(outside_castle_town_east)

    outside_castle_town_east.locations.append(
    TPLocation(
        player,
        CheckName.EAST_CASTLE_TOWN_BRIDGE_POE,
        outside_castle_town_east,
        LOCATION_TABLE[CheckName.EAST_CASTLE_TOWN_BRIDGE_POE]
      )
    )

    outside_castle_town_south = Region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH, player, world)
    regions[RoomName.OUTSIDE_CASTLE_TOWN_SOUTH] = outside_castle_town_south
    world.regions.append(outside_castle_town_south)

    outside_castle_town_south.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_TIGHTROPE_CHEST,
        outside_castle_town_south,
        LOCATION_TABLE[CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_TIGHTROPE_CHEST]
      )
    )

    outside_castle_town_south.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_FOUNTAIN_CHEST,
        outside_castle_town_south,
        LOCATION_TABLE[CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_FOUNTAIN_CHEST]
      )
    )

    outside_castle_town_south.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_DOUBLE_CLAWSHOT_CHASM_CHEST,
        outside_castle_town_south,
        LOCATION_TABLE[CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_DOUBLE_CLAWSHOT_CHASM_CHEST]
      )
    )

    outside_castle_town_south.locations.append(
    TPLocation(
        player,
        CheckName.WOODEN_STATUE,
        outside_castle_town_south,
        LOCATION_TABLE[CheckName.WOODEN_STATUE]
      )
    )

    outside_castle_town_south.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_MALE_LADYBUG,
        outside_castle_town_south,
        LOCATION_TABLE[CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_MALE_LADYBUG]
      )
    )

    outside_castle_town_south.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_FEMALE_LADYBUG,
        outside_castle_town_south,
        LOCATION_TABLE[CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_FEMALE_LADYBUG]
      )
    )

    outside_castle_town_south.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_POE,
        outside_castle_town_south,
        LOCATION_TABLE[CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_POE]
      )
    )

    outside_castle_town_south.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_GOLDEN_WOLF,
        outside_castle_town_south,
        LOCATION_TABLE[CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_GOLDEN_WOLF]
      )
    )

    outside_castle_town_south_inside_boulder = Region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_INSIDE_BOULDER, player, world)
    regions[RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_INSIDE_BOULDER] = outside_castle_town_south_inside_boulder
    world.regions.append(outside_castle_town_south_inside_boulder)

    outside_castle_town_south_tektite_grotto = Region(RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_TEKTITE_GROTTO, player, world)
    regions[RoomName.OUTSIDE_CASTLE_TOWN_SOUTH_TEKTITE_GROTTO] = outside_castle_town_south_tektite_grotto
    world.regions.append(outside_castle_town_south_tektite_grotto)

    outside_castle_town_south_tektite_grotto.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_TEKTITE_GROTTO_CHEST,
        outside_castle_town_south_tektite_grotto,
        LOCATION_TABLE[CheckName.OUTSIDE_SOUTH_CASTLE_TOWN_TEKTITE_GROTTO_CHEST]
      )
    )

    lake_hylia_bridge = Region(RoomName.LAKE_HYLIA_BRIDGE, player, world)
    regions[RoomName.LAKE_HYLIA_BRIDGE] = lake_hylia_bridge
    world.regions.append(lake_hylia_bridge)

    lake_hylia_bridge.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_BRIDGE_VINES_CHEST,
        lake_hylia_bridge,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_BRIDGE_VINES_CHEST]
      )
    )

    lake_hylia_bridge.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_BRIDGE_OWL_STATUE_CHEST,
        lake_hylia_bridge,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_BRIDGE_OWL_STATUE_CHEST]
      )
    )

    lake_hylia_bridge.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_BRIDGE_OWL_STATUE_SKY_CHARACTER,
        lake_hylia_bridge,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_BRIDGE_OWL_STATUE_SKY_CHARACTER]
      )
    )

    lake_hylia_bridge.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_BRIDGE_MALE_MANTIS,
        lake_hylia_bridge,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_BRIDGE_MALE_MANTIS]
      )
    )

    lake_hylia_bridge.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_BRIDGE_FEMALE_MANTIS,
        lake_hylia_bridge,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_BRIDGE_FEMALE_MANTIS]
      )
    )

    lake_hylia_bridge_grotto_ledge = Region(RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE, player, world)
    regions[RoomName.LAKE_HYLIA_BRIDGE_GROTTO_LEDGE] = lake_hylia_bridge_grotto_ledge
    world.regions.append(lake_hylia_bridge_grotto_ledge)

    lake_hylia_bridge_grotto_ledge.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_BRIDGE_CLIFF_CHEST,
        lake_hylia_bridge_grotto_ledge,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_BRIDGE_CLIFF_CHEST]
      )
    )

    lake_hylia_bridge_grotto_ledge.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_BRIDGE_CLIFF_POE,
        lake_hylia_bridge_grotto_ledge,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_BRIDGE_CLIFF_POE]
      )
    )

    lake_hylia_bridge_bubble_grotto = Region(RoomName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO, player, world)
    regions[RoomName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO] = lake_hylia_bridge_bubble_grotto
    world.regions.append(lake_hylia_bridge_bubble_grotto)

    lake_hylia_bridge_bubble_grotto.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO_CHEST,
        lake_hylia_bridge_bubble_grotto,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_BRIDGE_BUBBLE_GROTTO_CHEST]
      )
    )

    lake_hylia = Region(RoomName.LAKE_HYLIA, player, world)
    regions[RoomName.LAKE_HYLIA] = lake_hylia
    world.regions.append(lake_hylia)

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_UNDERWATER_CHEST,
        lake_hylia,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_UNDERWATER_CHEST]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_LANAYRU_SPRING_LEFT_STATUE_CHEST,
        lake_hylia,
        LOCATION_TABLE[CheckName.OUTSIDE_LANAYRU_SPRING_LEFT_STATUE_CHEST]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.OUTSIDE_LANAYRU_SPRING_RIGHT_STATUE_CHEST,
        lake_hylia,
        LOCATION_TABLE[CheckName.OUTSIDE_LANAYRU_SPRING_RIGHT_STATUE_CHEST]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.FLIGHT_BY_FOWL_TOP_PLATFORM_REWARD,
        lake_hylia,
        LOCATION_TABLE[CheckName.FLIGHT_BY_FOWL_TOP_PLATFORM_REWARD]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.FLIGHT_BY_FOWL_SECOND_PLATFORM_CHEST,
        lake_hylia,
        LOCATION_TABLE[CheckName.FLIGHT_BY_FOWL_SECOND_PLATFORM_CHEST]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.FLIGHT_BY_FOWL_THIRD_PLATFORM_CHEST,
        lake_hylia,
        LOCATION_TABLE[CheckName.FLIGHT_BY_FOWL_THIRD_PLATFORM_CHEST]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.FLIGHT_BY_FOWL_FOURTH_PLATFORM_CHEST,
        lake_hylia,
        LOCATION_TABLE[CheckName.FLIGHT_BY_FOWL_FOURTH_PLATFORM_CHEST]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.FLIGHT_BY_FOWL_FIFTH_PLATFORM_CHEST,
        lake_hylia,
        LOCATION_TABLE[CheckName.FLIGHT_BY_FOWL_FIFTH_PLATFORM_CHEST]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.AURU_GIFT_TO_FYER,
        lake_hylia,
        LOCATION_TABLE[CheckName.AURU_GIFT_TO_FYER]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.FLIGHT_BY_FOWL_LEDGE_POE,
        lake_hylia,
        LOCATION_TABLE[CheckName.FLIGHT_BY_FOWL_LEDGE_POE]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.ISLE_OF_RICHES_POE,
        lake_hylia,
        LOCATION_TABLE[CheckName.ISLE_OF_RICHES_POE]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_ALCOVE_POE,
        lake_hylia,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_ALCOVE_POE]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_DOCK_POE,
        lake_hylia,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_DOCK_POE]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_TOWER_POE,
        lake_hylia,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_TOWER_POE]
      )
    )

    lake_hylia.locations.append(
    TPLocation(
        player,
        CheckName.PLUMM_FRUIT_BALLOON_MINIGAME,
        lake_hylia,
        LOCATION_TABLE[CheckName.PLUMM_FRUIT_BALLOON_MINIGAME]
      )
    )

    lake_hylia_cave_entrance = Region(RoomName.LAKE_HYLIA_CAVE_ENTRANCE, player, world)
    regions[RoomName.LAKE_HYLIA_CAVE_ENTRANCE] = lake_hylia_cave_entrance
    world.regions.append(lake_hylia_cave_entrance)

    lake_hylia_lakebed_temple_entrance = Region(RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE, player, world)
    regions[RoomName.LAKE_HYLIA_LAKEBED_TEMPLE_ENTRANCE] = lake_hylia_lakebed_temple_entrance
    world.regions.append(lake_hylia_lakebed_temple_entrance)

    lake_hylia_lanayru_spring = Region(RoomName.LAKE_HYLIA_LANAYRU_SPRING, player, world)
    regions[RoomName.LAKE_HYLIA_LANAYRU_SPRING] = lake_hylia_lanayru_spring
    world.regions.append(lake_hylia_lanayru_spring)

    lake_hylia_lanayru_spring.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_SPRING_UNDERWATER_LEFT_CHEST,
        lake_hylia_lanayru_spring,
        LOCATION_TABLE[CheckName.LANAYRU_SPRING_UNDERWATER_LEFT_CHEST]
      )
    )

    lake_hylia_lanayru_spring.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_SPRING_UNDERWATER_RIGHT_CHEST,
        lake_hylia_lanayru_spring,
        LOCATION_TABLE[CheckName.LANAYRU_SPRING_UNDERWATER_RIGHT_CHEST]
      )
    )

    lake_hylia_lanayru_spring.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_SPRING_BACK_ROOM_LEFT_CHEST,
        lake_hylia_lanayru_spring,
        LOCATION_TABLE[CheckName.LANAYRU_SPRING_BACK_ROOM_LEFT_CHEST]
      )
    )

    lake_hylia_lanayru_spring.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_SPRING_BACK_ROOM_RIGHT_CHEST,
        lake_hylia_lanayru_spring,
        LOCATION_TABLE[CheckName.LANAYRU_SPRING_BACK_ROOM_RIGHT_CHEST]
      )
    )

    lake_hylia_lanayru_spring.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_SPRING_BACK_ROOM_LANTERN_CHEST,
        lake_hylia_lanayru_spring,
        LOCATION_TABLE[CheckName.LANAYRU_SPRING_BACK_ROOM_LANTERN_CHEST]
      )
    )

    lake_hylia_lanayru_spring.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_SPRING_EAST_DOUBLE_CLAWSHOT_CHEST,
        lake_hylia_lanayru_spring,
        LOCATION_TABLE[CheckName.LANAYRU_SPRING_EAST_DOUBLE_CLAWSHOT_CHEST]
      )
    )

    lake_hylia_lanayru_spring.locations.append(
    TPLocation(
        player,
        CheckName.LANAYRU_SPRING_WEST_DOUBLE_CLAWSHOT_CHEST,
        lake_hylia_lanayru_spring,
        LOCATION_TABLE[CheckName.LANAYRU_SPRING_WEST_DOUBLE_CLAWSHOT_CHEST]
      )
    )

    lake_hylia_long_cave = Region(RoomName.LAKE_HYLIA_LONG_CAVE, player, world)
    regions[RoomName.LAKE_HYLIA_LONG_CAVE] = lake_hylia_long_cave
    world.regions.append(lake_hylia_long_cave)

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_FIRST_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_FIRST_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_SECOND_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_SECOND_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_THIRD_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_THIRD_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_FOURTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_FOURTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_FIFTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_FIFTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_SIXTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_SIXTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_SEVENTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_SEVENTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_EIGHTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_EIGHTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_NINTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_NINTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_TENTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_TENTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_ELEVENTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_ELEVENTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_TWELFTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_TWELFTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_THIRTEENTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_THIRTEENTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_FOURTEENTH_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_FOURTEENTH_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_END_LANTERN_CHEST,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_END_LANTERN_CHEST]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_FIRST_POE,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_FIRST_POE]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_SECOND_POE,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_SECOND_POE]
      )
    )

    lake_hylia_long_cave.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_LANTERN_CAVE_FINAL_POE,
        lake_hylia_long_cave,
        LOCATION_TABLE[CheckName.LAKE_LANTERN_CAVE_FINAL_POE]
      )
    )

    lake_hylia_shell_blade_grotto = Region(RoomName.LAKE_HYLIA_SHELL_BLADE_GROTTO, player, world)
    regions[RoomName.LAKE_HYLIA_SHELL_BLADE_GROTTO] = lake_hylia_shell_blade_grotto
    world.regions.append(lake_hylia_shell_blade_grotto)

    lake_hylia_shell_blade_grotto.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_SHELL_BLADE_GROTTO_CHEST,
        lake_hylia_shell_blade_grotto,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_SHELL_BLADE_GROTTO_CHEST]
      )
    )

    lake_hylia_water_toadpoli_grotto = Region(RoomName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO, player, world)
    regions[RoomName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO] = lake_hylia_water_toadpoli_grotto
    world.regions.append(lake_hylia_water_toadpoli_grotto)

    lake_hylia_water_toadpoli_grotto.locations.append(
    TPLocation(
        player,
        CheckName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO_CHEST,
        lake_hylia_water_toadpoli_grotto,
        LOCATION_TABLE[CheckName.LAKE_HYLIA_WATER_TOADPOLI_GROTTO_CHEST]
      )
    )

    upper_zoras_river = Region(RoomName.UPPER_ZORAS_RIVER, player, world)
    regions[RoomName.UPPER_ZORAS_RIVER] = upper_zoras_river
    world.regions.append(upper_zoras_river)

    upper_zoras_river.locations.append(
    TPLocation(
        player,
        CheckName.UPPER_ZORAS_RIVER_FEMALE_DRAGONFLY,
        upper_zoras_river,
        LOCATION_TABLE[CheckName.UPPER_ZORAS_RIVER_FEMALE_DRAGONFLY]
      )
    )

    upper_zoras_river.locations.append(
    TPLocation(
        player,
        CheckName.UPPER_ZORAS_RIVER_POE,
        upper_zoras_river,
        LOCATION_TABLE[CheckName.UPPER_ZORAS_RIVER_POE]
      )
    )

    upper_zoras_river_izas_house = Region(RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE, player, world)
    regions[RoomName.UPPER_ZORAS_RIVER_IZAS_HOUSE] = upper_zoras_river_izas_house
    world.regions.append(upper_zoras_river_izas_house)

    upper_zoras_river_izas_house.locations.append(
    TPLocation(
        player,
        CheckName.IZA_HELPING_HAND,
        upper_zoras_river_izas_house,
        LOCATION_TABLE[CheckName.IZA_HELPING_HAND]
      )
    )

    upper_zoras_river_izas_house.locations.append(
    TPLocation(
        player,
        CheckName.IZA_RAGING_RAPIDS_MINIGAME,
        upper_zoras_river_izas_house,
        LOCATION_TABLE[CheckName.IZA_RAGING_RAPIDS_MINIGAME]
      )
    )

    fishing_hole = Region(RoomName.FISHING_HOLE, player, world)
    regions[RoomName.FISHING_HOLE] = fishing_hole
    world.regions.append(fishing_hole)

    fishing_hole.locations.append(
    TPLocation(
        player,
        CheckName.FISHING_HOLE_HEART_PIECE,
        fishing_hole,
        LOCATION_TABLE[CheckName.FISHING_HOLE_HEART_PIECE]
      )
    )

    fishing_hole.locations.append(
    TPLocation(
        player,
        CheckName.FISHING_HOLE_BOTTLE,
        fishing_hole,
        LOCATION_TABLE[CheckName.FISHING_HOLE_BOTTLE]
      )
    )

    fishing_hole_house = Region(RoomName.FISHING_HOLE_HOUSE, player, world)
    regions[RoomName.FISHING_HOLE_HOUSE] = fishing_hole_house
    world.regions.append(fishing_hole_house)

    zoras_domain = Region(RoomName.ZORAS_DOMAIN, player, world)
    regions[RoomName.ZORAS_DOMAIN] = zoras_domain
    world.regions.append(zoras_domain)

    zoras_domain.locations.append(
    TPLocation(
        player,
        CheckName.ZORAS_DOMAIN_CHEST_BY_MOTHER_AND_CHILD_ISLES,
        zoras_domain,
        LOCATION_TABLE[CheckName.ZORAS_DOMAIN_CHEST_BY_MOTHER_AND_CHILD_ISLES]
      )
    )

    zoras_domain.locations.append(
    TPLocation(
        player,
        CheckName.ZORAS_DOMAIN_CHEST_BEHIND_WATERFALL,
        zoras_domain,
        LOCATION_TABLE[CheckName.ZORAS_DOMAIN_CHEST_BEHIND_WATERFALL]
      )
    )

    zoras_domain.locations.append(
    TPLocation(
        player,
        CheckName.ZORAS_DOMAIN_MALE_DRAGONFLY,
        zoras_domain,
        LOCATION_TABLE[CheckName.ZORAS_DOMAIN_MALE_DRAGONFLY]
      )
    )

    zoras_domain.locations.append(
    TPLocation(
        player,
        CheckName.ZORAS_DOMAIN_MOTHER_AND_CHILD_ISLE_POE,
        zoras_domain,
        LOCATION_TABLE[CheckName.ZORAS_DOMAIN_MOTHER_AND_CHILD_ISLE_POE]
      )
    )

    zoras_domain.locations.append(
    TPLocation(
        player,
        CheckName.ZORAS_DOMAIN_WATERFALL_POE,
        zoras_domain,
        LOCATION_TABLE[CheckName.ZORAS_DOMAIN_WATERFALL_POE]
      )
    )

    zoras_domain_west_ledge = Region(RoomName.ZORAS_DOMAIN_WEST_LEDGE, player, world)
    regions[RoomName.ZORAS_DOMAIN_WEST_LEDGE] = zoras_domain_west_ledge
    world.regions.append(zoras_domain_west_ledge)

    zoras_throne_room = Region(RoomName.ZORAS_THRONE_ROOM, player, world)
    regions[RoomName.ZORAS_THRONE_ROOM] = zoras_throne_room
    world.regions.append(zoras_throne_room)

    zoras_throne_room.locations.append(
    TPLocation(
        player,
        CheckName.ZORAS_DOMAIN_LIGHT_ALL_TORCHES_CHEST,
        zoras_throne_room,
        LOCATION_TABLE[CheckName.ZORAS_DOMAIN_LIGHT_ALL_TORCHES_CHEST]
      )
    )

    zoras_throne_room.locations.append(
    TPLocation(
        player,
        CheckName.ZORAS_DOMAIN_EXTINGUISH_ALL_TORCHES_CHEST,
        zoras_throne_room,
        LOCATION_TABLE[CheckName.ZORAS_DOMAIN_EXTINGUISH_ALL_TORCHES_CHEST]
      )
    )

    zoras_throne_room.locations.append(
    TPLocation(
        player,
        CheckName.ZORAS_DOMAIN_UNDERWATER_GORON,
        zoras_throne_room,
        LOCATION_TABLE[CheckName.ZORAS_DOMAIN_UNDERWATER_GORON]
      )
    )

    outside_links_house = Region(RoomName.OUTSIDE_LINKS_HOUSE, player, world)
    regions[RoomName.OUTSIDE_LINKS_HOUSE] = outside_links_house
    world.regions.append(outside_links_house)

    ordon_links_house = Region(RoomName.ORDON_LINKS_HOUSE, player, world)
    regions[RoomName.ORDON_LINKS_HOUSE] = ordon_links_house
    world.regions.append(ordon_links_house)

    ordon_links_house.locations.append(
    TPLocation(
        player,
        CheckName.WOODEN_SWORD_CHEST,
        ordon_links_house,
        LOCATION_TABLE[CheckName.WOODEN_SWORD_CHEST]
      )
    )

    ordon_links_house.locations.append(
    TPLocation(
        player,
        CheckName.LINKS_BASEMENT_CHEST,
        ordon_links_house,
        LOCATION_TABLE[CheckName.LINKS_BASEMENT_CHEST]
      )
    )

    ordon_village = Region(RoomName.ORDON_VILLAGE, player, world)
    regions[RoomName.ORDON_VILLAGE] = ordon_village
    world.regions.append(ordon_village)

    ordon_village.locations.append(
    TPLocation(
        player,
        CheckName.ULI_CRADLE_DELIVERY,
        ordon_village,
        LOCATION_TABLE[CheckName.ULI_CRADLE_DELIVERY]
      )
    )

    ordon_seras_shop = Region(RoomName.ORDON_SERAS_SHOP, player, world)
    regions[RoomName.ORDON_SERAS_SHOP] = ordon_seras_shop
    world.regions.append(ordon_seras_shop)

    ordon_seras_shop.locations.append(
    TPLocation(
        player,
        CheckName.ORDON_CAT_RESCUE,
        ordon_seras_shop,
        LOCATION_TABLE[CheckName.ORDON_CAT_RESCUE]
      )
    )

    ordon_seras_shop.locations.append(
    TPLocation(
        player,
        CheckName.SERA_SHOP_SLINGSHOT,
        ordon_seras_shop,
        LOCATION_TABLE[CheckName.SERA_SHOP_SLINGSHOT]
      )
    )

    ordon_shield_house = Region(RoomName.ORDON_SHIELD_HOUSE, player, world)
    regions[RoomName.ORDON_SHIELD_HOUSE] = ordon_shield_house
    world.regions.append(ordon_shield_house)

    ordon_shield_house.locations.append(
    TPLocation(
        player,
        CheckName.ORDON_SHIELD,
        ordon_shield_house,
        LOCATION_TABLE[CheckName.ORDON_SHIELD]
      )
    )

    ordon_sword_house = Region(RoomName.ORDON_SWORD_HOUSE, player, world)
    regions[RoomName.ORDON_SWORD_HOUSE] = ordon_sword_house
    world.regions.append(ordon_sword_house)

    ordon_sword_house.locations.append(
    TPLocation(
        player,
        CheckName.ORDON_SWORD,
        ordon_sword_house,
        LOCATION_TABLE[CheckName.ORDON_SWORD]
      )
    )

    ordon_bos_house_left_door = Region(RoomName.ORDON_BOS_HOUSE_LEFT_DOOR, player, world)
    regions[RoomName.ORDON_BOS_HOUSE_LEFT_DOOR] = ordon_bos_house_left_door
    world.regions.append(ordon_bos_house_left_door)

    ordon_bos_house_right_door = Region(RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR, player, world)
    regions[RoomName.ORDON_BOS_HOUSE_RIGHT_DOOR] = ordon_bos_house_right_door
    world.regions.append(ordon_bos_house_right_door)

    ordon_bos_house = Region(RoomName.ORDON_BOS_HOUSE, player, world)
    regions[RoomName.ORDON_BOS_HOUSE] = ordon_bos_house
    world.regions.append(ordon_bos_house)

    ordon_bos_house.locations.append(
    TPLocation(
        player,
        CheckName.WRESTLING_WITH_BO,
        ordon_bos_house,
        LOCATION_TABLE[CheckName.WRESTLING_WITH_BO]
      )
    )

    ordon_ranch_entrance = Region(RoomName.ORDON_RANCH_ENTRANCE, player, world)
    regions[RoomName.ORDON_RANCH_ENTRANCE] = ordon_ranch_entrance
    world.regions.append(ordon_ranch_entrance)

    ordon_ranch = Region(RoomName.ORDON_RANCH, player, world)
    regions[RoomName.ORDON_RANCH] = ordon_ranch
    world.regions.append(ordon_ranch)

    ordon_ranch.locations.append(
    TPLocation(
        player,
        CheckName.HERDING_GOATS_REWARD,
        ordon_ranch,
        LOCATION_TABLE[CheckName.HERDING_GOATS_REWARD]
      )
    )

    ordon_ranch_stable = Region(RoomName.ORDON_RANCH_STABLE, player, world)
    regions[RoomName.ORDON_RANCH_STABLE] = ordon_ranch_stable
    world.regions.append(ordon_ranch_stable)

    ordon_ranch_grotto = Region(RoomName.ORDON_RANCH_GROTTO, player, world)
    regions[RoomName.ORDON_RANCH_GROTTO] = ordon_ranch_grotto
    world.regions.append(ordon_ranch_grotto)

    ordon_ranch_grotto.locations.append(
    TPLocation(
        player,
        CheckName.ORDON_RANCH_GROTTO_LANTERN_CHEST,
        ordon_ranch_grotto,
        LOCATION_TABLE[CheckName.ORDON_RANCH_GROTTO_LANTERN_CHEST]
      )
    )

    ordon_spring = Region(RoomName.ORDON_SPRING, player, world)
    regions[RoomName.ORDON_SPRING] = ordon_spring
    world.regions.append(ordon_spring)

    ordon_spring.locations.append(
    TPLocation(
        player,
        CheckName.ORDON_SPRING_GOLDEN_WOLF,
        ordon_spring,
        LOCATION_TABLE[CheckName.ORDON_SPRING_GOLDEN_WOLF]
      )
    )

    ordon_bridge = Region(RoomName.ORDON_BRIDGE, player, world)
    regions[RoomName.ORDON_BRIDGE] = ordon_bridge
    world.regions.append(ordon_bridge)

    snowpeak_climb_lower = Region(RoomName.SNOWPEAK_CLIMB_LOWER, player, world)
    regions[RoomName.SNOWPEAK_CLIMB_LOWER] = snowpeak_climb_lower
    world.regions.append(snowpeak_climb_lower)

    snowpeak_climb_lower.locations.append(
    TPLocation(
        player,
        CheckName.ASHEI_SKETCH,
        snowpeak_climb_lower,
        LOCATION_TABLE[CheckName.ASHEI_SKETCH]
      )
    )

    snowpeak_climb_upper = Region(RoomName.SNOWPEAK_CLIMB_UPPER, player, world)
    regions[RoomName.SNOWPEAK_CLIMB_UPPER] = snowpeak_climb_upper
    world.regions.append(snowpeak_climb_upper)

    snowpeak_climb_upper.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_ABOVE_FREEZARD_GROTTO_POE,
        snowpeak_climb_upper,
        LOCATION_TABLE[CheckName.SNOWPEAK_ABOVE_FREEZARD_GROTTO_POE]
      )
    )

    snowpeak_climb_upper.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_BLIZZARD_POE,
        snowpeak_climb_upper,
        LOCATION_TABLE[CheckName.SNOWPEAK_BLIZZARD_POE]
      )
    )

    snowpeak_climb_upper.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_POE_AMONG_TREES,
        snowpeak_climb_upper,
        LOCATION_TABLE[CheckName.SNOWPEAK_POE_AMONG_TREES]
      )
    )

    snowpeak_ice_keese_grotto = Region(RoomName.SNOWPEAK_ICE_KEESE_GROTTO, player, world)
    regions[RoomName.SNOWPEAK_ICE_KEESE_GROTTO] = snowpeak_ice_keese_grotto
    world.regions.append(snowpeak_ice_keese_grotto)

    snowpeak_freezard_grotto = Region(RoomName.SNOWPEAK_FREEZARD_GROTTO, player, world)
    regions[RoomName.SNOWPEAK_FREEZARD_GROTTO] = snowpeak_freezard_grotto
    world.regions.append(snowpeak_freezard_grotto)

    snowpeak_freezard_grotto.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_FREEZARD_GROTTO_CHEST,
        snowpeak_freezard_grotto,
        LOCATION_TABLE[CheckName.SNOWPEAK_FREEZARD_GROTTO_CHEST]
      )
    )

    snowpeak_summit_upper = Region(RoomName.SNOWPEAK_SUMMIT_UPPER, player, world)
    regions[RoomName.SNOWPEAK_SUMMIT_UPPER] = snowpeak_summit_upper
    world.regions.append(snowpeak_summit_upper)

    snowpeak_summit_upper.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_CAVE_ICE_LANTERN_CHEST,
        snowpeak_summit_upper,
        LOCATION_TABLE[CheckName.SNOWPEAK_CAVE_ICE_LANTERN_CHEST]
      )
    )

    snowpeak_summit_upper.locations.append(
    TPLocation(
        player,
        CheckName.SNOWBOARD_RACING_PRIZE,
        snowpeak_summit_upper,
        LOCATION_TABLE[CheckName.SNOWBOARD_RACING_PRIZE]
      )
    )

    snowpeak_summit_upper.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_CAVE_ICE_POE,
        snowpeak_summit_upper,
        LOCATION_TABLE[CheckName.SNOWPEAK_CAVE_ICE_POE]
      )
    )

    snowpeak_summit_lower = Region(RoomName.SNOWPEAK_SUMMIT_LOWER, player, world)
    regions[RoomName.SNOWPEAK_SUMMIT_LOWER] = snowpeak_summit_lower
    world.regions.append(snowpeak_summit_lower)

    snowpeak_summit_lower.locations.append(
    TPLocation(
        player,
        CheckName.SNOWPEAK_ICY_SUMMIT_POE,
        snowpeak_summit_lower,
        LOCATION_TABLE[CheckName.SNOWPEAK_ICY_SUMMIT_POE]
      )
    )
# Connect Menu to starting region
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
        )