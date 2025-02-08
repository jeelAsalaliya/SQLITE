import pandas as pd

data={
	'Item_no':['I01','I02','I03','I04','I05'],
	'Item_name':['AC','TV','Microwave','Refrigerator','Dish Washer'],
	'Qty':[100,200,300,400,500],
	'Price':[30000,20000,50000,60000,40000]
      }
df=pd.DataFrame(data)
df.to_csv('Q7.csv',index=False)

df['Total'] = df['Qty']*df['Price']
df.to_csv('Q7.csv',index=False)

print('---Display item name and price between 20000 and 35000----')
df_filter=df[(df['Price']>=20000) & (df['Price']<=35000)]
print(df_filter.loc[:,['Item_name','Price']])

print()
print('----Alternate record----')
print(df.iloc[0::2])

print()
print('----Minimum and Maximum-----')
df_min=df[df['Price']==df['Price'].min()]
print(df_min.loc[:,['Item_name','Price']])

df_max=df[df['Price']==df['Price'].max()]
print(df_max.loc[:,['Item_name','Price']])

print()
print('---Sort the data Itemname-wise in ascending and descending order---')
print(df.sort_values(by=['Item_name']))
print(df.sort_values(by=['Item_name'],ascending=False))

print()
print('---Display rows between 3rd to 5th row---')
print(df.iloc[2:5])

print()
print('---Display last 2 rows---')
print(df.tail(2))