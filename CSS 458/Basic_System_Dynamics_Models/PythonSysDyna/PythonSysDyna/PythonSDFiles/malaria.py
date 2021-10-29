# malaria.py
# Program to run simulation of the spread of malaria

def malaria(DT = 0.001, simLength = 200):
    numIterations = int(simLength/DT) + 1
    t = 0

    uninfected_humans = 300
    vectors = 0
    uninfected_mosquitoes = 300
    mosquitoes = uninfected_mosquitoes +vectors
    prob_vector = vectors / mosquitoes
    prob_bit = 0.3
    recovery_rate = 0.3
    human_hosts = 1
    recovered = human_hosts * recovery_rate
    flow_to_host = prob_bit * prob_vector * uninfected_humans
    immunity_rate = 0.01
    flow_to_immune = human_hosts * immunity_rate
    malaria_induced_death_rate = 0.005
    human_host_deaths =  malaria_induced_death_rate * human_hosts
    mosquito_birth_rate = 0.01
    mosquito_births = mosquito_birth_rate * mosquitoes
    immune = 0
    humans = human_hosts + immune + uninfected_humans
    prob_host = human_hosts / humans
    prob_bite_human = 0.3
    infected = prob_bite_human * prob_host * uninfected_mosquitoes
    mosquito_death_rate = 0.01
    uninfected_mosquito_deaths = mosquito_death_rate * uninfected_mosquitoes
    vector_deaths = mosquito_death_rate * vectors     

    tLst = [t]
    uninfected_humansLst = [uninfected_humans]
    vectorsLst = [vectors]
    uninfected_mosquitoesLst = [uninfected_mosquitoes]
    human_hostsLst = [human_hosts]
    immuneLst = [immune]
    
    for i in range(1, numIterations):
        t = i * DT
        uninfected_humans = uninfected_humans + (recovered - flow_to_host) * DT
        vectors = vectors + (infected - vector_deaths) * DT
        uninfected_mosquitoes = uninfected_mosquitoes + (mosquito_births - infected - uninfected_mosquito_deaths) * DT
        human_hosts = human_hosts + (flow_to_host - flow_to_immune - recovered - human_host_deaths) * DT
        immune = immune + (flow_to_immune) * DT
        mosquitoes = uninfected_mosquitoes +vectors
        prob_vector = vectors / mosquitoes
        recovered = human_hosts * recovery_rate
        flow_to_host = prob_bit * prob_vector * uninfected_humans
        flow_to_immune = human_hosts * immunity_rate
        human_host_deaths =  malaria_induced_death_rate * human_hosts
        mosquito_births = mosquito_birth_rate * mosquitoes
        humans = human_hosts + immune + uninfected_humans
        prob_host = human_hosts / humans
        infected = prob_bite_human * prob_host * uninfected_mosquitoes
        uninfected_mosquito_deaths = mosquito_death_rate * uninfected_mosquitoes
        vector_deaths = mosquito_death_rate * vectors
        
        tLst.append(t)
        uninfected_humansLst.append(uninfected_humans)
        vectorsLst.append(vectors)
        uninfected_mosquitoesLst.append(uninfected_mosquitoes)
        human_hostsLst.append(human_hosts)
        immuneLst.append(immune)

    return tLst, uninfected_humansLst, vectorsLst, uninfected_mosquitoesLst, human_hostsLst, immuneLst
