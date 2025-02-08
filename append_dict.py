import csv
new_student=[{'name':'heta','branch':'bca','year':'2','cgpa':'8.5'},
	{'name':'rekha','branch':'bba','year':'3','cgpa':'7.9'}]

file=open('f2.csv','a')
fields=list(new_student[0].keys())
dict_writer=csv.DictWriter(file,fieldnames=fields)
dict_writer.writerows(new_student)
file.close()