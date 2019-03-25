import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv('data/name_list_features_tsne.tsv', sep='\t')
plt.plot(df.x[:23], df.y[:23], 'ro')
plt.plot(df.x[23:], df.y[23:], 'bo')

plt.savefig('data/plot_result.png', dpi=100)