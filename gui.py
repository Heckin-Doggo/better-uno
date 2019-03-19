from tkinter import Tk, Label, Button, StringVar
import random

class MyGUI:
    LABEL_TEXT = [
        "click me!",
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


def get_deck():
    deck = []
    # The below just creates the deck.
    for color in ["RED", "GREEN", "BLUE", "YELLOW"]:
        # Cards 0-9
        for i in range(1): # TODO: SET BACK TO 10
            deck.append(color + " " + str(i))
        # Another set of 1-9
        for i in range(1, 2):  # TODO: SET THE 2 to 10
            deck.append(color + " " + str(i))
        # Action Cards
        deck.append(color + " REVERSE")
        deck.append(color + " REVERSE")
        deck.append(color + " SKIP")
        deck.append(color + " SKIP")
        deck.append(color + " DRAW 2")
        deck.append(color + " DRAW 2")

    # Wild Cards
    for i in range(4):
        deck.append("WILDCARD")
        deck.append("WILD +4")

    random.shuffle(deck)
    return deck


root = Tk()
my_gui = MyGUI(root)

if __name__ == '__main__':
    root.mainloop()
