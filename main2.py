import pandas as pd
import numpy as np
pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')
an = pd.read_csv('fao_2013/FAOSTAT_2013_animal.csv')

nour=pd.concat([an,vg],axis=0).sort_values(by=['Code Pays','Code Produit']).reset_index(drop=True)
countrypop=pd.concat([pop[['Country Code','Country']],pop['Value']*1000],axis=1)
unified_df=nour.merge(countrypop,how="left",left_on="Code Pays",right_on="Country Code")[["Code Élément","Code Produit", "Code Pays","Value","Valeur"]].rename(columns={"Value":"Population"})
values=unified_df.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément', aggfunc='first')
ratio=(values[664][values[664]!=0]/values[645]*365).rename_axis("ratio énergétique (Kcal/kg)")

print(ratio)