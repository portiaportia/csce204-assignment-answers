print("Welcome to our factorial generator")

num = int(input("Enter Number: "))
result = 1

for i in range(1, num + 1):
    result *= i

print(f"Factorial of {num} is {result}")