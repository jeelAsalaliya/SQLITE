import pandas 
import numpy

data=[
	['neeta jain',20000],
	['beena patel',25000],
	['anju sharma',35000]
    ]

df=pandas.DataFrame(data)
np=df.to_numpy()
print(np)

data={
	'emp_name':['aaa','bbb','ccc'],
	'emp_sal':[9999,8888,7777]
     }

df=pandas.DataFrame(data)
np=df.to_numpy()
print(np)

data=[
	{'emp_name':'raj shah','emp_sal':5000},
	{'emp_name':'raj panchal','emp_sal':6000},
	{'emp_name':'raj purohit','emp_sal':7000},
     ]

df=pandas.DataFrame(data)
np=df.to_numpy()
print(np)