import csv

file=open('f2.csv','r')
dict=csv.DictReader(file)

for row in dict:
	print(row)
file.close()