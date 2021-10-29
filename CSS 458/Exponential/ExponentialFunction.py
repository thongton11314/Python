import math

def exponential(value, tol=1e-8):
    num = float(value)
    calTol = num
    totalSum = 0.0
    nCount = 0

    while calTol > tol:
        
        # Current calculation at nCount
        curSum = totalSum + ((num ** nCount) / math.factorial(nCount))
        
        # Check convergence
        calTol = (curSum - totalSum) / num * 100.
        
        # Add up to overall sum
        totalSum = curSum
        
        # Increase by nCount after each series process
        nCount += 1

    return totalSum

# Testing
print(exponential(3.4, tol=1e-8))
