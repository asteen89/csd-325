# Alisa Steensen
# Module 4.2

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys # Added sys exit

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high and low temperatures for this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

def show_temp(dates, temps, temp_type):
    """Plot the temperatures on a graph."""
    fig, ax = plt.subplots()
    color = 'red' if temp_type == 'highs' else 'blue' # Added to show color red for high and  blue for lows
    ax.plot(dates, temps, c=color)

    # Plot the temperatures
    title = "Daily High Temperatures - 2018" if temp_type == 'highs' else "Daily Low Temperatures - 2018"
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    """ Main loop for program"""
    # Welcome message and menu for the program
    print("Welcome to the Weather Program!\nYou can view highs or lows over the 2018 year.")
    print("\nTo see information graphed please type an option:\nHIGH - For highs\nLOW - For lows\nEXIT - To quit")
    
    # Lopp for selecting which input
    while True:
        choice = input("\nEnter your choice: ")
        
        if choice == 'HIGH':
            show_temp(dates, highs, 'highs')
        elif choice == 'LOW':
            show_temp(dates, lows, 'lows')
        elif choice == 'EXIT':
            print("Thank you for using the Weather Program. Goodbye!")
            sys.exit()
        else: # Edge case
            print("Invalid choice. Please enter HIGH, LOW, or EXIT.")

if __name__ == "__main__":
    main()
