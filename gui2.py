from tkinter import Tk, Label, Button, StringVar
import random


class UnoGUI:

    def __init__(self, master):
        self.master = master
        master.title("Test GUI 2")
        
        self.deck = self.get_deck()
        self.card = "nothing"

        self.label_text = StringVar()
        self.label_text.set(self.get_card(self.deck))

        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.get_card(self.deck))
        self.label.pack()

        self.card_button = Button(master, text="nab a card", command=self.get_card(self.deck))
        self.card_button.pack()

        self.close_button = Button(master, text="I dont know", command=master.quit)
        self.close_button.pack()
    
    
    def get_deck(self):
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
    
    def get_card(self, deck):
        card = deck.pop(0)
        self.card = card
        return card


root = Tk()
my_gui = UnoGUI(root)

if __name__ == '__main__':
    root.mainloop()
