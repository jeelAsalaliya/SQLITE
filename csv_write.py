
import csv
fields=['name','branch','year','cgpa']

rows=[['nikhil','coe','2','9.0'],
	['sanchit','coe','2','9.1'],
	['aditya','it','2','9.3'],
	['sagar','se','1','9.5'],
	['prateek','mce','3','7.8'],
	['sahil','ep','2','9.1']]

filename='f1.csv'
file=open(filename,'w')
csv_writer=csv.writer(file)
csv_writer.writerow(fields)
csv_writer.writerows(rows)
file.close()