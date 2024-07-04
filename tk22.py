
import tkinter as tk
from tkinter import ttk

def exit_function(usrdata):
    root.destroy()
    return usrdata
    print(usrdata)
    
def display_user_input():
    user_input = entry.get()
    if user_input:
        result_label.config(text=f"You entered: {user_input}")
        print(user_input)
        return user_input
    else:
        result_label.config(text="Please enter some text.")

def confirm_input():
    result_label.config(text=f"Operation Confirmed")
    exit()
    
root = tk.Tk()
root.title("User Input")

# Create the input field
label = ttk.Label(root, text="Enter some text:")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=10)

ee = entry

# Create the result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

user_data = ""
user_input = ""
tt = display_user_input()
user_data = exit_function(user_input)

print(user_input)
print(entry)
print(ee)
print("Alex")
# Create the confirmation button
confirm_button = ttk.Button(root, text="Confirm", command=confirm_input)
confirm_button.pack(pady=10)

root.mainloop()

print(user_input)
print(tt)
print(entry)
print(ee)
print("Alexandre")
