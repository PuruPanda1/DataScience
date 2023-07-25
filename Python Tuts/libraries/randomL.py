import random

# Simulating tossing a coin event -- random.choice([list])
print(random.choice(["heads", "tails"]))

# Random number between two integers inclusive
print(random.randint(2, 10))

# Shuffle the values in the list
values = ["king", "Queen", "Jack"]
random.shuffle(values)
print(values)
