FILE_NAME = "assignments/11-file-writing/bands.txt"

def writeBands(bands):
    with open(FILE_NAME, "w") as file:
        for band in bands:
            file.write(band + "\n")
 
def readBands():
    bands = []
    with open(FILE_NAME) as file:
        for line in file:
            line = line.replace("\n","").strip()
            bands.append(line)
    return bands

def listBands(bands):
    for band in bands:
        print(f"- {band}")
        
# add a band to this list
def addBand(bands):
    band = input("Band: ").strip()
  
    for i in range(len(bands)):
        if(bands[i].lower().strip() == band.lower()):
            print(f"Sorry {band} was already on the list")
            return bands

    bands.append(band)
    print(f"{band} was added.")  
    return bands

# remove a band from the list
def deleteBand(bands):
    bandName = input("Enter band Name: ").strip().lower()

    for i in range(len(bands)):
        if(bands[i].lower().strip() == bandName):
            bands.pop(i)
            print(f"{bandName} was deleted")
            return bands

    print("Sorry your band was not found on the list")
    return bands

bands = readBands()

while True:
    command = input("Enter (L)ist, (A)dd, (D)elete, or (Q)uit: ").lower().strip()
    
    if command == "l":
        listBands(bands)
    elif command == "a":
        bands = addBand(bands)
    elif command == "d":
        bands = deleteBand(bands)
    elif command == "q":
        break
    else:
        print("Invalid command, try again.")

print("Goodbye")
writeBands(bands)
