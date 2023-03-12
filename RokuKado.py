from random import randint

from dataclasses import field
from dataclasses import dataclass


CARD_VALUES = {
    '3': 1, '4': 2, '5': 3, 
    '6': 4, '7': 5, '8': 6, 
    '9': 7, '10': 8, 'J': 9, 
    'Q': 10, 'K': 11, 'A': 12, '2': 13
    }

@dataclass
class Player:
    """
    Class for keeping track of a player's stats.

    Keyword arguments:
    * name (str)    --  no default
    * cards (list)  --  no default
    * money (int)   --  0
    * wins (int)    --  0
    * losses (int)  --  0
    """
    name: str = ''
    cards: list = field(default_factory=list)

    money: int = 0
    wins: int = 0
    losses: int = 0

player1 = Player('player_01')
player2 = Player('player_02')
players = [player1, player2]


def distribute_cards(player_list, card_values, max_card=10):
    card_deck = list(card_values) * 4

    for player in player_list:
        while len(player.cards) < max_card:
            ran_num = card_deck[randint(0, len(card_deck) - 1)]
            player.cards.append(ran_num)
            card_deck.pop(card_deck.index(ran_num))
        player.cards = sorted(player.cards, key=card_values.__getitem__)
    print(card_deck, len(card_deck))
    return player_list


players = distribute_cards(players, CARD_VALUES)
for player in players:
    print(player.cards, len(player.cards))

