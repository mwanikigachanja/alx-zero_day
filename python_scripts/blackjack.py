import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare_scores(player_score, dealer_score):
    if player_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 21:
        return "Dealer wins with Blackjack!"
    elif player_score == 21:
        return "You win with Blackjack!"
    elif player_score > 21:
        return "You went over. Dealer wins!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "Dealer wins!"

def blackjack_game():
    print("Welcome to Blackjack!")

    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    while player_score < 21:
        should_deal = input("Type 'y' to get another card, or 'n' to pass: ").lower()
        if should_deal == 'y':
            player_hand.append(deal_card())
            player_score = calculate_score(player_hand)
            print(f"Your cards: {player_hand}, current score: {player_score}")
        else:
            break

    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))

if __name__ == "__main__":
    blackjack_game()

