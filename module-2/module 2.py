# module 2.2

def miles_to_kilometers(miles): # defining the function
    """Coversion for miles to kilometers"""

    return miles * 1.609

def main():
    miles_input = float(input("Please input amount of miles: "))
    kilometers = miles_to_kilometers(miles_input) # Calulation for miles to kilometers

    f miles_input <= 0: # another error test
        print("Please enter a positive number.")
        continue
    print(f"Your miles are {miles_input} and your kilometers are {kilometers:.2f}") # Displays the requeted information
    eturn miles_input, kilometers # Returns the requested values

    print("New Test")

main() # calling the main function

input('Press ENTER to exit')

#change
