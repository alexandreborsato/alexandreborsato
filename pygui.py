import tkinter as tk
from tkinter import filedialog

def save_to_txt():
    user_input = input_entry.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, "w") as file:
            file.write(user_input)
        status_label.config(text="File saved successfully!")
        status_label.config(text=user_input)
        
    else:
        status_label.config(text="Save canceled.")

# Create the main window
window = tk.Tk()
window.title("Save Input to Text File")

# Create and position the widgets
input_label = tk.Label(window, text="Enter your text:")
input_label.pack(pady=10)

input_entry = tk.Entry(window, width=40)
input_entry.pack(pady=5)

save_button = tk.Button(window, text="Save to File", command=save_to_txt)
save_button.pack(pady=10)

status_label = tk.Label(window, text="", fg="green")
status_label.pack(pady=5)

# Start the main loop
window.mainloop()
