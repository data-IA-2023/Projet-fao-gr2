import pandas as pd
import numpy as np

pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')

vg1p = vg.drop(vg.index[vg['Élément'] != "Disponibilité de protéines en quantité (g/personne/jour)"].tolist())['Pays']
vg1pr = vg.drop(vg.index[vg['Élément'] != "Disponibilité de protéines en quantité (g/personne/jour)"].tolist())['Produit']
vg1e = vg.drop(vg.index[vg['Élément'] != "Disponibilité de protéines en quantité (g/personne/jour)"].tolist())['Élément']
vg1v = vg.drop(vg.index[vg['Élément'] != "Disponibilité de protéines en quantité (g/personne/jour)"].tolist())['Valeur']
vg2v = vg.drop(vg.index[vg['Élément'] != "Disponibilité alimentaire (Kcal/personne/jour)"].tolist())['Valeur']
vg2e = vg.drop(vg.index[vg['Élément'] != "Disponibilité alimentaire (Kcal/personne/jour)"].tolist())['Élément']
vg2p = vg.drop(vg.index[vg['Élément'] != "Disponibilité alimentaire (Kcal/personne/jour)"].tolist())['Pays']
vg2pr = vg.drop(vg.index[vg['Élément'] != "Disponibilité alimentaire (Kcal/personne/jour)"].tolist())['Produit']

country=pd.concat([pop['Country'],pop['Value']*1000],axis=1)

dap=pd.concat([vg1p, vg1pr, vg1e, vg1v], axis=1)
da=pd.concat([vg2p, vg2pr, vg2e, vg2v], axis=1)


print(dap)
print(country)
#print(df.drop(df.index[32:36])['Country'].to_string())