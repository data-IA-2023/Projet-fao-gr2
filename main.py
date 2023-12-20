import pandas as pd
import numpy as np

tt = pd.read_csv('country_translation_table.csv')
pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')
an = pd.read_csv('fao_2013/FAOSTAT_2013_animal.csv')


"""
Création de la table des populations en français
"""
countrypop=pd.concat([pop['Country'],pop['Value']*1000],axis=1)
L=[]
for i,Country in countrypop.iterrows():
    a=tt.iloc[tt.index[tt["English"]==Country["Country"]].tolist()]['French']
    L.append(a)
countrypop=pd.concat([pd.concat(L,axis=0).reset_index(drop=True),pop['Value']*1000],axis=1)

countrypop = countrypop.rename(columns={'French': 'Pays', 'Value': 'Population'})
del a,L



vg1p = vg.drop(vg.index[vg['Code Élément'] != 674])['Pays']
vg1pr = vg.drop(vg.index[vg['Code Élément'] != 674])['Produit']
vg1v = vg.drop(vg.index[vg['Code Élément'] != 674])['Valeur']

vg2v = vg.drop(vg.index[vg['Code Élément'] != 664])['Valeur']
vg2p = vg.drop(vg.index[vg['Code Élément'] != 664])['Pays']
vg2pr = vg.drop(vg.index[vg['Code Élément'] != 664])['Produit']



an1p = an.drop(an.index[an['Code Élément'] != 674])['Pays']
an1pr = an.drop(an.index[an['Code Élément'] != 674])['Produit']
an1v = an.drop(an.index[an['Code Élément'] != 674])['Valeur']

an2v = an.drop(an.index[an['Code Élément'] != 664])['Valeur']
an2p = an.drop(an.index[an['Code Élément'] != 664])['Pays']
an2pr = an.drop(an.index[an['Code Élément'] != 664])['Produit']



dap1=pd.concat([vg1p, vg1pr, vg1v], axis=1).reset_index(drop=True).rename(columns={'Valeur': 'Disponibilité de protéines en quantité (g/personne/jour)'})
dap2=pd.concat([an1p, an1pr, an1v], axis=1).reset_index(drop=True).rename(columns={'Valeur': 'Disponibilité de protéines en quantité (g/personne/jour)'})

da1=pd.concat([vg2p, vg2pr, vg2v], axis=1).reset_index(drop=True).rename(columns={'Valeur': 'Disponibilité alimentaire (Kcal/personne/jour)'})
da2=pd.concat([an2p, an2pr, an2v], axis=1).reset_index(drop=True).rename(columns={'Valeur': 'Disponibilité alimentaire (Kcal/personne/jour)'})

dap=pd.concat([dap1,dap2],axis=0).sort_values(by=['Pays','Produit']).reset_index(drop=True)
da=pd.concat([da1,da2],axis=0).sort_values(by=['Pays','Produit']).reset_index(drop=True)


print(countrypop)
print(dap)
print(da)