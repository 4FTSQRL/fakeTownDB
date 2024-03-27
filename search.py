"""
Author: Elicia Ramitt

Script: search.py

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

# Main function for testing
def main():
    print(searchName("Jerry Butler"))
    # Return statement
    return

# Get all people
def getPeople():
    """
    Description: Gets all people from the database
    
    Returns:
        list: all people
    """
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
def searchName(person):
    """
    Description: Searches for person
    
    Returns: list : descriptions about person
    """
    # Get all people
    people = getPeople()
    # personInfo list
    personInfo = []
    # Status of search
    stat = False
    
    # Search for person via their name
    for p in people:
        # Check name
        if p[1] == person:
            # Get name
            personInfo.append(p[1])
            # Get age
            personInfo.append(p[2])
            # Get address
            personInfo.append(p[3])
            # Get status
            personInfo.append(p[4])
            # Change search status to true
            stat = True
    
    # if status of search is still false, give user error
    if stat == False:
        print("Person does not exist")
        return False
    # Else: return the person info list
    return personInfo
# Python incantation
if __name__ == "__main__":
    main()