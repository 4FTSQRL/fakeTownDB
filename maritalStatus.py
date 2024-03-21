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
    # Call print Adults
    printAdults()
    
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
    
# Python Incantation
if __name__ == "__main__":
    main()