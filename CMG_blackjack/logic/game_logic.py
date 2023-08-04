class BlackjackGame:
    def __init__(self):
        self.deck = []  # Create and shuffle deck
        self.player_hand = []
        self.dealer_hand = []
        self.player_hands = [self.player_hand]  # To support splitting
        self.active_hand_index = 0
        self.insurance_taken = False


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

    def player_hit(self):
        # Logic for player hitting

    def player_stand(self):
        # Logic for player standing
        if self.active_hand_index < len(self.player_hands) - 1:
            self.active_hand_index += 1
            return

    def dealer_turn(self):
        # Logic for dealer's turn

    def determine_winner(self):
        # Logic to determine the winner

