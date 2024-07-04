# Python program to encript a plain text in a very simple way

import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter import filedialog

# Functions created below

def save_to_txt():
    user_input = input_entry.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, "w") as file:
            file.write(user_input)
        status_label.config(text="File saved successfully!")
        status_label.config(text=user_input)
        #status_label.config(text=user_entry)
        #status_label.config(text=self.user_entry)
    else:
        status_label.config(text="Save canceled.")

def char_array_to_int_array(char_array):
    int_array = [ord(char) for char in char_array]
    return int_array

def add_constant_to_array(arr, constant):
    return [num + constant for num in arr]

def int_array_to_char_array(int_array):
    cript_char_array = [chr(num) for num in int_array]
    return cript_char_array

def char_array_to_string(echar_array):
    return ''.join(echar_array)

def generate_output_file(output_filename, content):
    with open(output_filename, 'w') as file:
        file.write(content)

# Getting Initial Text and converting to array, and so, converting to ascii code;

# Create the main window
window = tk.Tk()
window.title("Plain Text to Encript")

# Create and position the widgets
input_label = tk.Label(window, text="Enter your text:")
input_label.pack(pady=10)

input_entry = tk.Entry(window, width=40)
input_entry.pack(pady=5)
#self.user_entry = tk.Entry(self.window)

save_button = tk.Button(window, text="Save to File", command=save_to_txt)
save_button.pack(pady=10)

status_label = tk.Label(window, text="", fg="green")
status_label.pack(pady=5)

# Start the main loop
window.mainloop()

# adding 3 to ascii code to codify so converting the original text into a coded text:
user_string = save_to_txt()                      # get_user_input()
string_length = len(user_string)
user_char_array = list(user_string)
user_int_array = char_array_to_int_array(user_char_array)
result_array = add_constant_to_array(user_int_array, 3)
encript_char_array = int_array_to_char_array(result_array)
encripted_user_string = char_array_to_string(encript_char_array)

MessageBox.showinfo("User String:", user_string)

MessageBox.showinfo("Encripted String:", encripted_user_string)

output_filename = "output.txt"
generate_output_file(output_filename, encripted_user_string)

# printing everything

print("User String:", user_string)
# print("Input Char Array:", user_char_array)
# print("Array Length:", string_length)
# print("Integer Array:", user_int_array)
# print("Result Array (with constant added):", result_array)
# print("Result Encripted Array:", encript_char_array)
print("Encripted String:", encripted_user_string)
print(f"File '{output_filename}' created with the given content.")
