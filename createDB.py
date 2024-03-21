"""
Author: Elicia Ramitt

Script Name: createDB.py

Description: 
    Creates a table in the Fake Town database and populates it with 500 fake people using Faker
    
Usage:
    python createDB.py
"""

# Import Statements
    # os
import os
    # sqlite3
import sqlite3
    # Faker
from faker import Faker

# Get the path of the database
    # Directory
scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    # database path
dbPath = os.path.join(scriptDirectory, 'fakeTown.db')

# Main function
def main():
    # Call createPeople Function
    createPeople()
    
    # Call popPeople Function
    popPeople()
    
    # Return None
    return None


# Create people function
def createPeople():
    """
    Objective: Creates a people table in the database
    """
    
    # Open a connection to the database
    con = sqlite3.connect(dbPath)
    
    # Define cursor
    cur = con.cursor
    
    # Create query table
    pplQuery = """
        CREATE TABLE IF NOT EXISTS people
        (
            id  INTEGER PRIMARY KEY,
            name    TEXT NOT NULL,
            age     INTEGER,
            address TEXT NOT NULL
        );
    """
    
    # Execute
    cur.execute(pplQuery)
    
    # Commit
    con.commit()
    
    # Close connection
    con.close()
    
    # Return statement
        # Return the query
    return pplQuery

# Populate people function
def popPeople():
    """
    Objective: Populates the people table with 500 fake people
    """
    
    # Open connection
    con = sqlite3.connect(dbPath)
    
    # Cursor
    cur = con.cursor()
    
    # Create query to add a person
    addPerson = """
        INSERT INTO people
        (
            name,
            age,
            address
        )
        VALUES(?, ?, ?)
    """
    
    # Make new people with faker
    fake = Faker("en_CA")
    
    # 500 people
    for fakePerson in range(500):
        fP = (
            # Get name
            fake.name(),
            
            # Get Age
            fake.random_int(min=0, max=110),
            
            # Address
            fake.street_address()
        )
        
        # Execute
        cur.execute(addPerson, fP)
        
    # Commit
    con.commit()
    
    # Close
    con.close()
    
    # Return Statement
    return
# Python Incantation
if __name__ == "__main__":
    main()