#python code to convert feet to meeters using a GUI - tkinter

#importing the necessary modules
#tkinter for creating the GUI - tkinter, is the standard binding to Tk. When imported, it loads the Tk library on your system.
#ttk for styling the GUI elements - ttk, is a submodule of tkinter. It implements Python's binding to the newer "themed widgets" that were added to Tk. It is a binding to the Tk themed widget set.
#StringVar for storing the user input
#IntVar for storing the calculated value

from tkinter import *
from tkinter import ttk

#defining the calculate function
#The try block attempts to convert the input value to a float and then performs the conversion.
""" 
The except block catches any ValueError exceptions that may occur if the user input is not a valid number.
If a ValueError occurs, the function simply returns without doing anything. This is a good practice to include,
as it prevents the program from crashing if the user enters invalid input. 

Here's where the magic textvariable options we specified when creating the widgets come into play. 
We specified the global variable feet as the textvariable for the entry. 
Whenever the entry changes, Tk will automatically update the global variable feet. 
Similarly, if we explicitly change the value of a textvariable associated with a widget (as we're doing for meters which 
is attached to our label), the widget will automatically be updated with the current contents of the variable. 
For Python, the only caveat is that these variables must be an instance of the StringVar class. Slick.
"""
def calculate(*args):
    try:
        value = float(feet.get())
        print(value)
        print(good)
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# setting up the main application window, giving to it the title "Feet to Meters."
root = Tk()
root.title("Feet to Meters")

#creating a mainframe for the application, padding it with 10 pixels on all sides.
#The mainframe is a container widget that holds all the other widgets in the application.
#The sticky option is used to align the widget within the container. N, S, E, and W represent the different directions.
#The columnconfigure and rowconfigure options are used to make the widgets resize with the mainframe.
#The columnconfigure/rowconfigure bits tell Tk that the frame should expand to fill any extra space if the window is resized.
#The weight option is used to determine how the widgets should be resized when the mainframe is resized.
#The padx and pady options are used to add padding around the widgets.

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#This is the feet entry widget, where the user will input the number of feet to convert.
#The textvariable option is used to bind the input field to the StringVar variable feet.
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
good = "good"

print("Alex")
print(good)
print(feet_entry)
# When create a widget, it is important to specify its parent. In this case, the meters label is a child of the mainframe.
# The textvariable option is used to bind the label to the StringVar variable meters, which will display the calculated value.
# The sticky option to grid describes how the widget should line up within the grid cell, using compass directions. 
# So w (west) means to anchor the widget to the left side of the cell, we (west-east) means to attach it to both the left and right sides,
# and so on. Python also defines constants for these directional strings, which you can provide as a list, e.g. W or (W, E).

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# This is how you run the main loop for the application. It listens for events (like button clicks or key presses)
# and allows the user to interact with the application.
# The for chield loop is used to iterate over all the widgets in the mainframe and configure their padding. 
# "padding" is the way how some spaces are added around the widgets. The padx and pady options are used to add padding
# The mainloop() function is the main event loop for the application. It handles all the GUI events and redraws the widgets
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# This line sets the focus on the feet_entry widget, so the user can immediately start typing in the input field.
# The bind() method is used to bind a function to a specific event. In this case, the <Return> event is bound to the calculate function.
# This means that when the user presses the Enter key, the calculate function will be called, and the conversion will be performed.
feet_entry.focus()
root.bind("<Return>", calculate)

# Finally, we start the main event loop for the application. This is where the application will wait for user input and respond accordingly.
root.mainloop()

print("iiiiiiiiiii")
print(good)
print(feet_entry)
print("iiiiiiiiiii")