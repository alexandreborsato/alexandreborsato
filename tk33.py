import tkinter as tk
from tkinter import ttk

def display_user_input():
    text1 = entry1.get()
    text2 = entry2.get()
    if text1 and text2:
        result_label.config(text=f"You entered:\n1. {text1}\n2. {text2}")
        print(text1, text2)
        return text1, text2
    else:
        result_label.config(text="Please enter both texts.")

root = tk.Tk()
root.title("User Input")

# Create the input fields
label1 = ttk.Label(root, text="Enter the first text:")
label1.pack(pady=10)

entry1 = ttk.Entry(root)
entry1.pack(pady=10)

label2 = ttk.Label(root, text="Enter the second text:")
label2.pack(pady=10)

entry2 = ttk.Entry(root)
entry2.pack(pady=10)

# Create the result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

tt = display_user_input()

confirm_button = ttk.Button(root, text="Confirm", command=root.destroy)
confirm_button.pack(pady=10)

print(tt)

# Run the main loop
root.mainloop()

print("Alex")
print(tt)
