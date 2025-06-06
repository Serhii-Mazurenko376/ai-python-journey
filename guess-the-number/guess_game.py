import random

number = random.randint(1, 100)
attempts = 0

print("Gissa ett nummer mellan 1 och 100")

while True:
    guess = int(input("Ditt gissning: "))
    attempts += 1

    if guess < number:
        print("För lågt!")
    elif guess > number:
        print("För högt!")
    else:
        print(f"Rätt! Du gissade rätt på {attempts} försök.")
        break
