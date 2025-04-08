from WorldParser import WorldParser
from AccessParser import AccessParser
from LocationGenerator import LocationGenerator
from RegionGenerator import RegionGenerator


def main():
    world_parser = WorldParser()
    world_parser.combine_world_files()

    access_parser = AccessParser()
    access_parser.create_access_rules_file()

    if not access_parser.validate_access_rules():
        print("New access rules please update the file")
        return

    location_generator = LocationGenerator()
    location_generator.generate_location_rules()

    region_generator = RegionGenerator()
    region_generator.generate_region_creation()
    region_generator.generate_region_connections()
    region_generator.generate_region_rules()

    print("Done")


if __name__ == "__main__":
    main()
