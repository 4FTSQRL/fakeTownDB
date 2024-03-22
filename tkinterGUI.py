"""
Author: Elicia Ramitt

Script: tkinterGUI.py

Description: Adding a GUI
"""

# Import Statements
from tkinter import *
from maritalStatus import getAdults
from kids import getChildren

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
    kdBtn = Button(frame, text="Get Kid Stats", command=kdBtnClick)
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


# Function for Kids Button Click
def kdBtnClick():
    # Get the children stats
    kids = getChildren()
    
    # Create a new root
    root = Tk()
    
    # Create a new geometry
    root.geometry("600x100")
    
    # Create title
    root.title("Statistics for Kids")
    
    # Create counter for all kids
    i = 0
    
    # Create counter for kids under 6
    uS = 0
    
    # Create counter for kids 6 to 12
    uTw = 0
    
    # Create counter for teens
    teen = 0
    
    # Iterate through all of the kids
    for kid in kids:
        # Check the age for under 6
        if kid[1] > 6:
            # Add to under six counter
            uS += 1
        
        # Check for 6 to 12
        elif kid[1] > 13:
            # Add to the appropriate counter
            uTw += 1
        
        # Check for teens
        elif kid[1] <= 13:
            # Add to teen counter
            teen += 1
    
        # Increment all kid counter
        i += 1
    
    # Get the stats
    stats = f"There are {i} kids in Fake Town. {uS} of them are 5 and under. {uTw} of them are 6-12. {teen} are teenagers (13-17)."
    
    # Put it in a label
    statLabel = Label(root, text=stats)
    
    # Establish grid for the label
    statLabel.grid(row=2, column=1)
    # Run the root
    root.mainloop()
# Python Incantation
if __name__ == "__main__":
    main()