import numpy as N
import math

# This function will calculate the distance off all point by given point
def distance(x, y, pt):
    dist = N.zeros(shape=(len(y), len(x)), dtype=N.float64)  
      
    # run all point of x
    for eachY in y:
        
        # runn all point of y for each x
        for eachX in x:
            dist[eachY][eachX] = math.dist([eachX, eachY], pt)
    return dist

# Test
pointx = N.array([0, 1, 2, 3, 4])
pointy = N.array([0, 1, 2, 3])
print(distance(pointx, pointy, [-2.3, 3.3]))