import pandas as pd

df = pd.read_csv('fao_2013/FAOSTAT_2013_population.csv')
#filetot=df['Value'].sum()*1000
#chinapop = df.drop(df.index[32:36])['Value'].sum()*1000
#df.index[df['Country'] == "China"].tolist()
totpop = df.drop(df.index[df['Country'] == "China"].tolist())['Value'].sum()*1000
#print(df.to_string())
#totpop = df['Value'].sum()*1000
print(totpop)
#print(filetot-chinapop)
#print(df.drop(df.index[32:36])['Country'].to_string())