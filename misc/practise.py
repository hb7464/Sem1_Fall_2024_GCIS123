'''def dicsount(age):
	if age < 10:
		disc = .5
	
	elif 10 <= age <= 18:
		disc = .3
	
	elif age > 60:
		disc = .2
	
	else:
		disc = 0

	return disc


def amount(tariff_standard, age):
	
	disc = dicsount(age)
	price = tariff_standard * (1-disc)
	
	return price

def main():
	print(f'For a standard tariff of 30DHS and children aged 9 it is: {amount(30,9)}')
	print(f'For a standard tariff of 20DHS and for child aged 16 it is: {amount(20,16)}')
	print(f'For a standard tariff of 35DHS and children aged 40 it is: {amount(35,40)}')
'''
'''def readnumbers():
	with open('number.txt') as f:
		s = 0
		for lines in f:
			s+= float(lines)
		print(f"Sum is {s}")

def main():
	readnumbers()
'''
if __name__ == '__main__':
	main()