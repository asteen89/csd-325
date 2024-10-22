# module 2.2

def miles_to_kilometers(miles): # defining the function
    """Coversion for miles to kilometers"""

    return miles * 1.609

def main():
    miles_input = float(input("Please input amount of miles: "))
    kilometers = miles_to_kilometers(miles_input) # Calulation for miles to kilometers

    return f"Your miles are {miles_input} and your kilometers are {kilometers:.2f}" # Displays the requeted information


main() # calling the main function
