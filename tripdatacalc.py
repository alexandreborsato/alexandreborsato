import tkinter as tk
from tkinter import messagebox

class TripCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Trip Calculator")

        # Create left window elements
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, padx=20, pady=20)

        tk.Label(left_frame, text="Trip 1").pack()
        self.distance1 = tk.StringVar()
        self.time1 = tk.StringVar()
        self.consumption1 = tk.StringVar()
        tk.Label(left_frame, text="Distance (km):").pack()
        tk.Entry(left_frame, textvariable=self.distance1).pack()
        tk.Label(left_frame, text="Time (hours):").pack()
        tk.Entry(left_frame, textvariable=self.time1).pack()
        tk.Label(left_frame, text="Gas Consumption (liters):").pack()
        tk.Entry(left_frame, textvariable=self.consumption1).pack()

        tk.Label(left_frame, text="Trip 2").pack()
        self.distance2 = tk.StringVar()
        self.time2 = tk.StringVar()
        self.consumption2 = tk.StringVar()
        tk.Label(left_frame, text="Distance (km):").pack()
        tk.Entry(left_frame, textvariable=self.distance2).pack()
        tk.Label(left_frame, text="Time (hours):").pack()
        tk.Entry(left_frame, textvariable=self.time2).pack()
        tk.Label(left_frame, text="Gas Consumption (liters):").pack()
        tk.Entry(left_frame, textvariable=self.consumption2).pack()

        tk.Button(left_frame, text="Calculate", command=self.calculate).pack()

        # Create right window elements
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        self.result_label = tk.Label(right_frame, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            distance1 = float(self.distance1.get())
            time1 = float(self.time1.get())
            consumption1 = float(self.consumption1.get())
            distance2 = float(self.distance2.get())
            time2 = float(self.time2.get())
            consumption2 = float(self.consumption2.get())

            average_speed1 = distance1 / time1
            average_speed2 = distance2 / time2
            average_consumption1 = distance1 / consumption1
            average_consumption2 = distance2 / consumption2

            if average_speed1 > average_speed2:
                faster_driver = "Driver 1"
            elif average_speed1 < average_speed2:
                faster_driver = "Driver 2"
            else:
                faster_driver = "Both drivers have the same average speed"

            result_text = f"Trip 1:\nAverage Speed: {average_speed1:.2f} km/h\nAverage Gas Consumption: {average_consumption1:.2f} km/l\n\n"
            result_text += f"Trip 2:\nAverage Speed: {average_speed2:.2f} km/h\nAverage Gas Consumption: {average_consumption2:.2f} km/l\n\n"
            result_text += f"Faster Driver: {faster_driver}"

            self.result_label.config(text=result_text)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TripCalculator(root)
    root.mainloop()
