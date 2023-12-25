from typing import Literal
JOKER_CARD = 'J'

card_ranking = [
    *[str(num) for num in range(2, 10)],
    'T', JOKER_CARD, 'Q', 'K', 'A'
]

card_ranking_part_two = [
    JOKER_CARD, *filter(lambda x: x != JOKER_CARD, card_ranking)
]


def get_rank_order(card_ranking: 'list[str]'):
    return {element: index for index, element in enumerate(card_ranking)}


rank_order_by_card = get_rank_order(card_ranking)
rank_order_by_card_part_two = get_rank_order(card_ranking_part_two)


def get_hand_bid(line: 'str'):
    [hand, bid] = line.strip().split(" ")
    return hand, int(bid)


class Hand:
    def __init__(self, hand: 'str') -> None:
        self.hand = hand
        self.cards = list(self.hand)
        self.cards_set = set(self.cards)
        self.cards_set_len = len(self.cards_set)
        self.has_joker = JOKER_CARD in self.cards_set

        self.card_appear_by_card: 'dict[str, int]' = {}
        self.cards_by_card_appear: 'dict[int, list[str]]' = {}

        for card in self.cards_set:
            card_appear = len(self.hand.split(card)) - 1
            self.card_appear_by_card[card] = card_appear

            self.cards_by_card_appear[card_appear] = [
                *self.cards_by_card_appear.get(card_appear, []),
                card
            ]

    def get_rank(self, is_part_two=False):
        should_optimize = self.has_joker and is_part_two

        if not should_optimize:
            mapper = {
                1: 7, 4: 2,
                2: 6 if self.cards_by_card_appear.get(4) else 5,
                3: 4 if self.cards_by_card_appear.get(3) else 3,
            }

            return mapper.get(self.cards_set_len, 1)

        joker_appear = self.card_appear_by_card.get(JOKER_CARD, 0)

        should_return_5_if_set_has_3 = joker_appear == 1 \
            and not self.cards_by_card_appear.get(3)

        mapper = {
            1: 7, 2: 7, 4: 4,
            3: 5 if should_return_5_if_set_has_3 else 6
        }
        return mapper.get(self.cards_set_len, 2)


def get_sorted_by(is_part_two=False):
    def sorted_by(line1: 'str', line2: 'str'):
        hand1 = Hand(get_hand_bid(line1)[0])
        hand2 = Hand(get_hand_bid(line2)[0])

        rank1 = hand1.get_rank(is_part_two)
        rank2 = hand2.get_rank(is_part_two)

        if rank1 != rank2:
            return rank1 - rank2

        for index1, card1 in enumerate(hand1.cards):
            card2 = hand2.cards[index1]

            rank_order = rank_order_by_card_part_two if is_part_two else rank_order_by_card
            rank1 = rank_order[card1]
            rank2 = rank_order[card2]

            if rank2 != rank1:
                return rank1 - rank2

        return 1

    return sorted_by


def reducer(acc: 'int', el: 'tuple[int, str]'):
    index, line = el
    rank = index + 1
    bid = get_hand_bid(line)[1]

    return acc + (bid * rank)
