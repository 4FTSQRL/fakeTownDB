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
    # Run the root
    root.mainloop()
    
    # FRAMES
    # Top Frame
    topFrame = ttk.Frame(root)
    # set grid
    topFrame.grid(row=0, column=0, columnspan=2)
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
# Python Incantation
if __name__ == "__main__":
    main()