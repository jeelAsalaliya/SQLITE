import csv
file=open('f1.csv','r')
data=csv.DictReader(file)

for row in data:
	print(row)
file.close()