# new attempt to create a clear and user-friendly app to encript plain text

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class encript_text:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Encription")

        # Get the screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the center position
        center_x = int((screen_width - 600) / 2)
        center_y = int((screen_height - 300) / 2)

        # Set the window position
        self.root.geometry(f"300x150+{center_x}+{center_y}")

        # Create label and entry widgets
        tk.Label(self.root, text="Enter text to encript:").pack(pady=10)
        self.user_entry = tk.Entry(self.root)
        self.user_entry.pack(pady=5)

        tk.Button(self.root, text="Submit", command=self.display_user).pack()

    def display_user(self):
        user_string = self.user_entry.get()
        if user_string.strip() != "":

            user_char_array = list(user_string)
            string_length = len(user_string)
            int_array = [ord(char) for char in user_char_array]
            new_array = [num + 3 for num in int_array]
            encript_char_array = [chr(num) for num in new_array]
            encript_string = "".join(encript_char_array)
            
            messagebox.showinfo("String Encripted: ", {encript_string})
            
            tk.Button(self.root, text="Save source string", command=next)
            
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(user_string)
                    
            tk.Button(self.root, text="Save encripted string", command=next)
            
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(encript_string)
                
            else:
                root.config(text="Save canceled.")

        else:
            messagebox.showerror("Error", "Please enter a valid text.")

if __name__ == "__main__":
    root = tk.Tk()
    app = encript_text(root)
    root.mainloop()
    