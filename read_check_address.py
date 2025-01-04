import csv
import os
from dolphin_memory_engine import read_byte, hook, is_hooked

CHECK_FILE_NAME = 'TPGC US Check Flags.csv'

def read_checks(file_path):
    checks = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) < 5:
                checks[row[0]] = ("Invalid", "Invalid", "Invalid", "Invalid", "Invalid")
                continue
            check_name = row[0]
            address = row[1]
            flag = row[2]
            is_region_flag = row[3]
            save_file_region = row[4]
            note = row[5] if len(row) > 5 else ""
            checks[check_name] = (address, flag, is_region_flag, save_file_region, note)
    return checks

def get_check_address(checks, check_name):
    if check_name in checks:
        address, flag, is_region_flag, save_file_region, note = checks[check_name]
        if is_region_flag == "Region Flag":
            try:
                full_address = hex(int(save_file_region, 16) + int(address, 16))
            except ValueError:
                return "Invalid", "Invalid"
        else:
            try:
                full_address = hex(int(address, 16))
            except ValueError:
                return "Invalid", "Invalid"
        return full_address, flag
    else:
        return None, None

def read_check_byte(address):
    if isinstance(address, str):
        address_int = int(address, 16)
    else:
        address_int = address
    if address_int > 0xFFFFFFFF:
        raise ValueError(f"Address {hex(address_int)} is too large.")
    byte_value = read_byte(address_int)
    return byte_value

def get_bit_value(byte_value, bit_position):
    return (byte_value & int(bit_position, 16)) != 0

def display_check_info(file, check_name, address, byte_value, flag, bit_value):
    file.write(f"Check Name: {check_name}\n")
    file.write(f"Address: {address}\n")
    file.write(f"Byte Value: {byte_value}\n")
    file.write(f"Bit Position: {flag}\n")
    file.write(f"Bit Value: {bit_value}\n")
    file.write("\n")

def iterate_checks(checks, output_file):
    with open(output_file, 'w') as file:
        for check_name in checks:
            address, flag = get_check_address(checks, check_name)
            if address == "Invalid":
                file.write(f"Check Name: {check_name}\n")
                file.write(f"Error: Check is not correctly formatted.\n")
                file.write("\n")
                continue
            if address:
                try:
                    byte_value = read_check_byte(address)
                    bit_value = get_bit_value(byte_value, flag)
                    display_check_info(file, check_name, address, byte_value, flag, bit_value)
                except ValueError as e:
                    file.write(f"Check Name: {check_name}\n")
                    file.write(f"Error: {str(e)}\n")
                    file.write("\n")

def iterate_region_checks(checks, output_file, region_start_address, current_region_address):
    with open(output_file, 'w') as file:
        for check_name, (address, flag, is_region_flag, save_file_region, note) in checks.items():
            if is_region_flag == "Region Flag" and save_file_region == current_region_address:
                region_offset_address = hex(region_start_address + int(address, 16))
                if region_offset_address == "Invalid":
                    file.write(f"Check Name: {check_name}\n")
                    file.write(f"Error: Check is not correctly formatted.\n")
                    file.write("\n")
                    continue
                try:
                    byte_value = read_check_byte(region_offset_address)
                    bit_value = get_bit_value(byte_value, flag)
                    display_check_info(file, check_name, region_offset_address, byte_value, flag, bit_value)
                except ValueError as e:
                    file.write(f"Check Name: {check_name}\n")
                    file.write(f"Error: {str(e)}\n")
                    file.write("\n")

def get_check_bit_value(check_name):
    if(is_hooked() == False):
        hook()
    file_path = os.path.join(os.path.dirname(__file__), CHECK_FILE_NAME)
    checks = read_checks(file_path)
    address, flag = get_check_address(checks, check_name)
    if address == "Invalid" or address is None:
        raise ValueError(f"Check '{check_name}' is not valid or is incorrectly formatted.")
    byte_value = read_check_byte(address)
    return get_bit_value(byte_value, flag)


