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
    # Call user option functin
    userChoice()
    
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

# Print Career function
def printCareer():
    """
    Objectives: Prints career and name and whatnot
    """
    
    # Call careerStat
    people = careerStatus()
    
    # For loop to print each person
    for person in people:
        
        # Print
        print(f"{person[0]} is {person[1]}. Their career is {person[2]}, and career status is {person[3]}")

    # Return statement
    return

# career to csv function
def careerToCSV():
    """
    Objectives: exports people and career information to csv file
    """
    
    # Call careerStatus
    people = careerStatus()
    
    # Create pandas data frame
    peopleDF = pandas.DataFrame(people)
    
    # Create columns
    peopleDF.columns = ["Name", "Age", "Career", "Career Status"]
    
    # Export to csv
    peopleDF.to_csv('career.csv')
    
    # Return
    return

# user choice function
def userChoice():
    """
    Objectives: Ask user if they want to print the career information or export to csv
    """
    
    # Valid for valid input
    valid = False
    
    # While loop
    while valid == False:
        # Prompt user
        choice = int(input("Select one of the following:\n"
                    "1. Print Career Information\n"
                    "2. Export Career Information to CSV file\n"
                    "3. Exit\n"))
        
        # Check if choice is 1
        if choice == 1:
            # Change Valid to True
            valid = True
            
            # use print career function
            printCareer()
            
            
            
        # Check if choice is 2
        elif choice == 2:
            # Call careertoCSV function
            careerToCSV()
            
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