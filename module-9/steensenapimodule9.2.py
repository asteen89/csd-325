# Alisa Steensen
# Module 9.2

# Create a program that uses an API in a python program and ask the user if they would like to see the current astronauts
# in space, if yes, display astronauts with their ship, if no, exit the program

# reference/source help: https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/

import requests
import sys

def get_astronauts_in_space():
    """Fetch astronauts currently in space."""
    response = requests.get('http://api.open-notify.org/astros.json') 
    try:
        if response.status_code == 200:
            data = response.json()
            ship = []

            # Loop through the list of astronauts and collect their names
            for person in data['people']:
                ship.append(f" - {person['name']} ({person['craft']})")
            
            return "\n".join(ship)
        else:
            return f"Error: {response.status_code}"
        
    except Exception as e:
        return f"An error occurred"

def main():
    """Main program to ask if the user wants to see astronauts in space."""
    
    print("Welcome to the program that tells you who is in space currently!")

    input_question = input("Would you like to see who is in space currently? (y/n): ")

    # Exit if the answer is no
    if input_question.lower() == 'n':
        print("Thanks, have a great day!")
        sys.exit()
    elif input_question.lower() == 'y':
        # Call the function to fetch astronauts
        fetch_astronauts = get_astronauts_in_space()
        print("\nAstronauts currently in space:\n")
        print(fetch_astronauts)
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == '__main__':
    main()
