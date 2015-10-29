def csv_form():
	csv_file = open('people_info.csv', 'w')
	csv_file.write("Name, Gender, Lives, Job, Education\n")
	csv_file.close()
	csv_file = open('similar_pages.csv', 'w')
	csv_file.close()

def add_info(person):
	csv_file = open('people_info.csv', 'a')
	csv_file.write("%s, %s, %s, %s, %s\n" % (person.name, person.sex, person.lives, person.job, person.education))
	csv_file.close()

def similar_pages_csv(page):
	csv_file = open('similar_pages.csv', 'a')
	csv_file.write(page + '\n')
	csv_file.close()
