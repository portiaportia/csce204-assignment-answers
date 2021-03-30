import random

def play_game(play1, play2):
    if play1 == play2:
        return 0
    elif play1 == "r" and play2 == "p":
        return -1
    elif play1 == "r" and play2 == "s":
        return 1
    elif play1 == "p" and play2 == "r":
        return 1
    elif play1 == "p" and play2 == "s":
        return -1
    elif play1 == "s" and play2 == "p":
        return 1
    elif play1 == "s" and play2 == "r":
        return -1

def get_play():
    command = input("Enter (R)ock, (P)aper, or (S)cissors: ").strip().lower()
    if command == "r" or command == "p" or command == "s":
        return command
    else:
        return False

def get_comp_play():
    plays = ["r", "p", "s"]
    command = random.choice(plays)
    print(f"Computer choose: {command}")
    return command

print("Welcome to Rock Paper Scissors")
numRounds = 0
playersScore = 0
compScore = 0
tieScore = 0

while True:
    command = input("(P)lay or (Q)uit: ")

    if command == "q":
        break
    elif command != "p":
        print("Invalid command")
        continue

    numRounds += 1
    playerCommand = get_play()

    if playerCommand == False:
        print("Invalid command")
        break

    compCommand = get_comp_play()

    result = play_game(playerCommand, compCommand)

    if result == 1:
        print("You won!")
        playersScore += 1
    elif result == -1:
        print("Computer Won!")
        compScore += 1
    else:
        print("Tie!")
        tieScore += 1

print(f"You won {playersScore} rounds")
print(f"The computer won {compScore} rounds")
print(f"You tied {tieScore} rounds")