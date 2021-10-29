""" Python: File, Mask, Plotting
    CSS 458
    By: Thong Ton
    10/11/2021
"""
import numpy as N
import matplotlib.pyplot as plt

# Defined value to use for index
DAY = 0
TEMPERATURE = 1

# Read the ASFG file and return temperature, julian day by list
def readFile(fileName):
    
    # Open the file
    f = open(fileName, 'r')
    
    # Skip the first three lines in file
    for i in range(3):
        f.readline()
    
    # Read lines start from the third line in file
    lines = f.readlines() # Read full current line
    
    # Initialize the needed lists
    temperatures = list()
    julianDays = list()
    temperAndJulian = list()
    
    # Achieve each line in bunched of line just read from file
    for line in lines:
        
        # Split the line
        onlyDatas = line.split('\t')
        
        if (len(onlyDatas) == 4):
            
            # Temperature
            temper = onlyDatas[3].rstrip()
            julianDays.append(onlyDatas[0])
            
            if (temper == ''):
                temperatures.append(N.nan)   
            else:
                temperatures.append(temper)   

    # Add temperature and julian day into returned list
    temperAndJulian.append(julianDays)
    temperAndJulian.append(temperatures)
    return temperAndJulian

# Display the data by x and y cordination
def displayGraph(temperatures, days):
        
    # Plot first arguments is x-cordinate, second argument is y-cordinate
    plt.plot(temperatures, days)
    plt.xlabel('Temperature')
    plt.ylabel('Julian Day')
    plt.show()
    
def main():
    
    # Read the file
    sourceData = readFile("ASFG_Ts.txt")
    
    # Convert list of temperatures into array of temperature
    # Using Mask to eliminate missing value
    temperatures = N.ma.masked_invalid(N.asarray(sourceData[TEMPERATURE], dtype='float64'))
    
    # Convert list of Julian Day into array of JulianDay
    days = N.asarray(sourceData[DAY], dtype='float64')

    # Calculate average temperature
    print('Average temperature: ' + str(N.ma.average(temperatures)))
    
    # Calculate standard deviation
    print('Standard deviation: ' + str(N.ma.std(temperatures)))
    
    # Calculate median
    print('Median: ' + str(N.ma.median(temperatures)))
    
    # Display the graph
    displayGraph(temperatures, days)

# Run
main()