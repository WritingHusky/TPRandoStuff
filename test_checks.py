import os
from game_utils import GameUtils
from read_check_address import read_checks, iterate_checks, iterate_region_checks

def main():
    game_utils = GameUtils()
    file_path = os.path.join(os.path.dirname(__file__), 'TPGC US Check Flags.csv')
    output_file = 'checks_output.txt'
    checks = read_checks(file_path)
    choice = "region"
    
    if choice == 'all':
        iterate_checks(checks, output_file)
        print(f"All checks have been written to {output_file}.")
    elif choice == 'region':
        iterate_region_checks(checks, output_file, game_utils.region_start_address, game_utils.get_region_address())
        print(f"Region checks have been written to {output_file}.")
        print(f"Region: {game_utils.get_current_region()}")
    else:
        print("Invalid choice. Please enter 'all' or 'region'.")

if __name__ == "__main__":
    main()
