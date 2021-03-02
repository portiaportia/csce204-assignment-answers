import random

print("Welcome to our multiplication Game")

while True:
    play = input("Shall we ask you a question (Y)es or (N)o: ").lower().strip()
    if play != "y": break
    num1 = random.randint(1,11)
    num2 = random.randint(1,11)
    compAnswer = num1 * num2

    userAnswer = int(input(f"{num1} * {num2} = "))

    if compAnswer == userAnswer:
        print("You got it!")
    else:
        print(f"Sorry, the correct answer is {compAnswer}")

print("Goodbye")