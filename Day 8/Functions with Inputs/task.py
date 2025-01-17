def greet():
    print("Hello")
    print("Hi")
    print("How are you?")

greet()

# Functions that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Hi {name}")
    print(f"How are you?")

greet_with_name(input(user_name))
