# this code is to show how tkinter responds to a serie ov events

from tkinter import *
from tkinter import ttk

# create the root window
# create a label and bind the events to the label
# create a function to handle the events
root = Tk()

w = 180 # width for the Tk root
h = 50 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

l =ttk.Label(root, text="Starting...")
l.grid()

# function to handle the events
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))

""" What's with the lambda expressions? Tkinter expects you to provide a function as the event callback, 
whose first argument is an event object representing the event that triggered the callback. 
It's sometimes not worth the bother of defining regular named functions for one-off trivial callbacks, such as in this example. 
Instead, we've just used Python's anonymous functions via lambda. In real applications, you'll almost always use a regular function, 
such as the calculate function in our feet to meters example, or a method of an object.
"""
root.mainloop()

"""
Available Events
The most commonly used events are described below, along with the circumstances when they are generated. 
Some are generated on some platforms and not others. For a complete description of all the different event names, modifiers, 
and the different event parameters that are available with each, the best place to look is the bind command reference.

<Activate>:
Window has become active.
<Deactivate>:
Window has been deactivated.
<MouseWheel>:
Scroll wheel on mouse has been moved.
<KeyPress>:
Key on keyboard has been pressed down.
<KeyRelease>:
Key has been released.
<ButtonPress>:
A mouse button has been pressed.
<ButtonRelease>:
A mouse button has been released.
<Motion>:
Mouse has been moved.
<Configure>:
Widget has changed size or position.
<Destroy>:
Widget is being destroyed.
<FocusIn>:
Widget has been given keyboard focus.
<FocusOut>:
Widget has lost keyboard focus.
<Enter>:
Mouse pointer enters widget.
<Leave>:
Mouse pointer leaves widget.
"""