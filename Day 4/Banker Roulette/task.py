import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


# Option 1
print(random.choice(friends))

# Option 2
random_integer = random.randint(0, 4)
print(friends[random_integer])

# Option 3
random_integer = random.randint(0, 4)

if random_integer == 0:
    print(friends[0])
elif random_integer == 1:
    print(friends[1])
elif random_integer == 2:
    print(friends[2])
elif random_integer == 3:
    print(friends[3])
elif random_integer == 4:
    print(friends[4])

