# Author:  Your Name Here
# Date:    MM/DD/YYYY
# Program: ClockSimulator
# Descr:
# In-class exercise to create the Python implementation
# of a nested loop example

def main():
    
    # Local variables
    hours = int()
    minutes = int()
    seconds = int()

    # Display program description
    print('Clock Simulator Program')
    
    # Loop while changing hours/minutes/seconds
    for hours in range (0, 24):
        for minutes in range (0, 60):
            for seconds in range (0, 60):
                print(hours, ':', minutes, ':', seconds)

# Call main() module
main()
