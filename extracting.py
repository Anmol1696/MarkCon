from data_store import data_log

def extract(address, items_s, date):
	address = ' '.join(str(address).split(" ")[2:-4])

	for item_a in item_s:
		item_mod = (str(item_a).split(" ")[:-4])
		cost = int(str(item_a).split(" ")[-1])
		quantity = int(str(item_a).split(" ")[-3])

		data_log(item_mod, quantity, cost, address, date)
