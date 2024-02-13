import tkinter as tk
from bot.igbot import InstagramBot
# Explicit imports to satisfy Flake8
from tkinter import (Canvas, Entry, Text, Button,
                     PhotoImage, filedialog, messagebox,
                     Menubutton, Menu, Message)
from tkinter.ttk import Notebook
from lib.yt_dl_app import setup_folders
from pathlib import Path
import json
import sys
import time
import threading

cl = InstagramBot()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"***REMOVED***\instapi\build\assets\frame0")


class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        self.text_widget.configure(state=tk.DISABLED)

    def flush(self):
        pass


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def click_login():
    """
    Log in to Instagram with the given username and password.
    :return: True if login was successful, False otherwise
    """
    username = username_entry.get()
    password = password_entry.get()
    proxy = proxy_entry.get()
    if not username or not password:
        print("Username or password cannot be empty.")
        return False
    else:
        cl.login_user(username, password, proxy)
        print("Logged in")
        return True


def click_start():
    """
    starts the post scheduling feature of the bot
    :return:
    """
    hashtags = hashtags_entry.get("1.0", "end-1c")
    call_to_action = calltoaction_entry.get("1.0", "end-1c")
    directory = directory_entry.get()
    directory = 'r' + directory
    mention = False
    if not click_login():
        # Update console or show a message box
        raise ValueError("Not logged in. Log-in and try again.")
    else:
        pass
    if not directory:
        print("Directory cannot be empty.")
        return
    else:
        mp4_files, txt_files = setup_folders(directory)
        if not mp4_files:
            print("No mp4 files found in the directory.")
            return
        if not txt_files:
            print("No text files found in the directory.")
            return
        print("Starting the bot")
        cl.reels_to_instagram(mp4_files, txt_files, directory, hashtags, call_to_action, mention)
    # Validate login


def open_folder():
    directory_entry.config(state='normal')
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        # Clear the existing content of the Entry widget
        directory_entry.delete(0, tk.END)
        # Insert the new folder path
        directory_entry.insert(0, folder_selected)
    directory_entry.config(state='disabled')


def save_default_config():
    # messagebox.showinfo("Exiting", "Saving current configuration...")
    exit_message = Message(text="Saving current configuration...")
    Message.place(exit_message, x=300, y=300)
    config_file = "autosave.json"
    config_data = {
        'username': username_entry.get(),
        'password': password_entry.get(),
        'folder_path': directory_entry.get(),
        'hashtags': hashtags_entry.get("1.0", "end-1c"),
        'call_to_action': calltoaction_entry.get("1.0", "end-1c"),
        'proxy': proxy_entry.get(),
        'sleep': sleep_entry.get()
    }
    with open(config_file, 'w') as file:
        json.dump(config_data, file)


def save_config():
    # messagebox.showinfo("Exiting", "Saving current configuration...")
    config_file = (filedialog.asksaveasfilename
                   (defaultextension=".json", filetypes=[("JSON files", "*.json")]))
    config_data = {
        'username': username_entry.get(),
        'password': password_entry.get(),
        'folder_path': directory_entry.get(),
        'hashtags': hashtags_entry.get("1.0", "end-1c"),
        'call_to_action': calltoaction_entry.get("1.0", "end-1c"),
        'proxy': proxy_entry.get(),
        'sleep': sleep_entry.get()
    }
    with open(config_file, 'w') as file:
        json.dump(config_data, file)
    return print("Configuration saved.")


def load_default_config():
    config_file = "autosave.json"
    try:
        with open(config_file, 'r') as file:
            config_data = json.load(file)
            username_entry.delete(0, tk.END)
            username_entry.insert(0, config_data.get('username', ''))
            password_entry.delete(0, tk.END)
            password_entry.insert(0, config_data.get('password', ''))
            directory_entry.delete(0, tk.END)
            directory_entry.insert(0, config_data.get('folder_path', ''))
            hashtags_entry.delete("1.0", tk.END)
            hashtags_entry.insert("1.0", config_data.get('hashtags', ''))
            calltoaction_entry.delete("1.0", tk.END)
            calltoaction_entry.insert("1.0", config_data.get('call_to_action', ''))
            proxy_entry.delete(0, tk.END)
            proxy_entry.insert(0, config_data.get('proxy', ''))
            sleep_entry.delete(0, tk.END)
            sleep_entry.insert(0, config_data.get('sleep', ''))
    except FileNotFoundError:
        pass


