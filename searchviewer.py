"""
Author: Elicia Ramitt

Script: searchviewer.py

Description: Use tkinter to give the user a view to search for people

Usage: python searchviewer.py    
"""

# Import Statements
    # tkinter imports
from tkinter import ttk
from tkinter import *
    # searchName from search.py
from search import searchName

# Main function
def main():
    # Call createview
    createViewer()
    # Return statement
    return

# Create GUI
def createViewer():
    # Create root
    root = Tk()
    root.title("Searching People Database...")
    # Adjusting Geometry
    root.geometry("500x300+200+200")    
    
    # FRAMES
    # Top Frame
    topFrame = ttk.Frame(root)
    # set grid
    topFrame.grid(row=0, column=0, columnspan=3)
    # Add a border
    topFrame['borderwidth'] = 0.5
    topFrame['relief'] = 'sunken'
    
    # Info Frame
    infoFrame = ttk.Frame(root)
    # Set grid
    infoFrame.grid(row=1, column=0, columnspan=4)
    # Add border
    infoFrame['borderwidth'] = 0.5
    topFrame['relief'] = 'sunken'
    
    # Add a Label to Top Frame to tell user waht to do
    instructLabel = ttk.Label(topFrame, text="Enter a name:")
    # Establish Grid
    instructLabel.grid(row=0, column=0, padx=(90,3), pady=(20))
    # Add an Entry to grab the name from the user
    nameEntry = ttk.Entry(topFrame)
    # Establish grid for name
    nameEntry.grid(row=0, column=1)
    # Add a button to click after entering the name
    getPersonBtn = ttk.Button(topFrame, text="   Search   ", command=getPersonBtnClick(nameEntry))
    # Establish grid for button
    getPersonBtn.grid(row=0,column=3,padx=(50, 75))
    # Run the root
    root.mainloop()

def getPersonBtnClick(name):
    """
    Description: The actions for the button click for the Get person button
    """
    # Search for the person
    personInfo = searchName(name)
    
# Python Incantation
if __name__ == "__main__":
    main()