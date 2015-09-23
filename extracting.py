from data_store import *
ref_week = [63]

def extract(address, item_s, date):
	print date
	address = ' '.join(str(address).split(" ")[2:-4])

	for item_a in item_s:
		item_mod = ' '.join((str(item_a).split(" ")[:-4]))
		cost = int(str(item_a).split(" ")[-1])
		quantity = int(str(item_a).split(" ")[-3])
		week = date_week(date)

		if week < ref_week[-1]:
			load_data(week)
			ref_week.append(week)
		else: pass

		add_data(item_mod, quantity, cost, address)

def date_week(date):
	date = str(date).split("-")
	print date
	if int(date[0]) == 2015 or (int(date[1]) == 12 and int(date[2] > 28)):
			add = 24
	else: add = -28
	print int(date[0])
	week = datetime.date(int(date[0]), int(date[1]), int(date[2])).isocalendar()[1] + add
	return week
