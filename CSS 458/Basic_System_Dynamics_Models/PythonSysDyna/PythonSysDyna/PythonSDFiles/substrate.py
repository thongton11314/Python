# substrate.py
# Submodel for [S] in enzyme kinetics program

def substrate(DT = 0.001, simLength = 12):
    numIterations = int(simLength/DT) + 1
    t = 0

    k2 = 
    ES_concentration = 0
    S_formation = k2*ES_concentration
    S_concentration = 100
    k1 = 
    E_concentration = 1
    S_removal = k1*E_concentration*S_concentration
   
    tLst = [t]
    ES_concentrationLst = [S_concentration]
    S_concentrationLst = [S_concentration]
    E_concentrationLst = [S_concentration]
    vectorsLst = [vectors]
    uninfected_mosquitoesLst = [uninfected_mosquitoes]
    human_hostsLst = [human_hosts]
    immuneLst = [immune]
    
    for i in range(1, numIterations):
        t = i * DT
        ES_concentration = ES_concentration
        S_concentration = S_concentration + (S_formation - S_removal) * DT
        E_concentration = E_concentration
        k2 = 
        S_formation = k2*ES_concentration
        k1 = 
        S_removal = k1*E_concentration*S_concentration    

        
        tLst.append(t)
        ES_concentrationLst.append(S_concentration)
        S_concentrationLst.append(S_concentration)
        E_concentrationLst.append(S_concentration)

    return tLst, ES_concentrationLst, S_concentrationLst, E_concentrationLst
