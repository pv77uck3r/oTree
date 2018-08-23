import pandas as pd
import numpy as np

db = pd.read_excel('GuiltyProbs_jr_08022018.xlsx', 'Sheet1')
trialcrime = 2
trialdefevid = 0
trialprosevid = 2
print(np.random.binomial(1, (db.loc[(db['Crime'] == trialcrime) & (db['Defense evidence'] == trialdefevid) & (db['Prosecutor evidence'] == trialprosevid),
                              'Probability of a guilty findng at trial'].item())))


prosdec = pd.read_excel('ProsecutorDecisions.xls', 'Sheet1')
maxprosecutor = prosdec['subjectid'].max()
randprosecutor = np.random.choice(range(1, maxprosecutor + 1))
prosdec = prosdec[prosdec.subjectid == randprosecutor]
incentive = np.random.choice([1, 2])
prosdec = prosdec[prosdec.Period == incentive]

proschoice = prosdec.loc[prosdec['onetonine'] == 8, 'choice'].item()
nopleacharge = prosdec.loc[prosdec['onetonine'] == 8, 'no_plea_charge'].item()
nopleaevidence = prosdec.loc[prosdec['onetonine'] == 8, 'pros_evid_NP'].item()
nopleapun = prosdec.loc[prosdec['onetonine'] == 8, 'crime_pun_NP'].item()
pleacharge = prosdec.loc[prosdec['onetonine'] == 8, 'plea'].item()
pleacrimelevel = prosdec.loc[prosdec['onetonine'] == 8, 'crime_P'].item()
pleapunishment = prosdec.loc[prosdec['onetonine'] == 8, 'pun_P'].item()
pleaevidence = prosdec.loc[prosdec['onetonine'] == 8, 'pros_evid_P'].item()
pleathreat = prosdec.loc[prosdec['onetonine'] == 8, 'threat_P'].item()
threatcharge = prosdec.loc[prosdec['onetonine'] == 8, 'threat'].item()

print(proschoice)
print(nopleacharge)
print(nopleaevidence)
print(nopleapun)
print(pleacharge)
print(pleacrimelevel)
print(pleaevidence)
print(pleapunishment)
print(pleathreat)
print(threatcharge)