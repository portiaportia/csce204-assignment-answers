# Prices
flooring = 1.50
insulation = 0.5
dryWall = 2

print("Let's finish your room")

# Dimensions
width = float(input("Room Width: "))
length = float(input("Room Length: "))
height = float(input("Room Height: "))

floorCost = flooring * length * width
insulationCost = insulation * length * width
dryWallCeilingCost = dryWall * length * width
dryWallWallsCost = dryWall * (2 * length * height + 2 * width * height) 
totalDryWallCost = dryWallCeilingCost + dryWallWallsCost
totalCost = floorCost + insulationCost + totalDryWallCost

print(f"Room finishing cost: ${totalCost}")
