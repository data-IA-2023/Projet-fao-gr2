import pandas as pd
df_population2013=pd.read_csv("fao_2013/FAOSTAT_2013_population.csv")
df_animal2013=pd.read_csv("fao_2013/FAOSTAT_2013_animal.csv")
df_cereal2013=pd.read_csv("fao_2013/FAOSTAT_2013_cereal.csv")
df_sous_alimentation2013=pd.read_csv("fao_2013/FAOSTAT_2013_sous_alimentation.csv")
df_vegetal2013=pd.read_csv("fao_2013/FAOSTAT_2013_vegetal.csv")

tableau_population_animal = pd.merge(df_population2013,df_animal2013, how='outer', on='Code pays', indicator=True).query('_merge!="both"').drop(columns='_merge')