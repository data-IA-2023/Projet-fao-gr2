import pandas as pd
import numpy as np
df = pd.read_csv("fao_2013\FAOSTAT_data_en_12-19-2023.csv",sep=',')


totalpop = df['Value'].sum()*1000
totalpop=int(totalpop)
print(totalpop)
