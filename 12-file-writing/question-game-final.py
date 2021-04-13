import random
FILE_NAME_TRIVIA = "assignments/12-file-writing/trivia.txt"
FILE_NAME_SCORES = "assignments/12-file-writing/score.txt"
 
# read in in each line from the file into a dictionary   
def getQuestions():
    questions = {}
    with open(FILE_NAME_TRIVIA) as file:
        for line in file:
            data = line.split(':')
            question = data[0].strip()
            answer = data[1].strip()
            questions[question] = convertToBool(answer)
        return questions

def getScores():
    scores = [0] * 3
    counter = 0
    with open(FILE_NAME_SCORES) as file:
        for line in file:
            scores[counter] = int(line.strip())
            counter+=1
        return scores

def convertToBool(answer):
    if answer == "true":
        return True
    else:
        return False

def saveScores(scores):
    with open(FILE_NAME_SCORES,"w") as file:
        for score in scores:
            file.write(f"{score}\n")

def displayScores(scores):
    print(f"Games Played: {scores[0]}")
    print(f"Games Won: {scores[1]}")
    print(f"Games Lost: {scores[2]}")

def playRound():
    # get a random dictionary entry
    question = random.choice(list(questions.keys()))
    userAns = input(f"True or False: {question} ").strip().lower()
    compAns = questions.get(question)

    if convertToBool(userAns) == compAns:
        return True
    else:
        return False


print("Welcome to our Trivia Game")
questions = getQuestions()
scores = getScores()
displayScores(scores)

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command != "p":
        print("Invalid command")
        continue
    
    if playRound():
        print("Yay, you got it!")
        scores[1] += 1
    else:
        print("Sorry, incorrect")
        scores[2] += 1
    scores[0] += 1

saveScores(scores)
displayScores(scores)
print("Goodbye")
