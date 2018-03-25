import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/Users/carrielin/Desktop/0324result/02-yuxin/02-yuxin-trans/plot/r1_result(-4bdu)_final.csv')

means=df.groupby(['new'])[['acc']].mean()

errors=df.groupby(['new'])[['acc']].std()

fig, ax = plt.subplots()

means.plot.bar(yerr=errors, ax=ax)

plt.show()