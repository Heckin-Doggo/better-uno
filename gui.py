from tkinter import Tk, Label, Button, StringVar

class MyGUI:
    LABEL_TEXT = [
        "This is just an ordinary GUI.",
        "Alas, it is not.",
        "We can change text!",
        "YEET"
    ]

    def __init__(self, master):
        self.master = master
        master.title("Test GUI 2")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])

        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="I dont know", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Hello!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # word wrap
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyGUI(root)

if __name__ == '__main__':
    root.mainloop()
