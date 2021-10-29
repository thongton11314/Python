# PredatorPrey.py
# Program to run simulation of the predator-prey relationship

def PredatorPrey(DT = 0.001, simLength = 12):
    numIterations = int(simLength/DT) + 1
    t = 0

    predator_population = 15
    predator_birth_fraction = 0.01
    predator_death_proportionality_constant = 1.06
    prey_population = 100
    prey_birth_fraction = 2
    prey_death_proportionality_constant = 0.02

    predator_births = (predator_birth_fraction * prey_population) * predator_population
    predator_deaths = predator_death_proportionality_constant * predator_population

    prey_births = prey_birth_fraction * prey_population
    prey_deaths = (prey_death_proportionality_constant * predator_population) * prey_population

    tLst = [t]
    predatorLst = [predator_population]
    preyLst = [prey_population]
    for i in range(1, numIterations):
        t = i * DT
        prey_population = prey_population + (prey_births - prey_deaths) * DT
        predator_population = predator_population + (predator_births - predator_deaths) * DT

        prey_births = prey_birth_fraction * prey_population
        prey_deaths = (prey_death_proportionality_constant * predator_population) * prey_population

        predator_births = (predator_birth_fraction * prey_population) * predator_population
        predator_deaths = predator_death_proportionality_constant * predator_population

        tLst.append(t)
        predatorLst.append(predator_population)
        preyLst.append(prey_population)

    return tLst, predatorLst, preyLst
