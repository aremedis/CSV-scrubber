### Intended to remove the preceding " ' " from the chargebacks csv###



import csv
import sys
import datetime

today = str(datetime.date.today())



filein = '/Users/<USERNAME>/Downloads/'+sys.argv[-1]
fileout = '/Users/<USERNAME>/.Trash/temp.tmp'
fileout2 = '/Users/<USERNAME>/Desktop/'+today+' Amex_Chargebacks.csv'

with open(filein, 'rb') as infile, open(fileout, 'wb') as outfile:
	reader = csv.reader(infile)
	writer = csv.writer(outfile)



	conversion = set("'")
	for row in reader:
		newrow = [''.join("" if c in conversion else c for c in entry) for entry in row]
		writer.writerow(newrow)


##replaces the "Days Left" from the Due Date Field, leaving just the date  ###


def replace_all(text, dic):
	for i in dic:
		text = text.replace(i,"")
	return text

f_list = ["-%s" % i for i in reversed(range(1,21))] 

with open(fileout, 'rb') as temp:
	text = temp.read()
	text = replace_all(text, f_list)

with open(fileout2, 'wb') as final:
	final.write(text)
