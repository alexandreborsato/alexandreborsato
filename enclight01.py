# Python program to encript a plain text in a very simple way

import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter import filedialog
from tkinter import ttk 

class criptografia:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to be Encripted")

        # Create left window elements
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, padx=20, pady=20)

        tk.Label(left_frame, text="Add Text:").pack()
        self.distance1 = tk.StringVar()
        tk.Entry(left_frame, textvariable=self.distance1).pack()

        tk.Button(left_frame, text="Accept", command=self.calculate).pack()
            
        # Create right window elements
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        self.result_label = tk.Label(right_frame, text="")
        self.result_label.pack()

    def calculate(self):
        left_frame = tk.Frame(self.root)
        user_input = self.distance1.get()
        user_string = user_input
        string_length = len(user_string)
        user_char_array = list(user_string)
        user_int_array = [ord(char) for char in string_length]
        constant = 3
        tk.Button(left_frame, text="Transform", command=self.transform).pack()
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, "w") as file:
                file.write(user_input)
            status_label.config(text="File saved successfully!")
            status_label.config(text=user_input)
            return(user_input)
        else:
            status_label.config(text="Save canceled.")

    def transform(arr, constant):
            constant = 3
            return [num + constant for num in arr]

    def int_array_to_char_array(int_array):
        cript_char_array = [chr(num) for num in int_array]
        return cript_char_array

    def char_array_to_string(echar_array):
        return ''.join(echar_array)

    def generate_output_file(output_filename, content):
        with open(output_filename, 'w') as file:
            file.write(content)

    result_array = transform(user_int_array, 3)
    encript_char_array = int_array_to_char_array(result_array)
    encripted_user_string = char_array_to_string(encript_char_array)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = criptografia(root)
    root.mainloop()

