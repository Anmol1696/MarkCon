import os.path

csv = {}

def generate_csv(name):
	if name not in csv.keys:
		csv_new = None
		if os.path.isfile(name):
			csv_new = open((name + '.csv'), 'a')
			csv_new.write('\n')
		else:
			csv_new = open((name + '.csv'), 'w')
			csv_new.write('Week, Quantity, Amount, Address\n')
		csv[name] = csv_new
		return 0
	return -1

def close_csv():
	for key in csv.keys():
		csv[key].close()

def add_data(week, item, quantity, amount, address):
	if item not in csv.keys():
		generate_csv(item)
	csv[item].write(str(week) + ', ' + str(quantity) + ', ' + str(amount) + ', ' + str(address) + '\n')
