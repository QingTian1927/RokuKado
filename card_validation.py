CARD_VALUES = {
    '3': 1, '4': 2, '5': 3, 
    '6': 4, '7': 5, '8': 6, 
    '9': 7, '10': 8, 'J': 9, 
    'Q': 10, 'K': 11, 'A': 12, '2': 13
    }


def decode_cards(cards, card_values):
    translated_cards = []
    for card in cards:
        translated_cards.append(card_values[card])
    return translated_cards


def validate_cards(cards, max_card=10):
    len_cards = len(cards)

    if len_cards > max_card:
        raise OverflowError

    if len_cards <= 0:
        raise UnboundLocalError

    first_two_equal = cards[0] == cards[1]
    if len_cards == 2 and not first_two_equal:
        raise ValueError
    if len_cards == 5 and first_two_equal:
        raise ValueError


def compare_played_cards(played_cards, input_cards):
    validate_cards(input_cards)

    if played_cards[0] == input_cards[0]:
        raise ValueError

    played_type = get_card_type(played_cards)
    input_type = get_card_type(input_cards)

    played_decoded = decode_cards(played_cards, CARD_VALUES)
    input_decoded = decode_cards(input_cards, CARD_VALUES)
    equal_types = ('single', 'double', 'triple', 'quadtuple')

    if played_cards == '2' and input_type in ('quadtuple', 'equalizer'):
        return True

    if len(input_cards) != len(played_cards):
        raise IndexError

    if played_type != input_type:
        raise TypeError

    if input_type in equal_types:
        if sum(input_decoded) > sum(played_decoded):
            return True

    if input_type == 'series':
        for index, val_input in enumerate(input_cards):
            val_played = played_cards[index]
            if val_input <= val_played:
                raise ValueError
        return True
    raise ValueError


def get_card_type(cards):
    ori_cards = cards
    cards = decode_cards(cards, CARD_VALUES)
    len_cards = len(cards)

    if len_cards == 1:
        return 'single'

    if cards[0] == cards[1]:
        return equal_type_cards(cards)

    if cards[0] == cards[1] - 1:
        return series_type_cards(cards)

    raise TypeError(f"{ori_cards=}")


def series_type_cards(cards):
    for index, card in enumerate(cards):
        if card == cards[0]:
            continue
        prev_card = cards[index - 1]
        if card != prev_card + 1:
            raise TypeError(f"{prev_card=} {card=} {cards=}")
    return 'series'


def equal_type_cards(cards):
    len_cards = len(cards)

    if 2 <= len_cards <= 4:
        card_groups = {2: 'double', 3: 'triple', 4: 'quadtuple'}
        card_count = cards.count(cards[0])
        if card_count in card_groups:
            return card_groups[card_count]

    if len_cards == 6:
        second_set_equal = cards[2] == cards[3] == cards[0] + 1
        third_set_equal = cards[4] == cards[5] == cards[0] + 2
        if second_set_equal and third_set_equal:
            return 'equalizer'

    if len_cards % 2 == 0:
        for index, card in enumerate(cards, start=1):
            if card == cards[0] or index % 2 != 0:
                continue
            paired_card = cards[index - 1]
            if paired_card != card:
                raise TypeError(f"{index=} {paired_card=} {card=} {cards=}")
        return 'all_double'
    raise ValueError

