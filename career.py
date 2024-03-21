"""
Author: Elicia Ramitt

Script: career.py

Description: Gets the careers of people and then shows if they are retired, currently working in field, or in school

Usage: python career.py
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
    # faker
from faker import Faker

# Main Function
def main():
    # Return Statement
    return

# Get Career Function
def getCareer():
    """
    Objectives: Gets the careers of ALL people
    
    Return: list (name, age, career)
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
    
    # All People List
    allPeople = []
    
    # Setting up faker
    fake = Faker()
    
    # For loop to get all of the careers for everybody
    for person in people:
        # Get a career
        career = fake.job()
        
        # Add everything to the list
        allPeople.append((people[1], people[2], career))
        
    # Commit
    con.commit()
    
    # Close Connection
    con.close()
    
    # Return statement
    return allPeople

# Python Incantation
if __name__ == "__main__":
    main()