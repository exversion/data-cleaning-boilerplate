import csv

dirty_csv = 'dirty_csv.csv' #This is the file you have
clean_csv = 'clean_csv.csv' #This is the file python will create


with open(dirty_csv) as f:
	dr = csv.DictReader(f)
	#Write new dataset
	fn = dr.fieldnames #Automatically carry the columns over as is. To remove columns or alter the schema, change this to a custom list that will match the clean data
	with open(clean_csv,'wb') as f2:
		dw = csv.DictWriter(f2, delimiter=',', fieldnames=fn, quoting=csv.QUOTE_NONNUMERIC)
		dw.writerow(dict((fns,fns) for fns in fn))
		for r in dr:
			#########################
			#|
			#| Do your cleaning here
			item = r
			#|
			#|
			#########################
			try:
				dw.writerow(item)
			except: #will keep one bad row from breaking the whole process
				print item