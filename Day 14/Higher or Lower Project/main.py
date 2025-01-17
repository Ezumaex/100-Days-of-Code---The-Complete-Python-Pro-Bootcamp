from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Format data into something readable"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(answer, follower_a, follower_b):
    if follower_a > follower_b:
        return answer == 'a'
    else:
        return answer == 'b'

print(logo)

user_score = 0
game_should_continue = True

data_b = random.choice(data)

while game_should_continue:
    data_a = data_b
    data_b = random.choice(data)

    while data_a == data_b:
        data_b = random.choice(data)

    print(f"Compare A: {format_data(data_a)}")
    print(vs)
    print(f"Against B: {format_data(data_b)}")

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 25)
    print(logo)

    data_a_follower = data_a["follower_count"]
    data_b_follower = data_b["follower_count"]
    is_correct = check_answer(user_answer, data_a_follower, data_b_follower)

    if is_correct:
        user_score += 1
        print(f"You're right! Current score: {user_score}.")
    else:
        print(f"Sorry, that's wrong. Final score {user_score}.")
        game_should_continue = False



