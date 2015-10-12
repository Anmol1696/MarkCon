from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import socket
from extracting import *
from data_store import *

def web_scrape(username = "avrio@juicifix.com", password = "Juici12345!"):
	socket.setdefaulttimeout(20)

	baseurl = 'http://login.petpooja.com/users/login'
	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 0)
	driver = webdriver.Firefox(profile)
	try:
		driver.get(baseurl)
	except socket.timeout:
		driver.find_element_by_xpath('//div').send_keys(Keys.ESCAPE)

	xpaths = {
		'username' : "//input[@name = 'email']",
		'password' : "//input[@name = 'password']",
		'login' : "//button[@type = 'submit']",
		'action' : "//a[@href = 'javascript:void(0)']",
		'next' : "//a[@rel = 'next']"
	}

	try:
		driver.find_element_by_xpath(xpaths['username']).send_keys(username)
		driver.find_element_by_xpath(xpaths['password']).send_keys(password)
		driver.find_element_by_xpath(xpaths['login']).click()
	except:
		print 'Not working'
		return 0
	time.sleep(1)

	try:
		driver.get("http://login.petpooja.com/orders/order_list/all")
	except socket.timeout:
		driver.find_element_by_xpath('//div').send_keys(Keys.ESCAPE)

	pages = 95

	dates = []

	# for x in range(pages):
	# 	time.sleep(1)
	# 	driver.find_elements_by_xpath(xpaths['next'])[0].click()

	for page in range(pages):
		time.sleep(2)
		action = driver.find_elements_by_xpath(xpaths['action'])

		for i in range(2,12):
			num = 0
			item = []
			action[i].click()
			time.sleep(2)

			row = driver.find_elements_by_xpath("//tr")
			time.sleep(2)
			#print row[i-1].text.split(" ")[-2]
			date = row[i-1].text.split(" ")[-2].split("\n")[-1]

			try:
				while row[len(row) - 4 + num].text[0] != ' ':
					item.append(str(row[len(row) - 4 + num].text))
					num -= 1
					time.sleep(0.5)
			except:
				pass

			time.sleep(2)

			final = find(item)
			print page
			extract(final[1], final[0], date)

		time.sleep(2)
		driver.find_elements_by_xpath(xpaths['next'])[0].click()

def find(total):
	item = []
	for li in total:
		line = li.split(" ")
		for word in line:
			if str(word) == 'Address':
				address = line
			if str(word) == 'Unit':
				num = total.index(li)
	for x in range(num):
		if total[x].split(" ")[0] != 'Discount':
			item.append(total[x])
	address = ' '.join(address)
	if len(item) == 0:
		print 'wrong'
	return (item, address)


if __name__ == "__main__":
	print web_scrape()
	print other_list()
