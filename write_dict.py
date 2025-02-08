
import csv
fields=['name','branch','year','cgpa']

mydict=[{'branch':'coe','cgpa':'9.0','name':'nikhil','year':'2'},
	{'branch':'coe','cgpa':'9.1','name':'sanchit','year':'2'},
	{'branch':'it','cgpa':'9.3','name':'aditya','year':'2'},
	{'branch':'se','cgpa':'9.5','name':'sagar','year':'1'},
	{'branch':'mce','cgpa':'7.8','name':'prateek','year':'3'},
	{'branch':'ep','cgpa':'9.1','name':'sahil','year':'2'}]
file=open('f2.csv','w')
fields=list(mydict[0].keys())
writer=csv.DictWriter(file,fieldnames=fields)
writer.writeheader()
writer.writerows(mydict)
file.close()