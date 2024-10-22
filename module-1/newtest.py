<<<<<<< HEAD:module-1/steensen-module1_3.py
# Alisa Steensen
# 10/22/24
# Module 1.3

# Input number of bottles
bottles = int(input("Enter number of bottles: ")) 

def countdown():
    """Function to countdown bottles on each loop"""
    for i in range(bottles, 1, -1): # Start at bottles input, stop at 1 and skip by -1
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i - 1} bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, 0 bottles of beer on the wall.\n")

    print("Time to buy some more bottles of beer.")

=======
# Alisa Steensen
# date
# Module 1.3


bottles = int(input("Enter number of bottles: "))

def countdown():
    for i in range(bottles, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i - 1} bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, 0 bottles of beer on the wall.\n")

    print("Time to buy some more bottles of beer.")

>>>>>>> 77a3953ee7cf4facac8bd225f97ab835db4c7595:module-1/newtest.py
countdown()