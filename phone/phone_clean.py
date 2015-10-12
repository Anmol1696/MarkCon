def read_lines(name_file = "Numbers.csv"):
	f = open(name_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def main():
	lines = read_lines()
	numbers = []

	f = open('new_number.csv', 'a')
	for line in lines:
		if '"' not in line[:-1]:
			number = line[:-1].split(",")[1]
		elif '"' in line[:-1]:
			number = ''.join(line[:-1].split('"')[1].split(",")).split('.')[0]

		if type(number) is str:
			try:
				number = int(number)
			except:
				print number
		else: print number
		if type(number) is int and int(str(number)[0]) > 6 and str(number) not in numbers:
			if len(str(number)) >= 10:
				if len(str(number)) == 12:
					number = int(str(number)[2:])
				numbers.append(str(number))
				f.write(str(number) + ',\n')

	f.close()

if __name__ == '__main__':
	main()
