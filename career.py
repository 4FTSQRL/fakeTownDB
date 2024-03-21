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

# Career Status function
def careerStatus():
    """
    Objectives: get the career status of everybody. This is partially based on age
    
    Return: list (name, age, career, career status)
    """
    
    # Call getCareers
    people = getCareer()
    
    # People and career stats
    peopleNCarStat = []
    
    # For loop to go through each person
    for person in people:
        
        # Define age
        age = person[1]
        
        # Check if they are too young to be in post-secondary
        if age < 18:
            # Set career status to in school
            careerStatus = "Enrolled primary/secondary school"
        
        # If age is between 18 and 22, they are in post-secondary
        elif 18 >= age >= 22:
            # Set career status to post-secondary
            careerStatus = "Enrolled in post-secondary school"
            
        # If age is between 22 and 35, they are working or in school
        elif 22 >= age >= 35:
            # get random option
            careerStatus = choice(("Working", "Enrolled in post-secondary school"))
            
        # Check if age is between 35 and 65
        elif 35 >= age >= 65:
            # Working
            careerStatus = "Working"
            
        # Check if age is greater than 65
        elif age > 65:
            # Either retired or workaholic
            careerStatus = choice(("Retired", "Workaholic"))

        # Append to the list with career status
        peopleNCarStat.append((person[0], person[1], person[2], careerStatus))
        
    # Return peopleNCarStat list
    return peopleNCarStat


# Python Incantation
if __name__ == "__main__":
    main()