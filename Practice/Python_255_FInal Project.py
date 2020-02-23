# Option 1 - Data Analysis
# Objectives
# 	Understand how to read files using Python
# 	Use list, dictionary, and programming elements to analyze the data from the file
# 	Use Json package to read Json from a file
# 	Use Mathplotlib to draw a scatter plot
# Instruction
# 	Import json library to read data into a list of records
# 	Use list, dictionary, and programming elements to display 10 ten regions (timezone) that use the Internet
# 	Draw a horizontal bar chart to display the top ten regions and scatter plot of the data.
# Submission
# 	The py source code
# 	Snapshots of the scatter plot and the horizontal bar chart

import json

# This function will read data to json format
# Input:
#   fileName: the name of the file
# Output:
#   a dictionary filed by data from [filename]
def readingFromJSON(fileName):
    myFile = None
    #Open file
    try:
       with open(fileName) as myFile:
           data = json.load(myFile)
       return data
    #Any error relative to files
    except IOError:
        print("File is not found")
    #Close file
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file to close")

#File name
fileName = "National Internet Using.json"  
#Print data to file
print("Test reading from file")
data = readingFromJSON(fileName)