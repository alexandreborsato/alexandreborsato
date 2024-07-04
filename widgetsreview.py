from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))


def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()) + ' k=' + str(w.winfo_rootx()) + ' kk=' + str(w.winfo_rooty()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

print_hierarchy(root)
