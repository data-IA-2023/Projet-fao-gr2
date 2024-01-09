import pandas as pd
import numpy as np
pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')
an = pd.read_csv('fao_2013/FAOSTAT_2013_animal.csv')

nour=pd.concat([an,vg],axis=0).sort_values(by=['Code Pays','Code Produit']).reset_index(drop=True)
countrypop=pd.concat([pop[['Country Code','Country']],pop['Value']*1000],axis=1)
unified_df=nour.merge(countrypop,how="left",left_on="Code Pays",right_on="Country Code")[["Code Élément","Code Produit", "Code Pays","Value","Valeur"]].rename(columns={"Value":"Population"})
values=pd.Series([unified_df[unified_df["Code Pays"]==i].pivot_table(values='Valeur', index='Code Produit', columns='Code Élément') for i in pop['Country Code']],index=pop['Country Code']).rename_axis("Code Pays")

print(values[351][645][2511])