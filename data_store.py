import os.path
import datetime
from clustering import *

csv = {}
item_list = ['3 day fix', '5 day fix vegetable', 'jolly weekday detox']
items = {}
address_mapping = {"andheri":1, "jvlr":2, "lokhandwala":3}

class Item:
	def __init__(name):
		self.name = name
		self.quantity = 0
		self.amount = 0
		self.address = [0 for i in range(len(address_mapping))]

def generate_csv(name):
	if name not in csv.keys():
		csv_new = None
		if os.path.isfile(name):
			csv_new = open((name + '.csv'), 'a')
			csv_new.write('\n')
		else:
			csv_new = open((name + '.csv'), 'w')
			csv_new.write('Week, Quantity, Amount, ADDRESSLIST\n') # ADDRESSLIST to be implemented
		csv[name] = csv_new
		return 0
	return -1

def close_csv():
	for key in csv.keys():
		csv[key].close()

def add_data(item, quantity, amount, address):
	if item in item_list:
		if item not in items.keys():
			items[item] = Item(item)
		items[item].quantity += quantity
		items[item].amount += amount
		items[item].address[address_mapping[address]] += 1

def load_data(week):
	if item not in csv.keys() and item in item_list:
		generate_csv(item)
	for name, item in items:
		# Need to implement address storage after info is received
		csv[name].write(str(week) + ', ' + str(item.quantity) + ', ' + str(item.amount) + ', ' + str(item.address) + '\n')
	items = {}
