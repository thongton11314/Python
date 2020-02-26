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
def readFile(fileName):
    myFile = None   
    dct = {}
    try:
        count = 0
        myFile = open(fileName, 'r')
        while True:
            line = myFile.readline()
            if line.strip():
                dct.update({count : json.loads(line)})
                count += 1
            if not line:
                break
        return dct
    except IOError:
        print("File is not found:" , fileName)
        return {}
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file name:", fileName, "to close")
        
fileName= "National Internet Using.json"
dct = readFile(fileName)
print(len(dct))
for i in range(2):
    print(dct[i])
