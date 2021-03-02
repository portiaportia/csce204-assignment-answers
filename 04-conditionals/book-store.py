print("***** Welcome to our bookstore *****")
command = input("What would you like to do (V)iew or (O)rder: ").lower().strip()

if command == "v":
    print(f"""
    Our catalogue consists of:
    - 1984 by George Orwell
    - The Help by Kathryn Stockett
    - Gone with the Wind by Margaret Mitchell
    - The Fellowship of the Ring by J.R.R. Tolkien
    """)
elif command == "o":
    bookName = input("Enter book name: ").lower().strip()
    price = 0

    if bookName == "1984":
        price = 9.99
    elif bookName == "the help":
        price = 7.59
    elif bookName == "gone with the wind":
        price = 8.50
    elif bookName == "the fellowship of the ring":
        price =10.11
    else:
        print(f"Sorry {bookName} is not in stock")

    print(f"You can by {bookName} for ${price}")
else:
    print(f"Sorry {command} is a invalid command.")

print("Have a nice day")