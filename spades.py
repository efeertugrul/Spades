import numpy as np
import random
import pandas as pd

## Koz maça

"""
Deck is created.
Card shuffle added.
Player card sort added.
Table of scores is added.
# TODO:
Round needs to be modified.
    play function should be added

Bids needs to be modified.
"""
class spades:
    def __init__(self, players):
        if(len(players)!=4):
            raise "Number of players is not 4."
        self.players = players

        self.current_round_no = 0
        self.current_round = None
        #rounds are held in a list
        self.previous_rounds = []

class round:
    def __init__(self):

        self.deck = deck()

        self.trump = 0

        self.bids = []

        self.current_player = 0

        self.current_turn = 0

    def shuffle_deck(self):
        self.deck.shuffle_cards();

    def play(self):
        pass

class score_tables:
    def __init__(self, player_names):
        if((type(player_names) != np.ndarray) or  (type(player_names)!= list)):
            raise "The player_names is not list or numpy array."

        self.scores = pd.DataFrame(columns = player_names)

    def add_score_row(self, score_dict):
        if(len(score_array)!=4):
            raise "Invalid length of array: {}".format(len(score_array))

        self.scores = self.scores.append([score_dict])

    def __getitem__(self, args):
        if(type(args)==str):
            return self.scores.loc[args]
        elif(type(args)==slice or type(args)==int):
            return self.scores.iloc[args]
        else:
            raise "Type Error, {} is not slice or integer".format(args)

    def __str__(self):
        return self.scores

    __repr__ = __str__

class player:

    def __init__(self, name):
        self.name = name
        self.cards = np.ndarray((13), card)

    def gather_cards(self, cards):
        self.cards = cards

    def sort_cards(self):
        """
        Sorts the cards by comparing their suits and values.

        Check __ge__ function in card class
        """

        #Bubble sort is used just because this was the shortest sorting algorithm code i've found

        def swap(i, j):
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

        n = len(self.cards)
        swapped = True
        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if self.cards[i - 1] >= self.cards[i]:
                    swap(i - 1, i)
                    swapped = True

    def bid(self, number):
        return number


class deck:

    def __init__(self):
        self.cards = np.ndarray((52), card)
        card_suits = ["Karo", "Maca", "Kupa", "Sinek"]
        face_cards = [" Vale", " Kiz", " Papaz", " As"]
        name = ""

        for i in range(4,40):
            name = card_suits[i%4] + " {}".format(int(i/4)+1)
            self.cards[i-4] = card(i-4, name, card_suits[i%4])

        for i in range(40,56):
            name = card_suits[i%4] + face_cards[(int(i/4)+1)%11]
            self.cards[i-4] = card(i-4, name, card_suits[i%4])

    def shuffle_cards(self):
        np.random.shuffle(self.cards)

    def __getitem__(self, arg):
        return self.cards[arg]

    def __repr__(self):
        representation = ""
        for i in range(len(self.cards)):
            representation = representation + str(self.cards[i]) + "\n"
        return representation

    __str__ = __repr__

class card:

    def __init__(self, card_no, card_name, suit):
        self.card_no = card_no
        self.card_name = card_name
        self.value =  int(card_no/4)+1
        self.suit = suit

    def __str__(self):
        return self.card_name

    def __lt__(self,other):
        return (self.value < other.value)

    def __le__(self,other):
        return(self.value <= other.value)

    def __gt__(self,other):
        return(self.value > other.value)

    ## This operation (>=)  will be used for sorting the cards
    def __ge__(self,other):
        """
        For simulating the card order in players hand
        "Karo" < "Maca" < "Kupa" < "Sinek"
        """

        if(self.suit == other.suit):
            return(self.value > other.value)
        else:
            return (self.card_no%4) > (other.card_no%4)

    def __eq__(self,other):
        return (self.value == other.value)

    def __ne__(self,other):
        return not(self.__eq__(self, other))

    __repr__ = __str__


def main():
    pass

if __name__ == "__main__":
    main()