"""def show_loading_screen():
    global loading_label
    loading_label = tk.Label(window, text="Loading previous config...", anchor='center')
    loading_label.place(x=300, y=300)
    window.after(100, lambda: load_default_config())  # Delay call to give time for window update"""


def load_config():
    config_file = (filedialog.askopenfilename
                   (defaultextension=".json", filetypes=[("JSON files", "*.json")]))
    try:
        with open(config_file, 'r') as file:
            config_data = json.load(file)
            username_entry.delete(0, tk.END)
            username_entry.insert(0, config_data.get('username', ''))
            password_entry.delete(0, tk.END)
            password_entry.insert(0, config_data.get('password', ''))
            directory_entry.delete(0, tk.END)
            directory_entry.insert(0, config_data.get('folder_path', ''))
            hashtags_entry.delete("1.0", tk.END)
            hashtags_entry.insert("1.0", config_data.get('hashtags', ''))
            calltoaction_entry.delete("1.0", tk.END)
            calltoaction_entry.insert("1.0", config_data.get('call_to_action', ''))
            proxy_entry.delete(0, tk.END)
            proxy_entry.insert(0, config_data.get('proxy', ''))
            sleep_entry.delete(0, tk.END)
            sleep_entry.insert(0, config_data.get('sleep', ''))
    except FileNotFoundError:
        pass


def toggle_password_and_icon():
    global is_password_icon_toggled
    # Toggle password visibility
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        hide_button.config(text='Show Password')
        # Set the button icon for the "password hidden" state
        hide_button.config(image=eye_off_image)
        is_password_icon_toggled = False
    else:
        password_entry.config(show='')
        hide_button.config(text='Hide Password')
        # Set the button icon for the "password shown" state
        hide_button.config(image=eye_on_image)
        is_password_icon_toggled = True


def countdown_sleep(duration, interval=5):
    """
    Sleep for a specified duration, printing the time remaining every interval seconds.

    :param duration: Total sleep time in seconds.
    :param interval: Interval in seconds at which to print the remaining time.
    """
    remaining = duration
    while remaining > 0:
        print(f"Sleeping for {int(remaining // 60)} more minutes...")
        time.sleep(min(interval, remaining))
        remaining -= interval


window = tk.Tk()
window.title("instabot")
# window.overrideredirect(True)
window.iconphoto(False, PhotoImage(file=relative_to_assets(r"***REMOVED***instapi_2.png")))
"""tabConbtrol = ttk.Notebook(window)
tab1 = ttk.Frame(tabConbtrol)"""

window.geometry("700x900")
window.configure(bg="#2D2C2C")

canvas = Canvas(
    window,
    bg="#2D2C2C",
    height=900,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="flat"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("bg.png"))
image_1 = canvas.create_image(
    350.0,
    450.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("lines.png"))
