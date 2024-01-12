import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')
an = pd.read_csv('fao_2013/FAOSTAT_2013_animal.csv')
ce = pd.read_csv('fao_2013/FAOSTAT_2013_cereal.csv')
sa = pd.read_csv('fao_2013/FAOSTAT_2013_sous_alimentation.csv')

poptop=pop[pop["Country Code"]!=351].sort_values(by="Value").tail(10)

nour=pd.concat([an,vg,ce],axis=0).sort_values(by=['Code Pays','Code Produit']).drop_duplicates().reset_index(drop=True)
pop_pays=pd.concat([pop['Country Code'],pop['Value']*1000],axis=1).rename(columns={"Country Code":"Code Pays","Value":"Population"})
df_uni=nour.merge(pop_pays,on="Code Pays")[["Code Élément","Code Produit", "Code Pays","Population","Valeur"]]

valeurs=pd.Series([nour[nour["Code Pays"]==i].pivot_table(values='Valeur', index='Code Produit', columns='Code Élément') for i in pop['Country Code']],index=pop['Country Code']).rename_axis("Code Pays")
valeurs_veg=pd.Series([vg[vg["Code Pays"]==i].pivot_table(values='Valeur', index='Code Produit', columns='Code Élément') for i in pop['Country Code']],index=pop['Country Code']).rename_axis("Code Pays")
valeurs_ani=pd.Series([an[an["Code Pays"]==i].pivot_table(values='Valeur', index='Code Produit', columns='Code Élément') for i in pop['Country Code']],index=pop['Country Code']).rename_axis("Code Pays")
valeurs_cer=pd.Series([ce[ce["Code Pays"]==i].pivot_table(values='Valeur', index='Code Produit', columns='Code Élément') for i in pop['Country Code']],index=pop['Country Code']).rename_axis("Code Pays")

valeurs_moy=nour.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément',aggfunc='mean')
valeurs_tot=nour.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément',aggfunc='sum')
valeurs_veg_tot=vg.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément',aggfunc='sum')
valeurs_veg_moy=vg.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément',aggfunc='mean')
valeurs_ani_tot=an.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément',aggfunc='sum')
valeurs_ani_moy=an.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément',aggfunc='mean')
valeurs_cer_tot=ce.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément',aggfunc='sum')
valeurs_cer_moy=ce.pivot_table(values='Valeur', index='Code Produit', columns='Code Élément',aggfunc='mean')

valeurs=pd.concat([valeurs,pd.Series([valeurs_moy,valeurs_tot],index=["moy","tot"])])
valeurs_ani=pd.concat([valeurs_ani,pd.Series([valeurs_ani_moy,valeurs_ani_tot],index=["moy","tot"])])
valeurs_veg=pd.concat([valeurs_veg,pd.Series([valeurs_veg_moy,valeurs_veg_tot],index=["moy","tot"])])
valeurs_cer=pd.concat([valeurs_cer,pd.Series([valeurs_cer_moy,valeurs_cer_tot],index=["moy","tot"])])

valeurs_4d=pd.Series([valeurs,valeurs_veg,valeurs_ani,valeurs_cer],index=["glob","veg","ani","cer"])

"""
ratio=pd.Series([valeurs[i][664]/valeurs[i][645]*365 for i in pop['Country Code']],index=pop['Country Code']).rename_axis("Code Pays")
ratio_moy=valeurs_moy[664]/valeurs_moy[645]*365
"""
#print(df_uni)
#print(valeurs_veg_tot[5301]*ratio_moy*10**6)
#print(valeurs_4d["ce"]["tot"].index.values.tolist())
#print([e for e in valeurs_4d["ce"]["tot"].index.values.tolist()])

#Question 11
print(valeurs_4d["cer"]["tot"][5521].sum()/valeurs_4d["cer"]["tot"][5511].sum())

#Question 13
print(valeurs_4d["cer"][231][5521].sum()*100)

#Question 14
print(valeurs_4d["veg"][216][5911][2532])
print((sa[sa["Code zone"]==216]["Valeur"].values*10**6/pop_pays[pop_pays["Code Pays"]==216]["Population"].values)[0])