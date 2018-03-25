import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df=pd.read_csv('/Users/carrielin/Desktop/0324result/02-yuxin/02-yuxin-trans/r2_result(-6bdu).csv')


# for syllable 
df['new']=df['stimuli'].str[:2] #split letter and num 
df['acc']=np.where(df['response']==df['new'],'1','0')

# for tone 
df['tone']=df['stimuli'].str[-1:] #extract last number of the syllable (i.e. tone)
df['acc']=np.where(df['response']==df['tone'],'1','0')


df.to_csv('/Users/carrielin/Desktop/0324result/02-yuxin/02-yuxin-trans/r2_result(-6bdu)_final.csv')
#save one time 

