JOKER_CARD = 'J'

card_ranking = [*[str(num) for num in range(2, 10)],
                'T', JOKER_CARD, 'Q', 'K', 'A']

card_ranking_part_two = [JOKER_CARD, *
                         filter(lambda x: x != JOKER_CARD, card_ranking)]


rank_order_by_card = {element: index for index,
                      element in enumerate(card_ranking)}

rank_order_by_card_part_two = {element: index for index,
                               element in enumerate(card_ranking_part_two)}


def get_hand_bid(line: 'str'):
    line = line.strip()
    [hand, bid] = line.split(" ")
    bid = int(bid)
    return hand, bid


class Hand:
    def __init__(self, hand: 'str') -> None:
        self.hand = hand
        self.cards = list(self.hand)
        self.cards_set = set(self.cards)
        self.cards_set_len = len(self.cards_set)
        self.has_joker = JOKER_CARD in self.cards_set

        self.random_card_no_joker = self.hand[0]
        card_appear_by_card: 'dict[str, int]' = {}
        cards_by_card_appear: 'dict[int, list[str]]' = {}

        for card in self.cards_set:
            if card != JOKER_CARD:
                self.random_card_no_joker = card

            card_appear = len(self.hand.split(card)) - 1
            card_appear_by_card[card] = card_appear

            card_li = cards_by_card_appear.get(card_appear, [])
            if card not in card_li:
                card_li.append(card)
            cards_by_card_appear[card_appear] = card_li

        self.card_appear_by_card = card_appear_by_card
        self.cards_by_card_appear = cards_by_card_appear

        initial_dic = {
            1: 7, 4: 2,
            2: 6 if self.cards_by_card_appear.get(4) else 5,
            3: 4 if self.cards_by_card_appear.get(3) else 3,
        }

        self.pure_ranking = initial_dic.get(self.cards_set_len, 1)

    def get_card_appearences(self, card: 'str'):
        return self.card_appear_by_card.get(card, 0)


def get_optimized_hand(hand: Hand):
    def get_optimized_hand_str(hand: Hand):
        joker_appear = hand.get_card_appearences(JOKER_CARD)
        if joker_appear == 0:
            raise Exception('NO JOKER to optimize')

        hand_str = hand.hand

        if hand.cards_set_len == 1:
            return hand_str

        if hand.cards_set_len == 2:
            return hand.random_card_no_joker * 5

        if hand.cards_set_len == 3:
            # 3 - 1 -1
            if joker_appear == 3:
                return hand_str.replace(JOKER_CARD, hand.random_card_no_joker)

            # 2 - 2 - 1
            # 2 - 1 - 2
            if joker_appear == 2:
                [card_to_replace, joker] = hand.cards_by_card_appear[2]
                if joker != JOKER_CARD:
                    [joker, card_to_replace] = [card_to_replace, joker]

                return hand_str.replace(JOKER_CARD, card_to_replace)

            # 1 - 3 - 1
            # 1 - 2 - 2
            # 1 - 1 - 3
            if joker_appear == 1:
                cards_appear_three = hand.cards_by_card_appear.get(3)
                if cards_appear_three:
                    card_appear_three = cards_appear_three[0]
                    return hand_str.replace(JOKER_CARD, card_appear_three)

                # 1 - 2 - 2
                card_appear_twice = hand.cards_by_card_appear[2][0]
                return hand_str.replace(JOKER_CARD, card_appear_twice)

        if hand.cards_set_len == 4:
            if joker_appear == 2:
                return hand_str.replace(JOKER_CARD, hand.random_card_no_joker)

            card_appear_twice = hand.cards_by_card_appear[2][0]
            return hand_str.replace(JOKER_CARD, card_appear_twice)

        return hand_str.replace(JOKER_CARD, hand.random_card_no_joker)

    return Hand(get_optimized_hand_str(hand))


def get_sorted_by(is_part_two=False):
    def sorted_by(line1: 'str', line2: 'str'):
        hand1_str, bid1 = get_hand_bid(line1)
        hand2_str, bid2 = get_hand_bid(line2)

        hand1 = Hand(hand1_str)
        hand2 = Hand(hand2_str)

        rank1 = hand1.pure_ranking
        if is_part_two and hand1.has_joker:
            rank1 = get_optimized_hand(hand1).pure_ranking

        rank2 = hand2.pure_ranking
        if is_part_two and hand2.has_joker:
            rank2 = get_optimized_hand(hand2).pure_ranking

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
    _, bid = get_hand_bid(line)

    return acc + (bid * rank)
