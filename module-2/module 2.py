# module 2.2

def miles_to_kilometers(): # defining the function
    """Coversion for miles to kilometers"""
            miles = float(input("Please input amount of miles: "))
            kilometers = miles * 1.609 # Calulation for miles to kilometers

            if miles <= 0: # another error test
                print("Please enter a positive number.")
                continue
            print(f"Your miles are {miles} and your kilometers are {kilometers:.2f}") # Displays the requeted information
            return miles, kilometers # Returns the requested values


miles_to_kilometers() # calling the function

input('Press ENTER to exit') #does not close program until enter to exit is executed
