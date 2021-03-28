import random
correct = random.randint(1,9)
gameOver = False

while gameOver == False:
    guess = int(input("Enter your guess"))
    if guess == correct:
        print("You Win")
        gameOver = True
    elif guess > correct:
        print("Your guess is too big")
    elif guess < correct:
        print("Your guess is too small")