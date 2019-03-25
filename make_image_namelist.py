import pandas as pd
import os


names = os.listdir('data/images')
names = sorted(names)
names = [i  for i in names if i.endswith('.jpg')]


df = pd.DataFrame(names)
df.reset_index(inplace=True)
df.columns = ['id', 'image']
df['id'] = range(1, len(names)+1)
df.to_csv('data/name_list.tsv', sep='\t')
