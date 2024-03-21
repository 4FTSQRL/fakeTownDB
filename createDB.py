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
    # Datetime
from datetime import datetime
    # Faker
from faker import Faker

# Get the path of the database
    # Directory
scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    # database path
dbPath = os.path.join(scriptDirectory, 'fakeTown.db')

# Main function
def main():
    # Return None
    return None


# Create people function
def createPeople():
    # Return statement
    return

# Populate people function
def popPeople():
    # Return Statement
    return
# Python Incantation
if __name__ == "__main__":
    main()