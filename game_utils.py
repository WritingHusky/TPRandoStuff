import os
import json
from queue import Queue
from enum import Enum
from dolphin_memory_engine import read_byte, write_byte, hook, is_hooked
from item_addresses import ItemAddresses
from read_check_address import read_checks, get_check_address, read_check_byte, get_bit_value

class RegionIDs(Enum):
    ORDON_VILLAGE = (0x0, 0X804063B0)
    SEWERS = (0x1, 0X804063D0)
    FARON = (0x2, 0X80406F0)
    KAKARIKO = (0x3, 0X80406410)
    ZORA_DOMAIN = (0x4, 0X80406430)
    HYRULE_FIELD = (0x6, 0X80406470)
    SACRED_GROVE = (0x7, 0X80406490)
    SNOWPEAK = (0x8, 0X804064B0)
    CASTLE_TOWN = (0x9, 0X804064D0)
    GERUDO_DESERT = (0xA, 0X804064F0)
    FISHING_HOLE = (0xB, 0X80406510)
    FOREST_TEMPLE = (0x10, 0X804065B0)
    GORON_MINES = (0x11, 0X804065D0)
    LAKEBED_TEMPLE = (0x12, 0X804065F0)
    ARBITERS_GROUNDS = (0x13, 0X80406610)
    SNOWPEAK_RUINS = (0x14, 0X80406630)
    TEMPLE_OF_TIME = (0x15, 0X80406650)
    CITY_IN_THE_SKY = (0x16, 0X80406670)
    PALACE_OF_TWILIGHT = (0x17, 0X80406690)
    HYRULE_CASTLE = (0x18, 0X804066B0)
    CAVES = (0x19, 0X804066D0)
    HYPE_CAVE = (0x1A, 0X804066F0)
    GROTTOS = (0x1B, 0X80406710)


class GameUtils:
    def __init__(self, use_json=False, check_file_name='TPGC US Check Flags.csv'):
        self.use_json = use_json
        self.check_file_name = check_file_name
        self.write_queue = Queue()
        self.write_address = 0x80406AB0
        self.region_get_address = 0x80406B38
        self.region_start_address = 0x80406B18
        hook()

    def check_location(self, check_name):
        if not is_hooked():
            hook()
        file_path = os.path.join(os.path.dirname(__file__), self.check_file_name)
        checks = read_checks(file_path)
        address, flag = get_check_address(checks, check_name)
        if address == "Invalid" or address is None:
            raise ValueError(f"Check '{check_name}' is not valid or is incorrectly formatted.")
        byte_value = read_check_byte(address)
        return get_bit_value(byte_value, flag)

    def give_item(self, item_name):
        if self.use_json:
            with open(os.path.join(os.path.dirname(__file__), 'item_addresses.json'), 'r') as f:
                data = json.load(f)
            item = next((item for item in data['items'] if item['Name'] == item_name), None)
            if item:
                self.write_queue.put(int(item['Hex-Code'], 16))
            else:
                print(f"Item '{item_name}' not found in address list.")
        else:
            try:
                item_code = ItemAddresses[item_name.replace(" ", "_").upper()].value
                self.write_queue.put(item_code)
            except KeyError:
                print(f"Item '{item_name}' not found in address list.")

    def process_queue(self):
        if not self.write_queue.empty():
            if read_byte(self.write_address) == 0x00:
                item_code = self.write_queue.get()
                write_byte(self.write_address, item_code)

    def get_all_checks(self):
        if not is_hooked():
            hook()
        file_path = os.path.join(os.path.dirname(__file__), self.check_file_name)
        checks = read_checks(file_path)
        check_statuses = {}
        for check_name in checks.keys():
            address, flag = get_check_address(checks, check_name)
            if address == "Invalid" or address is None:
                check_statuses[check_name] = "error"
            else:
                byte_value = read_check_byte(address)
                check_statuses[check_name] = get_bit_value(byte_value, flag)
        return check_statuses

    def get_checks_in_current_region(self):
        if not is_hooked():
            hook()
        current_region_id = self.get_region_address()
        file_path = os.path.join(os.path.dirname(__file__), self.check_file_name)
        checks = read_checks(file_path)
        checks_in_region = {}
        for check_name, (address, flag, is_region_flag, save_file_region, note) in checks.items():
            if save_file_region == current_region_id:
                region_offset_address = self.region_start_address + int(address, 16)
                if region_offset_address == "Invalid" or region_offset_address is None:
                    checks_in_region[check_name] = "error"
                else:
                    byte_value = read_check_byte(region_offset_address)
                    checks_in_region[check_name] = get_bit_value(byte_value, flag)
        return checks_in_region

    def get_current_region(self):
        if not is_hooked():
            hook()
        current_region_byte = read_byte(self.region_get_address)
        current_region_name = next((region.name for region in RegionIDs if region.value[0] == current_region_byte), "Unknown Region")
        return current_region_name
    
    def get_region_id(self):
        if not is_hooked():
            hook()
        current_region_byte = read_byte(self.region_get_address)
        current_region_id = hex(current_region_byte)
        return current_region_id
    
    def get_region_address(self):
        if not is_hooked():
            hook()
        current_region_byte = read_byte(self.region_get_address)
        current_region_address = next((region.value[1] for region in RegionIDs if region.value[0] == current_region_byte), "Unknown Region")
        return hex(current_region_address)

