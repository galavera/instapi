***REMOVED***
***REMOVED***


from pathlib import Path

#from tkinter import *

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"***REMOVED***")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("instabot")
# window.overrideredirect(True)
window.iconphoto(False, PhotoImage(file=relative_to_assets(r"***REMOVED***instapi_2.png")))
tabConbtrol = ttk.Notebook(window)
tab1 = ttk.Frame(tabConbtrol)

window.geometry("700x900")
window.configure(bg="#2D2C2C")

canvas = Canvas(
    window,
    bg="#2D2C2C",
    height=900,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350.0,
    450.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
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
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_1.place(
    x=274.0,
    y=341.0,
    width=20.0,
    height=20.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_2.place(
    x=274.0,
    y=457.0,
    width=20.0,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_3.place(
    x=647.0,
    y=341.0,
    width=20.0,
    height=20.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_4.place(
    x=274.0,
    y=123.0,
    width=20.0,
    height=20.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_5.place(
    x=646.0,
    y=124.0,
    width=20.0,
    height=20.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_6.place(
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
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_7.place(
    x=103.0,
    y=553.0,
    width=30.0,
    height=30.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_8.place(
    x=136.0,
    y=553.0,
    width=30.0,
    height=30.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_9.place(
    x=637.0,
    y=12.0,
    width=38.0,
    height=38.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat",
    activebackground="#2D2C2C"
)
button_10.place(
    x=196.0,
    y=796.0,
    width=308.0,
    height=64.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    509.0,
    427.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    cursor="",
    font=("Inter SemiBold", 14 * -1)
)
entry_1.place(
    x=380.0,
    y=367.0,
    width=258.0,
    height=118.0
)

entry_1.configure(insertbackground='white')

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    511.0,
    630.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 12 * -1)
)
entry_2.place(
    x=351.0,
    y=568.0,
    width=320.0,
    height=123.0
)

entry_2.configure(insertbackground='white')

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    509.0,
    205.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14*-1)
)
entry_3.place(
    x=380.0,
    y=147.0,
    width=258.0,
    height=115.0
)

entry_3.configure(insertbackground='white')

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    159.5,
    173.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
entry_4.place(
    x=62.0,
    y=162.0,
    width=195.0,
    height=20.0
)

entry_4.configure(insertbackground='white')

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    159.5,
    240.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
entry_5.place(
    x=62.0,
    y=229.0,
    width=195.0,
    height=20.0
)

entry_5.configure(insertbackground='white')

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    143.5,
    374.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
entry_6.place(
    x=46.0,
    y=363.0,
    width=195.0,
    height=20.0
)

entry_6.configure(insertbackground='white')

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    163.0,
    508.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
entry_7.place(
    x=46.0,
    y=497.0,
    width=234.0,
    height=21.0
)

entry_7.configure(insertbackground='white')

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    70.5,
    568.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#464646",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter SemiBold", 14 * -1)
)
entry_8.place(
    x=44.0,
    y=555.0,
    width=53.0,
    height=24.0
)

entry_8.configure(insertbackground='white')

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

instabot = canvas.create_text(
    56.0,
    52.0,
    anchor="nw",
    text="instabot",
    fill="#1DC4DC",
    font=("Inter SemiBold", 20 * -1)
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

tabConbtrol.add(tab1, text=str(instabot))
tabConbtrol.pack(expand=1)
ttk.Label(tab1, text="HI").grid(column=0, row=0, padx=30, pady=30)

window.resizable(False, False)
window.mainloop()
