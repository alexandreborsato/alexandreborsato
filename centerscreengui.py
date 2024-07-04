import tkinter as tk
from tkinter import messagebox

class UserNameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Name App")

        # Get the screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the center position
        center_x = int((screen_width - 300) / 2)
        center_y = int((screen_height - 150) / 2)

        # Set the window position
        self.root.geometry(f"300x150+{center_x}+{center_y}")

        # Create label and entry widgets
        tk.Label(self.root, text="Enter your name:").pack(pady=10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        tk.Button(self.root, text="Submit", command=self.display_name).pack()

    def display_name(self):
        user_name = self.name_entry.get()
        if user_name.strip() != "":
            messagebox.showinfo("Welcome", f"Hello, {user_name}!")
        else:
            messagebox.showerror("Error", "Please enter a valid name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserNameApp(root)
    root.mainloop()
