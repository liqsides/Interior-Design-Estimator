import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def calc():
    bathvar = 200
    bedvar = 20
    kitvar = 75
    livvar = 25
    basvar = 40
    granvar = 1.8
    marvar = 2.5
    forvar = 0.5
    tilvar = 1.2
    harvar = 1.2
    carvar = 0.8

    entry1.set(e1.get())
    entry2.set(e2.get(e2.curselection()))

    foot = entry1.get()
    type = entry2.get()
    mat = entry3.get()

    footage = float(foot)
    typage = str(type)
    mats = str(mat)

    if typage == "Bathroom":
        cost = '$' + str(bathvar * footage)
        r1 = tk.Label(window, text=cost)
        r1.grid(row=7)
        r1.grid(column=1)

    if typage == "Bedroom":
        cost = "$" + str(bedvar * footage)
        r1 = tk.Label(window, text=cost)
        r1.grid(row=7)
        r1.grid(column=1)

    if typage == "Kitchen":
        cost = "$" + str(kitvar * footage)
        r1 = tk.Label(window, text=cost)
        r1.grid(row=7)
        r1.grid(column=1)

    if typage == "Living Room":
        cost = "$" + str(livvar * footage)
        r1 = tk.Label(window, text=cost)
        r1.grid(row=7)
        r1.grid(column=1)

    if typage == "Basement":
        cost = "$" + str(basvar * footage)
        r1 = tk.Label(window, text=cost)
        r1.grid(row=7)
        r1.grid(column=1)

window = tk.Tk()
window.title('Interior Design Estimator')
entry1 = StringVar()
entry2 = StringVar()
entry3 = StringVar()

l1 = tk.Label(window, text="Square Footage:").grid(row=0, column=1)
e1 = tk.Entry(window)
e1.grid(row=1)
e1.grid(column=1)

l2 = tk.Label(window, text='Remodel Type:').grid(row=3)
e2 = tk.Listbox(window, exportselection=0)
e2.insert(1, 'Bathroom')
e2.insert(2, 'Bedroom')
e2.insert(3, 'Kitchen')
e2.insert(4, 'Living Room')
e2.insert(5, 'Basement')
e2.grid(row=4)

l3 = tk.Label(window, text='Rough Estimate:').grid(row=6, column=1)

l4 = tk.Label(window, text='Materials:').grid(column=1, row=3)
e3 = tk.Listbox(window, exportselection=0, selectmode='multiple')
e3.insert(1, "Granite")
e3.insert(2, 'Marble')
e3.insert(3, 'Formicah')
e3.insert(4, 'Tile')
e3.insert(5, 'Hardwood')
e3.insert(6, 'Carpet')
e3.grid(column=1, row=4)

l5 = tk.Label(window, text='Utility/Major Reworks:').grid(column=2, row=3)
e4 = tk.Listbox(window, exportselection=0, selectmode='multiple')
e4.insert(1, 'Electric')
e4.insert(2, 'Plumbing')
e4.insert(3, 'Heat/AC')
e4.insert(4, 'Room Rebuild')
e4.insert(5, 'House Extension')
e4.grid(column=2, row=4)

button = tk.Button(window, text='Estimate', command=calc)
button.grid(column=1)
button.grid(row=5)

image = Image.open("C://Users//example//Pictures//company.jpg")
test = ImageTk.PhotoImage(image)
l6 = tk.Label(image=test)
l6.image = test
l6.grid(row=0)
l6.grid(rowspan=8)
l6.grid(column=5)


window.mainloop()

