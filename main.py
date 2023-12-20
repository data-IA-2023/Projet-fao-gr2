import pandas as pd
import numpy as np

tt = pd.read_csv('country_translation_table.csv')
pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')
countrypop=pd.concat([pop['Country'],pop['Value']*1000],axis=1)


L=[]
for i,Country in countrypop.iterrows():
    a=tt.iloc[tt.index[tt["English"]==Country["Country"]].tolist()]['French']
    L.append(a)
countrypop=pd.concat([pd.concat(L,axis=0).reset_index(drop=True),pop['Value']*1000],axis=1)

countrypop = countrypop.rename(columns={'French': 'Pays', 'Value': 'Population'})




vg1p = vg.drop(vg.index[vg['Élément'] != "Disponibilité de protéines en quantité (g/personne/jour)"])['Pays']
vg1pr = vg.drop(vg.index[vg['Élément'] != "Disponibilité de protéines en quantité (g/personne/jour)"])['Produit']
vg1e = vg.drop(vg.index[vg['Élément'] != "Disponibilité de protéines en quantité (g/personne/jour)"])['Élément']
vg1v = vg.drop(vg.index[vg['Élément'] != "Disponibilité de protéines en quantité (g/personne/jour)"])['Valeur']
vg2v = vg.drop(vg.index[vg['Élément'] != "Disponibilité alimentaire (Kcal/personne/jour)"])['Valeur']
vg2e = vg.drop(vg.index[vg['Élément'] != "Disponibilité alimentaire (Kcal/personne/jour)"])['Élément']
vg2p = vg.drop(vg.index[vg['Élément'] != "Disponibilité alimentaire (Kcal/personne/jour)"])['Pays']
vg2pr = vg.drop(vg.index[vg['Élément'] != "Disponibilité alimentaire (Kcal/personne/jour)"])['Produit']


dap=pd.concat([vg1p, vg1pr, vg1e, vg1v], axis=1).reset_index(drop=True)
da=pd.concat([vg2p, vg2pr, vg2e, vg2v], axis=1).reset_index(drop=True)




print(dap)
print(countrypop)#print(df.drop(df.index[32:36])['Country'].to_string())
