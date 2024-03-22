"""
Author: Elicia Ramitt

Script: maritalStatus.py

Description: Determines which citizens are married, single, divorced, or widowed

Usage: python maritalStatus.py
"""

# Import statments
    # os
import os
    # Get dbPath, createPeople, scriptDirectory from createDB.py
from createDB import scriptDirectory, dbPath, createPeople
    # sqlite3
import sqlite3
    # pandas
import pandas
    # Choice
from random import choice

# Main Function
def main():
    # Call userChoice function
    userChoice()
    
    # Return statement
    return None

# Get adults
def getAdults():
    """
    Objectives: Gets adults 20 or over
    
    Returns:
        list: (name, age, marital status) of adults
    """
    
    # Get all people
    people = createPeople()
    
    # Connect
    con = sqlite3.connect(dbPath)
    
    # Define cursor
    cur = con.cursor()
    
    #  Create query
    people = createPeople()
    
    # Get certain types of people (ie. people older than 20)
    cur.execute("SELECT * FROM people")
    
    # Fetch it
    people = cur.fetchall()
    
    
    # Adult list
    adults = []
    # Find out if they are an old enough adult
    for person in people:
        
        # Check age
        if person[2] >= 20:
            
            # Check status
            if person[4] == "Alive":
                
                # Get marital status
                maritalStatus = choice(("Married", "Single", "Divorced", "Widowed"))
                
                # Gets name, age, and marital status and adds to adults
                adults.append((person[1], person[2], maritalStatus))
    
    # Commit
    con.commit()
    
    # Close
    con.close()
    
    # Return the adults list
    return adults

# Print Adults Function
def printAdults():
    """
    Objective: Prints the adults and explains if they were divorced, married, single, or widowed, as well as their age
    """
    
    # Call getAdults
    adults = getAdults()
    
    # For loop
    for adult in adults:
        # print
        print(f"{adult[0]} is {adult[1]}. Their marital status is {adult[2].lower()}.")
        
    # Return statement
    return

# adults to csv function
def adultsToCSV():
    """
    Objective: Creates a pandas data frame and converts to a csv file
    """
    
    # Call getAdults
    adults = getAdults()
    
    # Create dataframe
    aDF = pandas.DataFrame(adults)
    
    # Add Column Names
    aDF.columns = ["Name", "Age", "Marital Status"]
    
    # Export to csv
    aDF.to_csv('maritalStatus.csv')
    

# user choice function
def userChoice():
    """
    Objectives: Ask user if they want to print adults' marital status or export to csv
    """
    
    # Valid for valid input
    valid = False
    
    # While loop
    while valid == False:
        # Prompt user
        choice = int(input("Select one of the following:\n"
                    "1. Print Marital Status of Adults over 20 in Fake Town\n"
                    "2. Export Marital Statuses to CSV file\n"
                    "3. Exit\n"))
        
        # Check if choice is 1
        if choice == 1:
            # Change Valid to True
            valid = True
            
            # Call printAdults function
            printAdults()
            
            
            
        # Check if choice is 2
        elif choice == 2:
            # Call adultsToCSV function
            adultsToCSV()
            
            # Change Valid to True
            valid = True
        
        # Check if choice is 3
        elif choice == 3:
            # Exit
            exit()
            
            # Change Valid to true
            valid = True
        
        # Else statement
        else:
            # Make sure Valid is False
            valid = False
        
# Python Incantation
if __name__ == "__main__":
    main()