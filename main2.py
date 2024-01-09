import pandas as pd
import numpy as np
pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')
an = pd.read_csv('fao_2013/FAOSTAT_2013_animal.csv')

nour=pd.concat([an,vg],axis=0).sort_values(by=['Code Pays','Code Produit']).reset_index(drop=True)
pop_pays=pd.concat([pop['Country Code'],pop['Value']*1000],axis=1).rename(columns={"Country Code":"Code Pays","Value":"Population"})
df_uni=nour.merge(pop_pays,on="Code Pays")[["Code Élément","Code Produit", "Code Pays","Population","Valeur"]]
valeurs=pd.Series([nour[nour["Code Pays"]==i].pivot_table(values='Valeur', index='Code Produit', columns='Code Élément') for i in pop['Country Code']],index=pop['Country Code']).rename_axis("Code Pays")

print(df_uni)
print(valeurs)
print(pop_pays)