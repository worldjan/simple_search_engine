import random

secret_number = random.randint(1,10)
print(secret_number)
print(type(secret_number))
print("Pick a number between 1 to 10")
while True:
    res = input("Guess ther number: ")
    print(res)
    print(type(res))
    if res is secret_number:
        print("You win")
        break
    else:
        print("You lose")
        continue

