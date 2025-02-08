import pandas as pd
stud_data=[
	['isha','mca',80.7],
	['karan','BCOM',67.78],
	['priya','bba',57],
	['swati','ca',78] ]
w=pd.ExcelWriter('f4.xlsx')
df=pd.DataFrame(stud_data,index=['f0','f1','f2','f3'],columns=['name','degree','per'])
df.to_excel(w)
w.close()