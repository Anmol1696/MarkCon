import os.path
import datetime
from clustering import *

# def init():
# 	global csv
# 	global items
# 	global address_mapping
csv = {}
items = {}
address_mapping = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'O']

class Item:
	def __init__(self, name):
		self.name = name
		self.quantity = 0
		self.amount = 0
		self.address = [0 for i in range(12)] # A B C D E F G H I J  L  O
											  # 0 1 2 3 4 5 6 7 8 9 10 11

def generate_csv(name):
	# global csv
	# global items
	# global address_mapping
	if name not in csv.keys():
		csv_new = None
		if os.path.isfile(name):
			csv_new = open((name + '.csv'), 'a')
			csv_new.write('\n')
		else:
			csv_new = open((name + '.csv'), 'w')
			csv_new.write('Week, Quantity, Amount, A, B, C, D, E, F, G, H, I, J, L, O\n') # ADDRESSLIST to be implemented
		csv[name] = csv_new
		return 0
	return -1

def close_csv():
	# global csv
	# global items
	# global address_mapping
	for key in csv.keys():
		csv[key].close()

def add_data(item, quantity, amount, address):
	# global csv
	# global items
	# global address_mapping
	item = item_clustering(item)
	address = address_clustering(address)
	print item
	if item not in items.keys():
		items[item] = Item(item)
	items[item].quantity += quantity
	items[item].amount += amount
	items[item].address[address_mapping.index(address)] += quantity

def load_data(week):
	# global address_mapping
	global csv
	global items
	print '----------------' + str(week)
	for name, item in items.items():
		# Need to implement address storage after info is received
		if name not in csv.keys():
			generate_csv(name)
		csv[name].write(str(week) + ', ' + str(item.quantity) + ', ' + str(item.amount) + ', ' + str(item.address[0]) + ', ' + \
						str(item.address[1]) + ', ' + str(item.address[2]) + ', ' + str(item.address[3]) + ', ' + str(item.address[4]) + ', ' + \
						str(item.address[5]) + ', ' + str(item.address[6]) + ', ' + str(item.address[7])  + ', ' + str(item.address[8]) + ', ' + \
						str(item.address[9]) + ', ' + str(item.address[10]) + ', ' + str(item.address[11]) + '\n')
	items = {}
