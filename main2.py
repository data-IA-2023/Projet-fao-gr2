import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pop = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
vg = pd.read_csv('fao_2013/FAOSTAT_2013_vegetal.csv')
an = pd.read_csv('fao_2013/FAOSTAT_2013_animal.csv')
ce = pd.read_csv('fao_2013/FAOSTAT_2013_cereal.csv')
sa = pd.read_csv('fao_2013/FAOSTAT_2013_sous_alimentation.csv')

valeurs_sa=pd.Series([sa[sa["Code zone"]==i]["Valeur"].values[0]*10**6 for i in pop['Country Code']],index=pop['Country Code'])

nour=pd.concat([an,vg,ce],axis=0).sort_values(by=['Code Pays','Code Produit']).drop_duplicates().reset_index(drop=True)
pop_pays=pop['Value'].rename_axis("Population").set_axis(pop['Country Code'])*1000

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

ratio_eng=pd.Series([valeurs[i][664]/valeurs[i][645]*365 for i in pop['Country Code']],index=pop['Country Code']).rename_axis("Code Pays")
ratio_eng_moy=valeurs_moy[664]/valeurs_moy[645]*365


#Question 6 Calculez, pour les produits végétaux uniquement, la disponibilité intérieure mondiale exprimée en kcal.
print("La disponibilité intérieur mondiale est de : " + str((valeurs_4d["veg"]["tot"][5301]/ratio_eng_moy).sum()*10**6) + " kcal.")

#Question 11 Établissez la liste des produits (ainsi que leur code) considéré comme des céréales selon la FAO. En ne prenant en compte que les céréales destinées à l'alimentation (humaine et animale), quelle proportion (en termes de poids) est destinée à l'alimentation animale ?
print("Les codes des céréales sont : " + str(valeurs_4d["cer"]["tot"].index.tolist()))

print("Le rapport de céréales destinées à l'alimentation animale est : " + str(valeurs_4d["cer"]["tot"][5521].sum()/valeurs_4d["cer"]["tot"][5511].sum()))

#Question 13 Combien de tonnes de céréales pourraient être libérées si les USA diminuaient leur production de produits animaux de 10% ?
print(str(valeurs_4d["cer"][231][5521].sum()*100) + " tonnes de céréales pouraient être libérées si les USA diminuaient leur production de produits animaux de 10%.")

#Question 14 En Thaïlande, quelle proportion de manioc est exportée ? Quelle est la proportion de personnes en sous-nutrition?
print("La proportion de manioc exportée en Thaïlande est de : " + str(valeurs_4d["veg"][216][5911][2532]/valeurs_4d["veg"][216][5511][2532]))

print("La proportion de personnes en sous-nutrition est de : " + str(valeurs_sa[216]/pop_pays[216]))