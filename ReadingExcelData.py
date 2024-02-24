import pandas as p
import pandas as pd
import numpy as np


csv_file= 'World_GDP_Dataset.csv'

df_csv = pd.read_csv(csv_file)

print(df_csv)
print(df_csv.plot)

