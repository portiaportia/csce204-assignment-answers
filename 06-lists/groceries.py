groceries = ["apples", "bananas", "pears", "grapes", "kiwis"]

print("Welcome to our grocery store")

print("The following items are in the store:")
for item in groceries:
    print(f"- {item}")

item = input("What would you like to order? ").strip().lower()

if item in groceries:
    groceries.remove(item)
    print(f"We've ordered {item} for you")
else:
    print(f"Sorry we don't have any {item}")

print("Now the grocery store contains the following:")
for item in groceries:
    print(f"- {item}")

print("Goodbye")