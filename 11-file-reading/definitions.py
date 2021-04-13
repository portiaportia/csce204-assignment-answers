def getDictionary():
    dictionary = {}
    with open("assignments/10-file-reading/words.txt") as file:
        for line in file:
            data = line.split(':')
            word = data[0].strip()
            definition = data[1].strip()
            dictionary[word] = definition
        return dictionary

def getDefinition(dictionary):
    word = input("Enter Word: ").strip().lower()
    if word in dictionary:
        print(f"{dictionary[word]}")
    else:
        print(f"Sorry {word} is not in our dictionary")

def displayDictionary(dictionary):
    for word in dictionary:
        print(f"{word}: {dictionary[word]}")

print("Welcome to our dictionary")
dictionary = getDictionary()

while True:
    command = input("Would you like to (V)iew, (D)efine, or (Q)uit: ").lower().strip()

    if command == "v":
        displayDictionary(dictionary)
    elif command == "d":
        getDefinition(dictionary)
    else:
        break

print("Good bye")