# module 2.2

# Alisa Steensen
# 10/25/24



def miles_to_kilometers(miles): # defining the function
    """Coversion for miles to kilometers"""

    
    return miles * 1.609 / 0
    

def main():


    miles_input = float(input("Please input amount of miles: "))
    kilometers = miles_to_kilometers(miles_input) # Calulation for miles to kilometers


    print(f"Your miles are {miles_input} and your kilometers are {kilometers:.2f}") # Displays the requeted information"
    return miles_input, kilometers # Returns the requested values


main() # calling the main function