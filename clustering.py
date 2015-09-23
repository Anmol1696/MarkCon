list_item = ['3 days fix', '5 days fix vegetable', 'jolly weekdays detox', 'jolly weekdays detox', '5 days fix fruit', 'jolly weekdays', 'jolly weekdays alternate', \
			'5 days fix alternate', '15 days fix fruit', '15 days fix', '15 days fix detox', '15 days fix vegetable', '30 days fix detox', \
			'30 days fix', '30 days fix alternate', '90 days alternate', '90 days detox', '90 days fix', '30 days kiddie fix', '15 days kiddie fix', \
			'30 days fixkiddie fix', '15 days fixkiddie fix', 'cleanse 6', 'cleanse 8', 'cleanse 4', 'cleanse 3', '3 day fix', '5 day fix vegetable',\
			'jolly weekday detox', 'jolly weekday detox', '5 day fix fruit', 'jolly weekday', 'jolly weekday alternate', \
			'5 day fix alternate', '15 day fix fruit', '15 day fix', '15 day fix detox', '15 day fix vegetable', '30 day fix detox', \
			'30 day fix', '30 day fix alternate', '90 day alternate', '90 day detox', '90 day fix', '30 day kiddie fix', '15 day kiddie fix', \
			'30 day fixkiddie fix', '15 day fixkiddie fix']

name_item = ["Sample", "Sub-5-V", "Sub-5-V", "Sub-5-V", "Sub-5-F", "Sub-5-F", "Sub-5-FV", "Sub-5-FV", "Sub-15-F", "Sub-15-F", "Sub-15-F", "Sub-30-V", "Sub-30-FV", \
			"Sub-30-F", "Sub-30-FV", "Sub-90-A", "Sub-30-V", "Sub-90-F", "Sub-30-F", "Sub-15-F", "Sub-30-F", "Sub-15-F", "6B-1D", "8B-1D", "cleanse custom", "cleanse custom",\
			"Sample", "Sub-5-V", "Sub-5-V", "Sub-5-V", "Sub-5-F", "Sub-5-F", "Sub-5-FV", "Sub-5-FV", "Sub-15-F", "Sub-15-F", "Sub-15-F", "Sub-30-V", "Sub-30-FV", \
			"Sub-30-F", "Sub-30-FV", "Sub-90-A", "Sub-30-V", "Sub-90-F", "Sub-30-F", "Sub-15-F", "Sub-30-F", "Sub-15-F"]

list_address = ["andheri", "jvlr", "lokhandwala", "oshiwara", "vile", "malad", "goregaon", "kandivali", "borivali", "bandra", "sion", "santacruz", \
				"khar", "dadar", "wadala", "parel", "matunga", "powai", "ghatkopar", "mulund", "chembur", "mira", "bhayandar", "dahisar", "colaba", \
				"churchgate", "nariman", "cuffe", "thane", "breach", "malabar", "grant", "charni", "dockyard", "mazgaon", "sector", "juhu", "kandivili", "marine"]
				# , "any sort of Sector implies navi mumbai"
phrase_address = ["mumbai 01", "mumbai 02", "mumbai 04", "mumbai 05", "mumbai 06", "mumbai 07"]
p_name_address = ['H', 'H', 'G', 'G', 'G', 'G']

name_address = ['C','C','C','C','C','A','A','A','A','B','D','D','D','I','I','I','E','E','E','E','E','F','F',"F","H","H","H","H","J", "G", "G","G","G","L","L", "J", "C", "A", "H"]

other_item = []
other_address = []

def item_clustering(item):

	item = item.lower()
	item = item.translate(None, '()&!?.,:;-/')
	item = ' '.join(item.split())

	if item in list_item:
		name = name_item[list_item.index(item)]
	else:
		name = 'Others'
		other_item.append(item)

	return name

def address_clustering(address):
	address = address.lower()
	address = address.translate(None, '()&!?.,:;-/')
	address_clean = ""

	for i in address:
		if i != '\n':
			address_clean += i
		else:
			address_clean += ' '

	address = address_clean

	address = ' '.join(address.split())

	for x in range(6):
		if phrase_address[x] in address:
			return p_name_address[x]

	for ad in address.split(" "):
		if ad in list_address:
			return name_address[list_address.index(ad)]

	other_address.append(address)
	return 'O'

def other_list():
	return (other_item, other_address)
