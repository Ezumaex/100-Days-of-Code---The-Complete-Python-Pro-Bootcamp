from data import resources, MENU

def check_resources_sufficient(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def insert_coins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost

        return True

    elif money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_a_coffee(drink_name, drink_ingredients):
    for items in drink_ingredients:
        resources[items] -= drink_ingredients[items]
    print(f"Here is your {drink_name}☕. Enjoy!")

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# Check the user's input to decide what to do next.

coffee_working = True
profit = 0

while coffee_working:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # Resources

    if user_choice == "off":
        coffee_working = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if check_resources_sufficient(drink["ingredients"]):
            payment = insert_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_a_coffee(user_choice, drink["ingredients"])

