from spades import spades, round, score_tables, player, deck, card, turn
import numpy as np

def cards_test():
    d = deck()
    d.shuffle_cards()
    for x in d:
        print(x, x.card_no)

def score_test():
    players = [player("A"), player("B"), player("C"), player("D")]

    scores = score_tables([x.name for x in players])
    scores.add_score_row([8,3,2,0])
    print(scores)
    scores.add_score_row([7,1,3,2])
    print(scores)

def select_trump_test():
    players = [player("A"), player("B"), player("C"), player("D")]
    r = round(players)
    d = deck()
    d.shuffle_cards()
    for p, i in zip(players, range(0,4)):
        p.gather_cards(d[i*13:(i+1)*13])
    r.get_bids()
    r.select_trump()


def player_rotate_test():
    players = [player("A"), player("B"), player("C"), player("D")]
    s = spades(players, 10)
    for i in range(0,10):
        print("Rotating")
        s.rotate_players()

def player_play_test():
    players = [player("A"), player("B"), player("C"), player("D")]
    r = round(players)
    r.shuffle_deck()
    r.deal_cards()
    r.get_bids()
    r.select_trump()
    #burada kaldık
    for p in players:
        for c in p.cards:
            print("Card:{}, value:{}".format(c, c.value))
    t = turn(False)
    t.play_turn(players, r.trump)

def max_test():
    c = []
    c.append(card(-4, "Karo 2", 2))
    c.append(card(-4, "Sinek 2", 3))
    c.append(card(1, "Kupa 2", 0))
    c.append(card(1, "Maça 2", 1))
    print(max(c))

def first_play():
    p = player("A")
    p2 = player("B")
    d = deck()
    trump = 0
    d.shuffle_cards()
    c = []
    d.update_values(trump)
    p.gather_cards(np.array(d[:4].tolist() + d[8:10].tolist()))
    p2.gather_cards(np.array(d[:4].tolist() + d[8:10].tolist()))
    c.append(p.play(c, trump, False))
    c.append(p2.play(c, trump, False))


def player_card_play():

    p = player("A")
    d = deck()
    trump = 0
    d.shuffle_cards()
    c = d[4:7]
    print(c[0].suit)
    d.update_values(trump)
    p.gather_cards(np.array(d[:4].tolist() + d[8:10].tolist()))
    print(c)
    p.play(c, 0, True)

def where_test():
    d = deck()

    c = d[4:7]

    print(c[0].suit_to_int())

    d.update_values(c[2].suit_to_int())

    #suits = {"Karo": 0, "Maca": 1, "Kupa": 2, "Sinek": 3}

    c_max = max(c)

    ##print(c_max)

    index = np.where(d.cards > c[2])[0]
    print(c[2])
    print(np.where(d.cards > c[2])[0])

    print(d[index])


if __name__ == "__main__":
    player_play_test()
    #player_card_play()
    #select_trump_test()
    #where_test()
