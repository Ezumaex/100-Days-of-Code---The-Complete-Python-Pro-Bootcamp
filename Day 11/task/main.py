import random, art


def deal_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(p_score, computer_score):
    if p_score > 21 and computer_score > 21:
        return "You lose"
    elif p_score == computer_score:
        return "Draw"
    elif p_score == 0:
        return "Blackjack!"
    elif computer_score == 0:
        return "Blackjack"
    elif p_score > 21:
        return "You lose."
    elif computer_score > 21:
        return "You win."
    elif p_score > computer_score:
        return "You win."
    else:
        return "You lose!"


def play_game():
    print(art.logo)

    player_card = [deal_a_card(), deal_a_card()]
    computer_card = [deal_a_card(), deal_a_card()]

    game_over = False
    while not game_over:
        player_score = calculate_score(player_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards: {player_card}, current score: {calculate_score(player_card)}")
        print(f"Computer's first card: {computer_card[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == 'y':
                player_card.append(deal_a_card())
            else:
                game_over = True

    while computer_score < 17:
        computer_card.append(deal_a_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {player_card}, final score: {player_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()
