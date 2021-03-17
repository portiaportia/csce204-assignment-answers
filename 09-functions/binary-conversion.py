def decimalToBinary(num):
    result = ""
    while num > 0:
        remainder = num % 2
        num = num // 2
        result = str(remainder) + result

    print(int(result))

def binaryToDecimal(num):
    twoFactor = 1
    result = 0
    while num > 0:
        remainder = num % 10
        remainder *= twoFactor
        twoFactor *= 2
        num = num // 10
        
        result += remainder
    print(result)

print("Calculator")

while True:
    command = input("Convert from Binary to Decimal (BtD) or " + 
    "from Decimal to Binary (DtB), or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command == "dtb":
        num = int(input("Enter decimal number: "))
        decimalToBinary(num)
    elif command == "btd":
        num = int(input("Enter binary number: "))
        binaryToDecimal(num)
    else:
        print("Invalid command")

print("Goodbye")