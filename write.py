import pandas as pd

data=[
	['aaa',20000],
	['bbb',25000],
	['ccc',35000] ]

df=pd.DataFrame(data)

df.to_csv('f3.csv','w')