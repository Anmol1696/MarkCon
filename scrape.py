from selenium import webdriver
import time

def web_scrape(username = "avrio@juicifix.com", password = "Juici12345!"):
	baseurl = 'http://login.petpooja.com/users/login'
	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 0)
	driver = webdriver.Firefox(profile)
	driver.get(baseurl)

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

	driver.get("http://login.petpooja.com/orders/order_list/all")

	'''
	item = a[82].text.split(" ")[: -4]
	add = row[75].text.split(" ")[2:-4]
	'''

	pages = 2

	for page in range(pages):
		time.sleep(1)
		action = driver.find_elements_by_xpath(xpaths['action'])

		for i in range(2,12):
			num = 1
			item = []
			action[i].click()
			time.sleep(2)
			row = driver.find_elements_by_xpath("//tr")
			address = row[len(row) - 11].text
			item.append(row[len(row) - 4].text)

			while row[len(row) - 4 + num].text[0] != ' ':
				item.append(row[len(row) - 11 + num].text)
				num += 1
			print item
		time.sleep(0.5)
		driver.find_elements_by_xpath(xpaths['next'])[0].click()



if __name__ == "__main__":
	print web_scrape()
