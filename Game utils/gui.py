import json
import tkinter as tk
from queue import Queue
from item_addresses import ItemAddresses
import numpy as np  # type: ignore
import os
from game_utils import GameUtils

USE_JSON = False
HIDE_UNUSED = False

write_queue = Queue()
item_index = 0
hex_index = 0

game_utils = GameUtils(use_json=USE_JSON)


def write_item_code(item_name):
    game_utils.give_item(item_name)


def process_queue():
    game_utils.process_queue()
    root.after(100, process_queue)


def on_button_click(item_name):
    write_item_code(item_name)


def on_checkbox_click(item_name, var):
    if USE_JSON:
        with open(
            os.path.join(os.path.dirname(__file__), "item_addresses.json"), "r"
        ) as f:
            data = json.load(f)
        for item in data["items"]:
            if item["Name"] == item_name:
                item["used"] = var.get()
                break
        with open(
            os.path.join(os.path.dirname(__file__), "item_addresses.json"), "w"
        ) as f:
            json.dump(data, f, indent=4)


def display_next_item():
    global item_index
    if USE_JSON:
        with open(
            os.path.join(os.path.dirname(__file__), "item_addresses.json"), "r"
        ) as f:
            data = json.load(f)
        items = data["items"]
    else:
        items = [
            {
                "Name": item.name.replace("_", " ").title(),
                "Hex-Code": hex(item.value),
                "used": True,
            }
            for item in ItemAddresses
        ]

    if item_index < len(items):
        item_name = items[item_index]["Name"]
        item_label.config(text=item_name)
        item_index += 1
    else:
        item_label.config(text="End of items")
        item_index = 0


def display_next_hex():
    global hex_index
    if hex_index <= 0xFE:
        hex_value = hex(hex_index)
        item_label.config(text=hex_value)
        hex_index += 1
    else:
        item_label.config(text="End of hex values")
        hex_index = 0


def add_all_items_to_queue():
    if USE_JSON:
        with open(
            os.path.join(os.path.dirname(__file__), "item_addresses.json"), "r"
        ) as f:
            data = json.load(f)
        items = data["items"]
        for item in items:
            write_queue.put(int(item["Hex-Code"], 16))
    else:
        for item in ItemAddresses:
            write_queue.put(item.value)


def add_all_hex_to_queue():
    for i in range(0x00, 0xFF):
        write_queue.put(i)


def toggle_use_json():
    global USE_JSON, game_utils
    USE_JSON = not USE_JSON
    game_utils = GameUtils(use_json=USE_JSON)
    refresh_items()


def toggle_hide_unused():
    global HIDE_UNUSED
    HIDE_UNUSED = not HIDE_UNUSED
    refresh_items()


def refresh_items():
    global items, item_index
    item_index = 0
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) or isinstance(widget, tk.Checkbutton):
            widget.destroy()

    if USE_JSON:
        with open(
            os.path.join(os.path.dirname(__file__), "item_addresses.json"), "r"
        ) as f:
            data = json.load(f)
        items = data["items"]
        if HIDE_UNUSED:
            items = [item for item in items if item["used"]]
    else:
        items = [
            {
                "Name": item.name.replace("_", " ").title(),
                "Hex-Code": hex(item.value),
                "used": True,
            }
            for item in ItemAddresses
        ]

    NUM_PER_COLUMN = np.ceil(len(items) / 7).astype(int)

    for idx, item in enumerate(items):
        item_name = item["Name"]
        item_used = item["used"]

        button = tk.Button(
            root, text=item_name, command=lambda name=item_name: on_button_click(name)
        )
        button.grid(column=(idx // NUM_PER_COLUMN) * 2, row=idx % NUM_PER_COLUMN)

        if USE_JSON:
            var = tk.BooleanVar(value=item_used)
            checkbox = tk.Checkbutton(
                root,
                variable=var,
                command=lambda name=item_name, var=var: on_checkbox_click(name, var),
            )
            checkbox.grid(
                column=(idx // NUM_PER_COLUMN) * 2 + 1, row=idx % NUM_PER_COLUMN
            )

    item_label.grid(column=0, row=NUM_PER_COLUMN + 1, columnspan=2)


def display_checks():
    for widget in root.winfo_children():
        if widget != check_frame:
            widget.grid_remove()

    check_statuses = game_utils.get_all_checks()
    for widget in check_frame.winfo_children():
        widget.destroy()

    for idx, (check_name, status) in enumerate(check_statuses.items()):
        color = "green" if status == 0 else "red" if status == 1 else "orange"
        button = tk.Button(check_frame, bg=color, width=2, height=1)
        button.grid(row=idx // 20, column=idx % 20)
        button.bind("<Enter>", lambda e, name=check_name: check_tooltip.showtip(name))
        button.bind("<Leave>", lambda e: check_tooltip.hidetip())

    check_frame.grid()
    root.after(60000, display_checks)


class ToolTip:
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None

    def showtip(self, text):
        if self.tipwindow or not text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            tw,
            text=text,
            justify=tk.LEFT,
            background="#ffffe0",
            relief=tk.SOLID,
            borderwidth=1,
            font=("tahoma", "8", "normal"),
        )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


root = tk.Tk()
root.title("Item Selector")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=file_menu)

file_menu.add_command(label="Add All Items", command=add_all_items_to_queue)
file_menu.add_command(label="Add All Hex", command=add_all_hex_to_queue)
file_menu.add_separator()
file_menu.add_command(label="Toggle Use JSON", command=toggle_use_json)
file_menu.add_command(label="Toggle Hide Unused", command=toggle_hide_unused)
file_menu.add_command(label="Display Checks", command=display_checks)

if USE_JSON:
    with open(os.path.join(os.path.dirname(__file__), "item_addresses.json"), "r") as f:
        data = json.load(f)
    items = data["items"]
    if HIDE_UNUSED:
        items = [item for item in items if item["used"]]
else:
    items = [
        {
            "Name": item.name.replace("_", " ").title(),
            "Hex-Code": hex(item.value),
            "used": True,
        }
        for item in ItemAddresses
    ]

NUM_PER_COLUMN = np.ceil(len(items) / 7).astype(int)

for idx, item in enumerate(items):
    item_name = item["Name"]
    item_used = item["used"]

    button = tk.Button(
        root, text=item_name, command=lambda name=item_name: on_button_click(name)
    )
    button.grid(column=(idx // NUM_PER_COLUMN) * 2, row=idx % NUM_PER_COLUMN)

    if USE_JSON:
        var = tk.BooleanVar(value=item_used)
        checkbox = tk.Checkbutton(
            root,
            variable=var,
            command=lambda name=item_name, var=var: on_checkbox_click(name, var),
        )
        checkbox.grid(column=(idx // NUM_PER_COLUMN) * 2 + 1, row=idx % NUM_PER_COLUMN)

item_label = tk.Label(root, text="")
item_label.grid(column=0, row=NUM_PER_COLUMN + 1, columnspan=2)

check_frame = tk.Frame(root)
check_frame.grid(column=0, row=NUM_PER_COLUMN + 2, columnspan=2)
check_tooltip = ToolTip(check_frame)

root.after(100, process_queue)
# root.after(60000, display_checks)

root.mainloop()
