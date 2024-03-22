"""
Author: Elicia Ramitt

Script: status.py

Description: Get all people who are alive and deceased

Usage: python status.py    
"""

# Import Statements
    # os
import os
    # Get dbPath, createPeople, scriptDirectory from createDB.py
from createDB import scriptDirectory, dbPath, createPeople
    # sqlite3
import sqlite3
    # pandas
import pandas

# Create main function
def main():
    # Call user choice function
    userChoice()
    # Return statement
    return

# User Choice
def userChoice():
    # Set valid to False
    valid = False
    # While Valid is False
    while valid == False:
        # Prompt the user to choose an option
        choice = input("Choose an option from the list below:\n"
                    "1. Export a list of people who are alive to CSV\n"
                    "2. Export a list of people who are deceased to CSV\n"
                    "3. Exit\n"
                    "Enter your choice: ")
        
        # Check if choice is 1
        if choice == "1":
            # Valid is true
            valid = True
            # Run the aliveToCSV function
            aliveToCSV()
            
        # Check if choice is 2
        elif choice == "2":
            # Valid is true
            valid = True
            # Run deadToCSV function
            deadToCSV()
        
        # Check if choice is 3
        elif choice == "3":
            # Valid is true
            valid = True
            # Exit
            exit()
# Function to get citzens who are alive
def getAlive():
    """
    Description: Searches people for the citzens who are alive
    
    Returns: alive (name, age, status)
    """
    
    # Get the people table
    people = createPeople()
    
    # Connect to dbPath
    con = sqlite3.connect(dbPath)
    
    # Cursor
    cur = con.cursor()
    
    # Execute to get all the data from people
    cur.execute("SELECT * from people")
    
    # Fetch it
    people = cur.fetchall()
    
    # List for alive people
    alive = []
    
    # Search for people who are alive through a for loop
    for person in people:
        # Check status
        if person[4] == "Alive":
            # Append to the alive list
            alive.append((person[1], person[2], person[4]))
    
    # commit and close
    con.commit()
    con.close()
    
    # Return Statement
    return alive

# Export Alive to csv
def aliveToCSV():
    """
    Objectives: exports to CSV
    """
    # Get alive
    alive = getAlive()
    
    # Creates pandas data frame
    aliveDF = pandas.DataFrame(alive)
    
    # Create columns
    aliveDF.columns = ["Name", "Age", "Status"]
    
    # export to csv
    aliveDF.to_csv('alive.csv')

# Function to get citizens who are dead
def getDead():
    """
    Description: Searches people for the citzens who are deceased
    
    Returns: dead (name, age, status)
    """
    
    # Get the people table
    people = createPeople()
    
    # Connect to dbPath
    con = sqlite3.connect(dbPath)
    
    # Cursor
    cur = con.cursor()
    
    # Execute to get all the data from people
    cur.execute("SELECT * from people")
    
    # Fetch it
    people = cur.fetchall()
    
    # List for dead people
    dead = []
    
    # Search for people who are dead through a for loop
    for person in people:
        # Check status
        if person[4] == "Deceased":
            # Append to the dead list
            dead.append((person[1], person[2], person[4]))
    
    # commit and close
    con.commit()
    con.close()
    
    # Return Statement
    return dead

# Export Dead to csv
def deadToCSV():
    """
    Objectives: exports to CSV
    """
    # Get Dead
    dead = getDead()
    
    # Creates pandas data frame
    deadDF = pandas.DataFrame(dead)
    
    # Create columns
    deadDF.columns = ["Name", "Age", "Status"]
    
    # export to csv
    deadDF.to_csv('dead.csv')
    
# Python Incantation
if __name__ == "__main__":
    main()