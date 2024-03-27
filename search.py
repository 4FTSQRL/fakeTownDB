"""
Author: Elicia Ramitt

Description: Allows for the user to search for a person

Usage: python search.py
"""

# Import Statements
    # os
import os
    # Get dbPath, createPeople, scriptDirectory from createDB.py
from createDB import scriptDirectory, dbPath, createPeople
    # sqlite3
import sqlite3

# Main function
def main():
    # Return statement
    return

# Get all people
def getPeople():
    # Get all people
    people = createPeople()
    # Connect
    con = sqlite3.connect(dbPath)
    # Define cursor
    cur = con.cursor()
    
    # Get certain types of people (ie. people older than 20)
    cur.execute("SELECT * FROM people")
    # Fetch it
    people = cur.fetchall()
    
    # Close and commit
    con.commit()
    con.close()
    
    # Return people
    return people

# Search for person
def searchName():
    # Get all people
    people = getPeople()
    
    
# Python incantation
if __name__ == "__main__":
    main()