import csv
import sys

f = open('all_data.csv', 'rt')
writer = open('all_part.js', 'wt' )

reader = csv.reader(f)

writer.write('var airPoints = [\n')
for row in reader:
	if row[5] != 'no2':
		#writer.write('[%s,%s,%.2f],\n'%(row[3],row[4],(float(row[5])*100)) )
		writer.write('[%s,%s,%s],\n'%(row[3],row[4],row[6]) )

writer.write('];')

f.close()
writer.close()
