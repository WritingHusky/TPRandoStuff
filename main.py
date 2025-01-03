from dolphin_memory_engine import read_byte, hook, write_byte
import json
import tkinter as tk
from queue import Queue
from item_addresses import ItemAddresses

NUM_PER_COLUMN = 30
USE_JSON = False

hook()

write_queue = Queue()

def write_item_code(item_name):
    if USE_JSON:
        with open('item_addresses.json', 'r') as f:
            data = json.load(f)
        item = next((item for item in data['items'] if item['Name'] == item_name), None)
        if item:
            write_queue.put(int(item['Hex-Code'], 16))
        else:
            print(f"Item '{item_name}' not found in address list.")
    else:
        try:
            item_code = ItemAddresses[item_name.replace(" ", "_").upper()].value
            write_queue.put(item_code)
        except KeyError:
            print(f"Item '{item_name}' not found in address list.")

def process_queue():
    if not write_queue.empty():
        if read_byte(0x80406AB0) == 0x00:
            item_code = write_queue.get()
            write_byte(0x80406AB0, item_code)
    root.after(100, process_queue)

def on_button_click(item_name):
    write_item_code(item_name)

def on_checkbox_click(item_name, var):
    if USE_JSON:
        with open('item_addresses.json', 'r') as f:
            data = json.load(f)
        for item in data['items']:
            if item['Name'] == item_name:
                item['used'] = var.get()
                break
        with open('item_addresses.json', 'w') as f:
            json.dump(data, f, indent=4)

# Create the main window
root = tk.Tk()
root.title("Item Selector")

if USE_JSON:
    # Load item data from JSON
    with open('item_addresses.json', 'r') as f:
        data = json.load(f)
    items = data['items']
else:
    # Load item data from enum
    items = [{'Name': item.name.replace("_", " ").title(), 'Hex-Code': hex(item.value), 'used': True} for item in ItemAddresses]

# Create buttons and checkboxes for each item
for idx, item in enumerate(items):
    item_name = item['Name']
    item_used = item['used']
    
    button = tk.Button(root, text=item_name, command=lambda name=item_name: on_button_click(name))
    button.grid(column=(idx // NUM_PER_COLUMN) * 2, row=idx % NUM_PER_COLUMN)
    
    if USE_JSON:
        var = tk.BooleanVar(value=item_used)
        checkbox = tk.Checkbutton(root, variable=var, command=lambda name=item_name, var=var: on_checkbox_click(name, var))
        checkbox.grid(column=(idx // NUM_PER_COLUMN) * 2 + 1, row=idx % NUM_PER_COLUMN)

# Start processing the queue
root.after(100, process_queue)

# Run the application
root.mainloop()