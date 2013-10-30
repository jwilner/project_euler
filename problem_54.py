from itertools import groupby, chain
from collections import defaultdict

class poker_hand:
    order = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
    def __init__(self,cards):
        self._cards,self._originals = sorted((self.order.index(c[0]),c[1]) for c in cards), cards
        self.hand_values = (
                ('high card',tuple()),
                ('one_pair',(self.get_pairs,)),
                ('two pairs',(self.is_two_pair,)),
                ('three of a kind',(self.get_three_of_a_kind,)),
                ('straight',(self.is_straight,)),
                ('flush',(self.is_flush,)),
                ('full house',(self.get_three_of_a_kind,self.get_pairs)),
                ('four of a kind',(self.get_four_of_a_kind,)),
                ('straight flush',(self.is_flush,self.is_straight)))
    def is_flush(self):
        try:
            return self._flush
        except AttributeError:
            suit = self._cards[0][1]
            self._flush = True
            for c in self._cards[1:]:
                if c[1] != suit:
                    self._flush = False
                    break
            return self._flush
    def is_straight(self):
        try:
            return self._straight
        except AttributeError:
            self._straight = True
            last_pos = self._cards[0][0]
            for c in self._cards[1:]:
                if c[0] != last_pos + 1:
                    self._straight = False
                    break
                last_pos = c[0]
            return self._straight
    def get_groups(self):
        try:
            return self._groups
        except AttributeError:
            self._groups = defaultdict(set)
            return_pos = lambda x:x[0]
            self._cards.sort(key=return_pos)
            for k,g in groupby(self._cards,key=return_pos):
                grouped = tuple(g)
                size_group = len(grouped)
                self._groups[size_group].add(grouped)
            return self._groups
    def get_pairs(self):
        return self.get_groups()[2]
    def is_two_pair(self):
        return True if len(self.get_groups()[2]) == 2 else False
    def get_three_of_a_kind(self):
        return self.get_groups()[3]
    def get_four_of_a_kind(self):
        return self.get_groups()[4]
    def get_high_card(self):
        #if the cards are grouped, it goes through them from big group to small;
        #if ungrouped, each individual card is treated as a group of one, so this will still serve up proper values for comparing five card hands
        try:
            return next(self._high_groups)
        except AttributeError:
            groups = sorted((i for i in chain(*self.get_groups().values())),key=lambda x:(len(x),x[0]),reverse=True)
            self._high_groups = (g[0][0] for g in groups)
            return next(self._high_groups)
    def get_hand_value(self):
        try:
            return self._value
        except AttributeError:
            best_hands = reversed(self.hand_values)
            for (hand,tests) in best_hands:
                for t in tests:
                    if not t(): break
                else:
                    self._value = (self.hand_values.index((hand,tests)),hand)
                    break
            return self._value
    def get_cards(self):
        return self._originals

def winning_hand(*hands):
    '''
    compare objects of class poker hand and return winning hand(s)
    problem 54
    '''
    def high_cards(hands):
        highest_value = 0
        winning_hands = set()
        for h in hands:
            high_val = h.get_high_card()
            if high_val > highest_value:
                highest_value,winning_hands = high_val,{h}
            elif high_val == highest_value:
                winning_hands.add(h)
        if len(winning_hands) == 1: return winning_hands
        try:
            return high_cards(winning_hands)
        except StopIteration as e:
            return winning_hands

    winning_val = (0,)
    winning_hands = set()
    for h in hands:
        this_val = h.get_hand_value()
        if  this_val[0] > winning_val[0]:
            winning_hands,winning_val = {h},this_val
        elif this_val[0] == winning_val[0]:
            winning_hands.add(h)
    if len(winning_hands) == 1: return winning_hands
    return high_cards(winning_hands)
