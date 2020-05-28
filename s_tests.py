from spades import spades, round, score_tables, player, deck, card


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
    print(d.values)

def player_rotate_test():
    players = [player("A"), player("B"), player("C"), player("D")]
    s = spades(players, 10)
    for i in range(0,10):
        print("Rotating")
        s.rotate_players()

if __name__ == "__main__":
    select_trump_test()