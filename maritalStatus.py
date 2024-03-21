"""
Author: Elicia Ramitt

Script: maritalStatus.py

Description: Determines which citizens are married

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


# Main Function
def main():
    # Call getadults
    getAdults()
    
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
    cur.execute("SELECT * FROM people WHERE column2 >= 20")
    
    # Fetch it
    people = cur.fetchall()
    
    print(people)
    # Commit
    con.commit()
    
    # Close
    con.close()

# Python Incantation
if __name__ == "__main__":
    main()