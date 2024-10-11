import re, csv

def zip_checK(Filepath):
	with open(Filepath) as f:
		A = csv.reader(f)
		next(A)

		for i in A:
			
			Zipcode = i[-1]
			print(f'Name <{i[0]}> | Zipcode <{Zipcode}>')
			
			if re.findall('^[7-9]',Zipcode) != []:
				print(Zipcode,'Starts with 7,8 or 9')
				print()

Filepath = r"C:\Users\hisha\gcis123\hb7464\misc\csv_zip.csv"
#Filepath = input(r"Enter filepath")

zip_checK(Filepath)
