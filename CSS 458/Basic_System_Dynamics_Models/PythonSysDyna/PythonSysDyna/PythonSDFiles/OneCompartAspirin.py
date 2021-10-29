# OneCompartAspirin.py
# One Compartment model of drug dosage of aspirin

import math
import matplotlib.pyplot as plt

def OneCompartAspirin(DT = 0.01, simLength = 8):
	numIterations = int(simLength/DT) + 1
	print("         t   Plasma Concentration")
	half_life = 3.2
	plasma_volume = 3000
	aspirin_in_plasma = 2 * 325 * 1000
	elimination_constant = -math.log(0.5) / half_life
 
	elimination = elimination_constant * aspirin_in_plasma
	plasma_concentration = aspirin_in_plasma / plasma_volume
	plasma_concentrationLst = [plasma_concentration]
	t = 0
	timeLst = [0]
	print('%10.2f\t%12.2f' % (t, plasma_concentration))
	for i in range(1, numIterations):
		t = i * DT
		timeLst.append(t)
		elimination = elimination_constant * aspirin_in_plasma
		aspirin_in_plasma = aspirin_in_plasma - elimination * DT
		plasma_concentration = aspirin_in_plasma / plasma_volume
		plasma_concentrationLst.append(plasma_concentration)
		print('%10.2f\t%12.2f' % (t, plasma_concentration))
	plt.plot(timeLst, plasma_concentrationLst)
	plt.xlabel('Time')
	plt.ylabel('Plasma Concentration')
	plt.title('Drug Dose')
	plt.show()
OneCompartAspirin()

"""
a. How many times would the loop body be executed? 
	801
b. What would the value of i be for each of those iterations? 
	whole number
c. What would each value of the x vector be?  
	floating number
d. What value of time (in minutes) would each iteration represent? 
	floating number
e. What value of time (in hours) would each iteration represent?  
	floating number
"""