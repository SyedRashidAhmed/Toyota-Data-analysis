import pandas as pd
import numpy as np
df=pd.read_csv('Toyota.csv')
print(df)
print(df.columns)
print(df.dtypes)
print(pd.unique(df['KM']))
print(np.unique(df['KM'])) #sorting in ascending order if spwcial chars pulled to last
junks=[]
junks.append('??')
print(np.unique(df['HP']))
junks.append('????')
print(pd.unique(df['FuelType']))
print(pd.unique(df['Doors']))
df=pd.read_csv('Toyota.csv',na_values=junks)        # to convert junk values to nan values
df['Doors'].replace('three',3,inplace=True)
df['Doors'].replace('four',4,inplace=True)
df['Doors'].replace('five',5,inplace=True)
df['Doors'].replace('3',3,inplace=True)
df['Doors'].replace('4',4,inplace=True)
df['Doors'].replace('5',5,inplace=True)
df['Doors'].replace('2',2,inplace=True)
(pd.unique(df['Doors']))
(df.dtypes)
(df['FuelType'].astype('category'))#add print where required ->()
(pd.unique(df['FuelType']))
df['FuelType']=df['FuelType'].astype('category')#converting the fueltype to its category
(df.dtypes)
(df.isnull().sum())
print(pd.value_counts(df['FuelType']))
df=df.fillna(method='ffill')                     #filling nan values with forward values ffill method
print(df)
print(df.isnull().sum())
print(df)
print(df.duplicated()) #to check if duplicated rows
print(df[df.duplicated()]) #to check if duplicated rows in all
del df['Unnamed: 0']
print(df.columns)
print(df[df['Doors']==3]) #to print the rows where doors are 3
print((622/1436)*100)
print(df[df['Doors']==4],'\n',(138/1436)*100)
print(pd.crosstab(df['Automatic'],df['Doors'])) #to make a crosstab or view like dbms
print(round(df['Age']/12),1)
df['Age']=round(df['Age']/12,1)
df.insert(1,'price_class','')
print(df)
for i in range(len(df['Price'])):
    if df['Price'][i]<=8450:
        df['price_class'][i]='Low'
    elif df['Price'][i]>8450 and df['Price'][i] <11951:
        df['price_class'][i]='Mid'
    else:
        df['price_class'][i]='High'
print(df)
df['abc']=1
print(df)    
print(pd.crosstab(df['price_class'],df['abc']))
print(df.value_counts(df['price_class'])) #function to solve it in better way
del (df['abc'])
print(df)
print(pd.crosstab(df['Price'],df['Doors']))
print(pd.crosstab(df['price_class'],df['Doors']))