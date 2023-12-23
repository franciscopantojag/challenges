card_ranking = [*[str(num) for num in range(2, 10)], 'T', 'J', 'Q', 'K', 'A']


def card_appear(hand: 'str', num: 'int'):
    hand_cards = list(hand)
    for card in hand_cards:
        appear = len(hand.split(card)) - 1
        if appear == num:
            return True
    return False


def get_hand_cards_bid(line: 'str'):
    [hand, bid] = line.split(" ")
    cards = list(hand)
    bid = int(bid)
    return hand, cards, bid


def define_ranking(hand: 'str'):
    hand_cards = list(hand)
    hand_cards_set_len = len(set(hand_cards))

    if hand_cards_set_len == 1:
        return 7

    if hand_cards_set_len == 2:
        if card_appear(hand, 4):
            return 6

        return 5

    if hand_cards_set_len == 3:
        if card_appear(hand, 3):
            return 4

        return 3

    if hand_cards_set_len == 4:
        return 2

    return 1


def sorted_by(line1: 'str', line2: 'str'):
    # logic here
    hand1, cards1, bid1 = get_hand_cards_bid(line1)
    hand2, cards2, bid2 = get_hand_cards_bid(line2)

    rank1 = define_ranking(hand1)
    rank2 = define_ranking(hand2)

    if rank1 != rank2:
        return rank1 - rank2

    for index1, card1 in enumerate(cards1):
        card2 = cards2[index1]

        index1 = card_ranking.index(card1)
        index2 = card_ranking.index(card2)

        if index2 != index1:
            return index1 - index2

    return 1


def reducer(acc: 'int', el: 'tuple[int, str]'):
    index, line = el
    rank = index + 1
    _, __,  bid = get_hand_cards_bid(line)

    return acc + (bid * rank)