image_2 = canvas.create_image(
    349.0,
    377.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    509.0,
    426.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    511.0,
    630.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    509.0,
    205.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    159.0,
    173.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    159.0,
    240.0,
    image=image_image_7
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
info_button_2 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("info_button_2 clicked: info for directory"),
    relief="flat",
    activebackground="#2D2C2C"
)
info_button_2.place(
    x=274.0,
    y=341.0,
    width=20.0,
    height=20.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
info_button_3 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("info_button_3 clicked: info for options"),
    relief="flat",
    activebackground="#2D2C2C"
)
info_button_3.place(
    x=274.0,
    y=457.0,
    width=20.0,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
info_button_5 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("info_button_5 clicked: info for hashatags"),
    relief="flat",
    activebackground="#2D2C2C"
)
info_button_5.place(
    x=647.0,
    y=341.0,
    width=20.0,
    height=20.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
info_button_1 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("info_button_1 clicked: info for login"),
    relief="flat",
    activebackground="#2D2C2C"
)
info_button_1.place(
    x=274.0,
    y=123.0,
    width=20.0,
    height=20.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
info_button_4 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("info_button_4 clicked: info for call-to-action"),
    relief="flat",
    activebackground="#2D2C2C"
)
info_button_4.place(
    x=646.0,
    y=124.0,
    width=20.0,
    height=20.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
directory_button = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_folder(),
    relief="flat",
    activebackground="#2D2C2C"
)
directory_button.place(
    x=252.0,
    y=363.0,
    width=23.0,
    height=23.0
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    143.0,
    374.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    162.0,
    509.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    70.0,
    568.0,
    image=image_image_10
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
sleep_minus_button = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("sleep_minus_button clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
sleep_minus_button.place(
    x=103.0,
    y=553.0,
    width=30.0,
    height=30.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
sleep_plus_button = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("sleep_plus_button clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
sleep_plus_button.place(
    x=136.0,
    y=553.0,
    width=30.0,
    height=30.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("cog.png"))
settings_button = Menubutton(
    # image=button_image_9,
    text="CONFIGURATION",
    font=("Inter Bold", 14 * -1),
    fg="grey",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#2D2C2C",
    disabledforeground="#464646",
    activeforeground="#FFFFFF",
)
settings_button.place(
    x=570.0,
    y=14.0,
    width=120.0,
    height=18.0
)
dropdown_menu = Menu(settings_button, tearoff=False, bg="#2D2C2C", fg="grey", activeforeground="white",
                     font=("Inter SemiBold", 12 * -1), activebackground="#2D2C2C")
settings_button.config(menu=dropdown_menu, background="#2D2C2C", activebackground="#2D2C2C")
dropdown_menu.add_command(label="Save config", command=save_config)
dropdown_menu.add_command(label="Load config", command=load_config)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
start_button = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_start(),
    relief="flat",
    activebackground="#2D2C2C"
)
start_button.place(
    x=257.0,
    y=786.0,
    width=186.0,
    height=36.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("stop.png"))
stop_button = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(directory_entry.get()),
    relief="flat",
    activebackground="#2D2C2C"
)
stop_button.place(
    x=257.0,
    y=832.0,
    width=186.0,
    height=36.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("login.png"))
login_button = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_login(),
    relief="flat",
    activebackground="#2D2C2C"
)
login_button.place(
    x=257.0,
    y=740.0,
    width=186.0,
    height=36.0
)
eye_on_image = PhotoImage(
    file=relative_to_assets("eye_on.png"))
eye_off_image = PhotoImage(
    file=relative_to_assets("eye_off.png"))
hide_button = Button(
    image=eye_off_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: toggle_password_and_icon(),
    relief="flat",
    activebackground="#2D2C2C",
    bg="#2D2C2C"
)
hide_button.place(
    x=270.0,
    y=229.0,
    width=24.0,
    height=22.0
)

image_image_13 = PhotoImage(
    file=relative_to_assets("login_info.png"))
image_13 = canvas.create_image(
    352.0,
    808.0,
    image=image_image_13
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    509.0,
    427.0,
    image=entry_image_1
)
hashtags_entry = Text(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    cursor="",
    font=("Inter SemiBold", 14 * -1)
)
hashtags_entry.place(
    x=380.0,
    y=367.0,
    width=258.0,
    height=118.0
)

hashtags_entry.configure(insertbackground='white')

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    511.0,
    630.5,
    image=entry_image_2
)
console = Text(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 12 * -1)
)
console.place(
    x=351.0,
    y=568.0,
    width=320.0,
    height=127.0
)

console.configure(insertbackground='white', state='disabled')

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    509.0,
    205.5,
    image=entry_image_3
)
calltoaction_entry = Text(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
calltoaction_entry.place(
    x=380.0,
    y=147.0,
    width=258.0,
    height=115.0
)

calltoaction_entry.configure(insertbackground='white')

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    159.5,
    173.0,
    image=entry_image_4
)
username_entry = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
username_entry.place(
    x=62.0,
    y=162.0,
    width=195.0,
    height=20.0
)

