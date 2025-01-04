import time
from game_utils import GameUtils

CHECK_INTERVAL = 10  # Check every 60 seconds
CHECK_VERSION = "all"  # or "region"

def monitor_checks():
    game_utils = GameUtils()
    if CHECK_VERSION == "all":
        previous_checks = game_utils.get_all_checks()
    else:
        previous_checks = game_utils.get_checks_in_current_region()
        current_region_name = game_utils.get_current_region()
        print(f"Monitoring checks in region: {current_region_name}")

    while True:
        current_region_name = game_utils.get_current_region()
        print(f"Checking for new checks in {current_region_name}...")
        if CHECK_VERSION == "all":
            current_checks = game_utils.get_all_checks()
        else:
            current_checks = game_utils.get_checks_in_current_region()
        for check_name, status in current_checks.items():
            if status == 1 and previous_checks.get(check_name) != 1:
                print(f"Check '{check_name}' has been checked!")
        previous_checks = current_checks
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_checks()