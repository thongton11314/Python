# Final Project
#   Proposal: https://docs.google.com/document/d/1lbD_dyg6gwNgmIyiGswhel6B7Jl6CUOwBP6hWMX14QE/edit
#   Developer: Thong Ton
#   Guider: Professor Dung Mai, Edmonds Community College
#   Topic: Data Analysis
#   Requirement:
# 	    Import json library to read data into a list of records
# 	    Use list, dictionary, and programming elements to display 10 ten regions (timezone) that use the Internet
# 	    Draw a horizontal bar chart to display the top ten regions and scatter plot of the data.
#   Reference:     
#       https://matplotlib.org
#       https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barh.html
#       https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html

# Library
import json
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

# Function: Get JSON data from the file
# Imply library: json
# Input: fileName - file of data
# Ouput: a list of data
def readFile(fileName):
    myFile = None   
    lst = []
    try:
        myFile = open(fileName, 'r')
        while True:
            line = myFile.readline()
            if line.strip():
                lst.append(json.loads(line))
            if not line:
                break
        return lst
    except IOError:
        print("File is not found:" , fileName)
        return []
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file name:", fileName, "to close")

# Functinon: Remove some necessray data, heartbeat in particular 
# Input: lst - list of data
# Output: list of data without useful data
def removeHeartbeat(lst):
    for each in reversed(lst):
        if len(each.keys()) == 1:
            lst.remove(each)

# Function: Create a tuple that contain valid/invalid time-zone
# Input: list of data
# Output: tubple
def countTimeZone(lst):
    validTZ = 0 
    nonValidTZ = 0    
    for each in lst:
        if len(each["tz"]) > 0:
            validTZ = validTZ + 1
        else:
            nonValidTZ = nonValidTZ + 1
    return (validTZ, nonValidTZ)

# Function: Create a dictionary with time-zone as key, time appear as value
# Input: lst - list of time-zone
# Output: a dictionary 
def dicOfTimeZone(lst):
    myDict = {}
    for each in lst:
        if len(each["tz"]) > 0:
            if each["tz"] in myDict:
                myDict[each["tz"]] += 1
            else:
                myDict[each["tz"]] = 1
    return myDict

# Function: Get the most 10 common element from dictionary
# Imply library: Collection/Counter
# Input: dictionary
# Output: a list of 10 commom element
def topTenTimeZone(dic):
    #Count the most commom in dict
    counter = Counter(dic)
    tenCountry = counter.most_common(10)
    return tenCountry

# Function: Show horizontal bars graph top 10 country using internet
# Imply library: numpy as np
#                matplotlib.pyplot as plt
# Input: lst - list of contries
# Output: a graph with horizontal bars
def dataVisualization(lst):
    # Make data
    frequency = []
    timeZone = []
    for each in lst:
        timeZone.append(each[0])
        frequency.append(each[1])
    # Two graph in one figure
    fig, (horizontalBar,scatterPlot) = plt.subplots(2)
    fig.suptitle('Top 10 Regions Using Internet')
    fig.canvas.set_window_title('Regions Internet Usage') 
    # Horizontal bar
    y_pos = np.arange(len(timeZone))
    horizontalBar.barh(y_pos, frequency)
    horizontalBar.set_yticks(y_pos)
    horizontalBar.set_yticklabels(timeZone)
    horizontalBar.invert_yaxis() 
    horizontalBar.set_title('By Horizontal Bar')
    horizontalBar.set_xlabel('Frequency')
    horizontalBar.set_ylabel('Time-Zone')
    # Scatter plot
    scatterPlot.set_title("By Scatter Plot")
    scatterPlot.scatter(timeZone, frequency)
    scatterPlot.set_xlabel("Time-Zone")
    scatterPlot.set_ylabel("Frequecy")
    #Show graphic
    plt.show()

#Read file name
fileName = "National Internet Using.json"
#Gather data into list
lst = readFile(fileName)
#Remove some unuseful data
removeHeartbeat(lst)
#Get countries
timeZone = dicOfTimeZone(lst)
#Get top ten
topTen = topTenTimeZone(timeZone)
print("- Total size of data:", len(lst))
print("- Valid time-zone and invalid time-zone", countTimeZone(lst))
print("- Top ten time-zone using internet:", topTen)
#Graph with 10 commom time-zone using internet
dataVisualization(topTen)