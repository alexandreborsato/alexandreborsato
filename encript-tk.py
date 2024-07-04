# Python program to encript a plain text in a very simple way

import tkinter as tk
from tkinter import ttk

def display_user_input():
    global text1, text2
    text1 = entry1.get()
    text2 = entry2.get()
    if text1 and text2:
        result_label.config(text=f"You entered:\n1. {text1}\n2. {text2}\n\n >>> You may now close this window <<< ")
    else:
        result_label.config(text="Please fill both fields.")

root = tk.Tk()
root.title("Text to Encript")

# Create the input fields
label1 = ttk.Label(root, text="Enter the text to be encripted: ")
label1.pack(pady=10)

entry1 = ttk.Entry(root)
entry1.pack(pady=10)

label2 = ttk.Label(root, text="Enter the output file name (TXT): ")
label2.pack(pady=10)

entry2 = ttk.Entry(root)
entry2.pack(pady=10)

# Create the confirmation button
confirm_button = ttk.Button(root, text="Confirm", command=display_user_input)
confirm_button.pack(pady=10)

# Create the result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

# Use the saved text variables outside the Tkinter session
print(f"Text to encript: {text1}")
print(f"Output File Name: {text2}")

# Functions created below

#def get_user_input():
#    user_input = input("Please enter a plain text to encript: ")
#    return user_input

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
# adding 3 to ascii code to codify so converting the original text into a coded text:
user_string = text1
string_length = len(user_string)
user_char_array = list(user_string)
user_int_array = char_array_to_int_array(user_char_array)
result_array = add_constant_to_array(user_int_array, 3)
encript_char_array = int_array_to_char_array(result_array)
encripted_user_string = char_array_to_string(encript_char_array)

output_filename = text2
generate_output_file(output_filename, encripted_user_string)

# printing everything

print("User String:", user_string)
print("Input Char Array:", user_char_array)
print("Array Length:", string_length)
print("Integer Array:", user_int_array)
print("Result Array (with constant added):", result_array)
print("Result Encripted Array:", encript_char_array)
print("Encripted String:", encripted_user_string)
print(f"File '{output_filename}' created with the given content.")
