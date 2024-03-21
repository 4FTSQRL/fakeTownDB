"""
Author: Elicia Ramitt

Script: kids.py

Description: Gets a list of all kiddos

Usage: python kids.py
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


# Main function
def main():
    # Call kids csv
    kidToCSV()
    # Return Statement
    return

# Get Children Function
def getChildren():
    """
    Objectives: Gets a list of children, ages, and hobby types and hobbies
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
    
    
    # Kids list
    kids = []
    
    # Find out if they are young enough to be a kid
    for person in people:
        
        # Check age
        if person[2] <= 17:
            
            # Get hobby category
            hobbyCat = choice(("Music", "Sports", "Creative", "Nerd"))
            
            # Check to if hobby category is music
            if hobbyCat == "Music":
                # Get an instrument
                instrument = choice(("Piano", "Guitar", "Drums", "Bass", "Orchestral Instrument", "More than one instrument"))
                
                # Gets name, age, and hobby and adds to kids
                kids.append((person[1], person[2], instrument))
                
            # Check if hobby category is sports
            elif hobbyCat == "Sports":
                # Get a sport
                sport = choice(("Hockey", "Basketball", "Baseball", "Football", "Soccer", "Ringette"))
                
                # Gets name, age, and hobby and adds to kids
                kids.append((person[1], person[2], sport))
                
            # Check if hobby category is Creative
            elif hobbyCat == "Creative":
                # Get an art
                art = choice(("Sketching", "Painting", "Writing", "Sewing", "Pottery", "Dance"))
                
                # Gets name, age, and hobby and adds to kids
                kids.append((person[1], person[2], art))
                
            # Check if hobby cateogry is nerd
            elif hobbyCat == "Nerd":
                # Get a nerdy hobby
                nerd = choice(("Reading", "Programming :P", "Video Games", "Lego", "Movies", "Board Games"))
                
                # Gets name, age, and hobby and adds to kids
                kids.append((person[1], person[2], nerd))
                
    # Commit
    con.commit()
    
    # Close
    con.close()
    
    # Return the adults list
    return kids

def kidToCSV():
    """
    Objectives: exports to CSV
    """
    
    kids = getChildren()
    
    # Creates pandas data frame
    kidDF = pandas.DataFrame(kids)
    
    # Create columns
    kidDF.columns = ["Name", "Age", "Hobby"]
    
    # export to csv
    kidDF.to_csv('kids.csv')

# Python incantation
if __name__ == "__main__":
    main()