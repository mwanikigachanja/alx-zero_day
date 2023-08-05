import random
class BlackjackGame:
    def __init__(self):
        self.deck = self.generate_deck() # Create and shuffle deck
        self.player_hand = []
        self.dealer_hand = []
        self.player_hands = [self.player_hand]  # To support splitting
        self.active_hand_index = 0
        self.insurance_taken = False
        self.player_bust = False
        self.dealer_bust = False

    def generate_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

    def double_down(self):
        if len(self.player_hands[self.active_hand_index]) == 2 and self.player_chips >= self.bet_amount:
            self.player_chips -= self.bet_amount
            self.bet_amount *= 2
            self.player_hit()
            self.player_stand()

    def split(self):
        if len(self.player_hands) == 1 and len(self.player_hands[self.active_hand_index]) == 2 and \
                self.player_chips >= self.bet_amount:
            new_hand = [self.player_hands[self.active_hand_index].pop()]
            self.player_hands.insert(self.active_hand_index + 1, new_hand)
            self.player_chips -= self.bet_amount
            self.bet_amount *= 2
            self.player_hit()

    def take_insurance(self):
        if len(self.dealer_hand) == 1 and not self.insurance_taken:
            self.insurance_taken = True
            self.player_chips -= self.bet_amount / 2


    def deal_initial_cards(self):
        # Logic to deal initial cards to players
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]

    def draw_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
    def player_hit(self):
        # Logic for player hitting
        if sum(self.get_hand_values(self.player_hand)) < 21:
            self.player_hand.append(self.draw_card())
        else:
            self.player_bust = True

    def get_hand_values(self, hand):
        values = [self.card_value(card) for card in hand]
        return values

    def card_value(self, card):
        rank = card['rank']
        if rank in ['J', 'Q', 'K']:
            return 10
        elif rank == 'A':
            return 11 if sum(self.get_hand_values([card])) + 11 <= 21 else 1
        else:
            return int(rank)

    def player_stand(self):
        # Logic for player standing
        if self.active_hand_index < len(self.player_hands) - 1:
            self.active_hand_index += 1
            return

    def dealer_turn(self):
        # Logic for dealer's turn

    def determine_winner(self):
        # Logic to determine the winner

