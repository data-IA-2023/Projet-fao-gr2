import pandas as pd
import numpy as np

tt = pd.read_csv('country_translation_table.csv')
pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')
an = pd.read_csv('fao_2013/FAOSTAT_2013_animal.csv')

nour=pd.concat([an,vg],axis=0).sort_values(by=['Pays','Produit']).reset_index(drop=True)


"""
Création de la table des populations en français
"""
countrypop=pd.concat([pop['Country Code'],pop['Country'],pop['Value']*1000],axis=1)
L=[]
for i,Country in countrypop.iterrows():
    a=nour.iloc[nour.index[nour["Code Pays"]==Country["Country Code"]].tolist()[0]]['Pays']
    L.append(pd.Series(a, name='Pays'))
countrypop=pd.concat([pop['Country Code'],pop['Country'],pd.concat(L,axis=0).reset_index(drop=True),pop['Value']*1000],axis=1)

countrypop = countrypop.rename(columns={'Value': 'Population','Country Code': 'Code Pays'}).sort_values(by=['Country']).reset_index(drop=True)
del a,L

countrypop.to_csv('Résultats/country_population.csv')




nour1c = nour.drop(nour.index[nour['Code Élément'] != 674])['Code Pays']
nour1p = nour.drop(nour.index[nour['Code Élément'] != 674])['Pays']
nour1pr = nour.drop(nour.index[nour['Code Élément'] != 674])['Produit']
nour1v = nour.drop(nour.index[nour['Code Élément'] != 674])['Valeur']
nour1e = nour.drop(nour.index[nour['Code Élément'] != 674])['Code Élément']


nour2c = nour.drop(nour.index[nour['Code Élément'] != 664])['Code Pays']
nour2v = nour.drop(nour.index[nour['Code Élément'] != 664])['Valeur']
nour2p = nour.drop(nour.index[nour['Code Élément'] != 664])['Pays']
nour2pr = nour.drop(nour.index[nour['Code Élément'] != 664])['Produit']
nour2e = nour.drop(nour.index[nour['Code Élément'] != 664])['Code Élément']


nourm = nour.drop(nour.index[nour['Code Élément'] != 645])
#print(nourm)
"""
an1c = an.drop(an.index[an['Code Élément'] != 674])['Code Pays']
an1p = an.drop(an.index[an['Code Élément'] != 674])['Pays']
an1pr = an.drop(an.index[an['Code Élément'] != 674])['Produit']
an1v = an.drop(an.index[an['Code Élément'] != 674])['Valeur']

an2c = an.drop(an.index[an['Code Élément'] != 664])['Code Pays']
an2v = an.drop(an.index[an['Code Élément'] != 664])['Valeur']
an2p = an.drop(an.index[an['Code Élément'] != 664])['Pays']
an2pr = an.drop(an.index[an['Code Élément'] != 664])['Produit']
"""


dap=pd.concat([nour1c, nour1p, nour1pr, nour1v], axis=1).reset_index(drop=True).rename(columns={'Valeur': 'Disponibilité de protéines en quantité (g/personne/jour)'})
#dap2=pd.concat([an1c, an1p, an1pr, an1v], axis=1).reset_index(drop=True).rename(columns={'Valeur': 'Disponibilité de protéines en quantité (g/personne/jour)'})

da=pd.concat([nour2c, nour2p, nour2pr, nour2v], axis=1).reset_index(drop=True).rename(columns={'Valeur': 'Disponibilité alimentaire (Kcal/personne/jour)'})
#da2=pd.concat([an2c, an2p, an2pr, an2v], axis=1).reset_index(drop=True).rename(columns={'Valeur': 'Disponibilité alimentaire (Kcal/personne/jour)'})

"""
dap=pd.concat([dap1,dap2],axis=0).sort_values(by=['Pays','Produit']).reset_index(drop=True)
da=pd.concat([da1,da2],axis=0).sort_values(by=['Pays','Produit']).reset_index(drop=True)
"""

#print(da)

L=[]
for i,row in da.iterrows():
    #countrypop.iloc[countrypop.index[countrypop["Code Pays"]==row["Code Pays"]].tolist()[0]]['Population']
    a=row['Disponibilité alimentaire (Kcal/personne/jour)']*365
    try:
        c=nourm[nourm["Code Pays"]==row["Code Pays"]]
        
        #print(c[c["Produit"]==row["Produit"]]["Valeur"])
        b=(a/c[c["Produit"]==row["Produit"]]["Valeur"]).iloc[0]
        #print(b.iloc[0])
        if b == 0 : b = 'NaN'
    except:b='NaN'
    L.append(pd.DataFrame({'Ratio énergetique (Kcal/kg)':[b]}))
#print(pd.concat(L,axis=0).reset_index(drop=True))
da=pd.concat([da,pd.concat(L,axis=0).reset_index(drop=True)],axis=1)
#print("c\n",c)
del a,L,b,c

"""
L=[]
for i,row in nourm.iterrows():
    a=countrypop.iloc[countrypop.index[countrypop["Code Pays"]==row["Code Pays"]].tolist()[0]]['Population']*row['Disponibilité alimentaire (Kcal/personne/jour)']
    L.append(pd.Series(a, name='Disponibilité alimentaire (Kcal/jour)'))
da=pd.concat([da,pd.concat(L,axis=0).reset_index(drop=True)],axis=1)
del a,L
"""



L=[]
for i,row in dap.iterrows():
    a=countrypop.iloc[countrypop.index[countrypop["Code Pays"]==row["Code Pays"]].tolist()[0]]['Population']*row['Disponibilité de protéines en quantité (g/personne/jour)']
    L.append(pd.Series(a, name='Disponibilité de protéines en quantité (g/jour)'))
dap=pd.concat([dap,pd.concat(L,axis=0).reset_index(drop=True)],axis=1)
del a,L

"""
L=[]
for i,row in da.iterrows():
    a=countrypop.iloc[countrypop.index[countrypop["Code Pays"]==row["Code Pays"]].tolist()[0]]['Population']*row['Disponibilité de protéines en quantité (g/personne/jour)']
    L.append(pd.Series(a, name='Disponibilité de protéines en quantité (g/jour)'))
dap=pd.concat([dap,pd.concat(L,axis=0).reset_index(drop=True)],axis=1)
del a,L
"""



print(countrypop)
print(dap)
print(da)
