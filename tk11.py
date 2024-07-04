from tkinter import * #import everything
from tkinter import ttk

class startFish():
    def __init__(self):
        SIZE = 80

        #create window and set title
        self.mainWindow = Tk()
        self.mainWindow.title('GUI-Practice')
        self.mainWindow.geometry('500x250')       

        titleLabel = Label(self.mainWindow, text="How would you like the list of fish sorted?")
        titleLabel.pack()

        self.var = IntVar()
        R1 = Radiobutton(self.mainWindow, text="Alphabetical", variable = self.var, value = 1)
        R1.pack(side=LEFT, anchor=N)
        R2 = Radiobutton(self.mainWindow, text="Reverse Alphabetical", variable = self.var, value = 2)
        R2.pack(side=LEFT, anchor=N)

        self.testLabel = Label(self.mainWindow, text="Hellos")
        self.testLabel.pack(side=RIGHT)

        self.forwardButton = Button(self.mainWindow, text="Select", command=self.fowardButton_Click).pack(side=LEFT)
        self.exitButton = Button(self.mainWindow, text="Exit", command=self.mainWindow.destroy).pack(side=LEFT)


    def fowardButton_Click(self):
        radioVal= self.var.get()
        self.testLabel.configure(text=radioVal)

        self.mainWindow.mainloop()
