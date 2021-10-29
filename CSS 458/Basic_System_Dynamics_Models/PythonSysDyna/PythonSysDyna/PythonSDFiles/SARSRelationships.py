# SARSRelationships.py
# Program to run simulation of the spread of SARS

def SARSRelationships(DT = 0.001, simLength = 12):
    numIterations = int(simLength/DT) + 1
    t = 0

    sus_to_expos =  { Place right hand side of equation here... }
    expos_to_undet =  { Place right hand side of equation here... }
    sus_to_expos_quar =  { Place right hand side of equation here... }
    expos_quar_to_inf_quar =  { Place right hand side of equation here... }
    undet_to_iso =  { Place right hand side of equation here... }
    inf_quar_to_iso =  { Place right hand side of equation here... }
    iso_to_immune =  { Place right hand side of equation here... }
    iso_to_death =  { Place right hand side of equation here... }
    quar_to_death =  { Place right hand side of equation here... }
    inf_quar_to_rec =  { Place right hand side of equation here... }
    undet_to_death =  { Place right hand side of equation here... }
    undet_to_im =  { Place right hand side of equation here... }
    sus_to_quar =  { Place right hand side of equation here... }
    quar_to_sus =  { Place right hand side of equation here... }
    exposed =  { Place initial value here... }
    exposed_quarantined =  { Place initial value here... }
    infectious_isolated =  { Place initial value here... }
    infectious_quarantined =  { Place initial value here... }
    infectious_undetected =  { Place initial value here... }
    recovered_immune =  { Place initial value here... }
    SARS_death =  { Place initial value here... }
    susceptible =  { Place initial value here... }
    susceptible_quarantined =  { Place initial value here... }

    tLst = [t]

    exposedLst = [exposed]
    exposed_quarantinedLst = [exposed_quarantined]
    infectious_isolatedLst = [infectious_isolated]
    infectious_quarantinedLst = [infectious_quarantined]
    infectious_undetectedLst = [infectious_undetected]
    recovered_immuneLst = [recovered_immune]
    SARS_deathLst = [SARS_death]
    susceptibleLst = [susceptible]
    susceptible_quarantinedLst = [susceptible_quarantined]
    for i in range(1, numIterations):
        t = i * DT
        exposed(t) = exposed(t - dt) + (sus_to_expos - expos_to_undet) * dt
        exposed_quarantined(t) = exposed_quarantined(t - dt) + (sus_to_expos_quar - expos_quar_to_inf_quar) * dt
        infectious_isolated(t) = infectious_isolated(t - dt) + (undet_to_iso + inf_quar_to_iso - iso_to_immune - iso_to_death) * dt
        infectious_quarantined(t) = infectious_quarantined(t - dt) + (expos_quar_to_inf_quar - quar_to_death - inf_quar_to_iso - inf_quar_to_rec) * dt
        infectious_undetected(t) = infectious_undetected(t - dt) + (expos_to_undet - undet_to_iso - undet_to_death - undet_to_im) * dt
        recovered_immune(t) = recovered_immune(t - dt) + (iso_to_immune + undet_to_im + inf_quar_to_rec) * dt
        SARS_death(t) = SARS_death(t - dt) + (quar_to_death + iso_to_death + undet_to_death) * dt
        susceptible(t) = susceptible(t - dt) + (quar_to_sus - sus_to_expos - sus_to_expos_quar - sus_to_quar) * dt
        susceptible_quarantined(t) = susceptible_quarantined(t - dt) + (sus_to_quar - quar_to_sus) * dt
        sus_to_expos =  { Place right hand side of equation here... }
        expos_to_undet =  { Place right hand side of equation here... }
        sus_to_expos_quar =  { Place right hand side of equation here... }
        expos_quar_to_inf_quar =  { Place right hand side of equation here... }
        undet_to_iso =  { Place right hand side of equation here... }
        inf_quar_to_iso =  { Place right hand side of equation here... }
        iso_to_immune =  { Place right hand side of equation here... }
        iso_to_death =  { Place right hand side of equation here... }
        quar_to_death =  { Place right hand side of equation here... }
        inf_quar_to_rec =  { Place right hand side of equation here... }
        undet_to_death =  { Place right hand side of equation here... }
        undet_to_im =  { Place right hand side of equation here... }
        sus_to_quar =  { Place right hand side of equation here... }
        quar_to_sus =  { Place right hand side of equation here... }      

        tLst.append(t)
        exposedLst.append(exposed)
        exposed_quarantinedLst.append(exposed_quarantined)
        infectious_isolatedLst.append(infectious_isolated)
        infectious_quarantinedLst.append(infectious_quarantined)
        infectious_undetectedLst.append(infectious_undetected)
        recovered_immuneLst.append(recovered_immune)
        SARS_deathLst.append(SARS_death)
        susceptibleLst.append(susceptible)
        susceptible_quarantinedLst.append(susceptible_quarantined)

    return tLst, exposedLst, exposed_quarantinedLst, infectious_isolatedLst, infectious_quarantinedLst, infectious_undetectedLst, recovered_immuneLst, SARS_deathLst, susceptibleLst, susceptible_quarantinedLst
