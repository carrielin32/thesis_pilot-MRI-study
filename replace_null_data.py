
import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np 

df=pd.read_csv('/Users/carrielin/Desktop/behavior_data_all/01/s1-r1_result.csv')

df['RT'].where(df['RT']=='None').count() #check the number of null data

#df['response'].where(df['response']=='None').count() #same as above


#now replace the null data with '0'

df['RT']=df['RT'].replace('None','0')

#df['response']=df['response'].replace('None','0')



#extract stimuli parameter from raw data 

#make new column tone/syllable/phoneme
df['tone']=df['stimuli'].str[-1:]  #get_tone_number
df['syllable']=df['stimuli'].str[:2] #get_syllable
df['phoneme']=df['stimuli']

df['subj']='01' #01 till 20; add subject number to all that columns 
df['run']='1'


#now import txt as a new column in csv 
onset=pd.read_csv('/Users/carrielin/Desktop/logtime/01/s1_r1.txt', sep = " ", header = None)

onset=onset.transpose()
onset.columns=['onset_time']

# onset.isnull().sum()  #count the number of null data

onset=onset.dropna()

df['onset']=onset['onset_time']
#

#df_new=pd.concat([df,onset])

df.to_csv('/Users/carrielin/Desktop/data_new/01/s1_r1.csv') #save as new csv


#do one by one subj. 
#now concatenate each csv file 

df=pd.read_csv('/Users/carrielin/Desktop/data_new/02/s2_r1.csv')
df2=pd.read_csv('/Users/carrielin/Desktop/data_new/02/s2_r2.csv')
df3=pd.read_csv('/Users/carrielin/Desktop/data_new/02/s2_r3.csv')
df4=pd.read_csv('/Users/carrielin/Desktop/data_new/02/s2_r4.csv')

data_s2=pd.concat([df,df2,df3,df4])

data_s2.to_csv('/Users/carrielin/Desktop/data_new/02/s2_all.csv')

#concatenate all 
df=pd.read_csv('/Users/carrielin/Desktop/data_new/01/s1_all.csv')
df1=pd.read_csv('/Users/carrielin/Desktop/data_new/02/s2_all.csv')
df2=pd.read_csv('/Users/carrielin/Desktop/data_new/03/s3_all.csv')
df3=pd.read_csv('/Users/carrielin/Desktop/data_new/04/s4_all.csv')
df4=pd.read_csv('/Users/carrielin/Desktop/data_new/05/s5_all.csv')
df5=pd.read_csv('/Users/carrielin/Desktop/data_new/06/s6_all.csv')
df6=pd.read_csv('/Users/carrielin/Desktop/data_new/07/s7_all.csv')
df7=pd.read_csv('/Users/carrielin/Desktop/data_new/08/s8_all.csv')
df8=pd.read_csv('/Users/carrielin/Desktop/data_new/09/s9_all.csv')
df9=pd.read_csv('/Users/carrielin/Desktop/data_new/10/s10_all.csv')
df10=pd.read_csv('/Users/carrielin/Desktop/data_new/11/s11_all.csv')
df11=pd.read_csv('/Users/carrielin/Desktop/data_new/12/s12_all.csv')
df12=pd.read_csv('/Users/carrielin/Desktop/data_new/13/s13_all.csv')
df13=pd.read_csv('/Users/carrielin/Desktop/data_new/14/s14_all.csv')
df14=pd.read_csv('/Users/carrielin/Desktop/data_new/15/s15_all.csv')
df15=pd.read_csv('/Users/carrielin/Desktop/data_new/16/s16_all.csv')

data_all=pd.concat([df,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15])

data_all.to_csv('/Users/carrielin/Desktop/data_new/data_all.csv')

