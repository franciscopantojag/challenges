from re import S


card_ranking = [*[str(num) for num in range(2, 10)], 'T', 'J', 'Q', 'K', 'A']
rank_by_card_order = {element: index for index,
                      element in enumerate(card_ranking)}


def card_appear(hand: 'str', num: 'int'):
    hand_cards = list(hand)
    for card in hand_cards:
        appear = len(hand.split(card)) - 1
        if appear == num:
            return True
    return False


def get_hand_cards_bid(line: 'str'):
    line = line.strip()
    [hand, bid] = line.split(" ")
    cards = list(hand)
    bid = int(bid)
    return hand, cards, bid


def define_ranking(hand: 'str'):
    hand_cards = list(hand)
    hand_cards_set_len = len(set(hand_cards))

    initial_dic = {
        1: 7, 4: 2,
        2: 6 if card_appear(hand, 4) else 5,
        3: 4 if card_appear(hand, 3) else 3,
    }

    return initial_dic.get(hand_cards_set_len, 1)


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

        rank1 = rank_by_card_order[card1]
        rank2 = rank_by_card_order[card2]

        if rank2 != rank1:
            return rank1 - rank2

    return 1


def reducer(acc: 'int', el: 'tuple[int, str]'):
    index, line = el
    rank = index + 1
    _, __,  bid = get_hand_cards_bid(line)

    return acc + (bid * rank)
