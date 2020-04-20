import random

while True:
    x = input("Roll the dice? ")
    if len(x) < 1:
        print("Ok goodbye")
        break
    result1 = random.randint(1,6)
    result2 = random.randint(1,6)
    print("You rolled...", result1, "and", result2)
    print("===============================================")