username_entry.configure(insertbackground='white')

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    159.5,
    240.0,
    image=entry_image_5
)
password_entry = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1),
    show="*"
)
password_entry.place(
    x=62.0,
    y=229.0,
    width=195.0,
    height=20.0
)

password_entry.configure(insertbackground='white')

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    143.5,
    374.0,
    image=entry_image_6
)
directory_entry = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1),
    disabledbackground="#464646"
)
directory_entry.place(
    x=46.0,
    y=363.0,
    width=195.0,
    height=20.0
)

directory_entry.configure(insertbackground='white', state='disabled')

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    163.0,
    508.5,
    image=entry_image_7
)
proxy_entry = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
proxy_entry.place(
    x=46.0,
    y=497.0,
    width=234.0,
    height=21.0
)

proxy_entry.configure(insertbackground='white')

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    70.5,
    568.0,
    image=entry_image_8
)
sleep_entry = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
sleep_entry.place(
    x=44.0,
    y=555.0,
    width=53.0,
    height=24.0
)

sleep_entry.configure(insertbackground='white')

canvas.create_text(
    370.0,
    325.0,
    anchor="nw",
    text="hashtags",
    fill="#C0C0C0",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    347.0,
    536.0,
    anchor="nw",
    text="console",
    fill="#C0C0C0",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    62.0,
    132.0,
    anchor="nw",
    text="username",
    fill="#C0C0C0",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    62.0,
    199.0,
    anchor="nw",
    text="password",
    fill="#C0C0C0",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    52.0,
    104.0,
    anchor="nw",
    text="instagram login",
    fill="#C0C0C0",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    52.0,
    325.0,
    anchor="nw",
    text="directory",
    fill="#C0C0C0",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    41.0,
    470.0,
    anchor="nw",
    text="proxy",
    fill="#C0C0C0",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    41.0,
    529.0,
    anchor="nw",
    text="sleep",
    fill="#C0C0C0",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    52.0,
    436.0,
    anchor="nw",
    text="options",
    fill="#C0C0C0",
    font=("Inter SemiBold", 16 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    349.0,
    27.0,
    image=image_image_11
)

tab_image_1 = PhotoImage(
    file=relative_to_assets("instabot_1.png"))
button_12 = Button(
    image=tab_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("instabot clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)

tab_1 = Button(
    image=tab_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("tab_1 clicked"),
    relief="flat",
    activebackground="#2D2C2C",
    bg="#2D2C2C"
)
tab_1.place(
    x=56.0,
    y=52.0,
    width=80.0,
    height=20.0
)

canvas.create_text(
    163.0,
    52.0,
    anchor="nw",
    text="follow/like",
    fill="#464646",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    290.0,
    52.0,
    anchor="nw",
    text="downloader",
    fill="#464646",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    432.0,
    52.0,
    anchor="nw",
    text="openai",
    fill="#464646",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    226.0,
    475.0,
    anchor="nw",
    text="optional",
    fill="#949494",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    48.0,
    585.0,
    anchor="nw",
    text="minutes",
    fill="#464646",
    font=("Inter SemiBold", 11 * -1)
)

canvas.create_text(
    370.0,
    104.0,
    anchor="nw",
    text="call-to-action",
    fill="#C0C0C0",
    font=("Inter SemiBold", 16 * -1)
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    282.0,
    22.0,
    image=image_image_12
)

"""# tabConbtrol.add(tab1, text=str(instabot))
tabConbtrol.pack(expand=1)
ttk.Label(tab1, text="HI").grid(column=0, row=0, padx=30, pady=30)"""
# CLI redirect to app console
sys.stdout = StdoutRedirector(console)

# Load the configuration on startup
window.after(400, load_default_config)  # Delay call to give time for window update

# tracks the hide password button's state
is_password_icon_toggled = False

# Save configuration upon exiting
window.protocol("WM_DELETE_WINDOW", lambda: [save_default_config(), window.destroy()])

window.resizable(False, False)
window.mainloop()
