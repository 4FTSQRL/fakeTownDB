"""
Author: Elicia Ramitt

Script: tkinterGUI.py

Description: Adding a GUI
"""

# Import Statements
from tkinter import *
from maritalStatus import printAdults, getAdults

# Main function
def main():
    # Call create GUI function
    createGUI()
    
    

# create GUI function
def createGUI():
    # Create object for tk
    root = Tk()

    # Create geometry
    root.geometry("500x500+100+100")

    # create Title
    root.title("Fake Town Statistics")
    
    # Frame Creating
    frame = Frame(root)
    # Establish grid for frame
    frame.grid(row=0, column=0, columnspan=7, rowspan=3)
    
    # Create a Label
    titleLabel = Label(frame, text="Get Fake Town Statistics")
    # Establish Grid
    titleLabel.grid(row=0, column=4)
    
    # Add buttons for maritial status and kid stats
    msBtn = Button(frame, text="Get Marrital Status", command=msBtnClick)
    # Est. Grid
    msBtn.grid(row=1, column=2)
    kdBtn = Button(frame, text="Get Kid Stats")
    # Est. Grid
    kdBtn.grid(row=1,column=7)

    # Run
    root.mainloop()
    
# Function for Maritial Status button click
def msBtnClick():
    # Call print function from the maritialStatus.py file
    adults = getAdults()
    
    # Create a new root and geometry
    root = Tk()
    root.geometry("600x50+200+200")
    
    # Create Title
    root.title("Marital Status of Adults over 21")
    
    # Counter for single
    s = 0
    
    # Counter for divorced
    d = 0
    
    # Counter for widowed
    w = 0
    
    # All adult counter
    i = 0
    # Iterate with foor loop
    for adult in adults:
        
        # Check if adult is single
        if adult[2].lower() == "single":
            # Add to single counter
            s += 1
            
        # Check if adult is divorced
        elif adult[2].lower() == "divorced":
            # Add to divorce counter
            d += 1
        
        # Else add to widowed counter
        else:
            w += 1
        
        # increment all adult counter
        i += 1
    
    # Get the stat
    stats = f"There are {i} adults in Fake Town. {s} of them are single. {d} of them are divorced. {w} of them are widows."
    
    # Print the statistic about how many adults there are and how many are single, divorced, or widowed
    statLabel = Label(root, text=stats)
    
    # Establish grid for label
    statLabel.grid(row=3, column=2)
    # Run the root
    root.mainloop()

# Python Incantation
if __name__ == "__main__":
    main()