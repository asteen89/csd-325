# Alisa Steensen
# date
# Module 1.3


bottles = int(input("Enter number of bottles: "))

def countdown():
    for i in range(bottles, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i - 1} bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, 0 bottles of beer on the wall.\n")

    print("Time to buy some more bottles of beer.")

countdown()