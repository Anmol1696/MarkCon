from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def web_driver(email = 'anmol.y@zabbed.com', password = 'marcon123'):
	baseurl = 'https://www.facebook.com/login'
	driver = webdriver.Firefox()
	driver.get(baseurl)

	xpaths = {
		'email' : "//input[@name = 'email']",
		'password' : "//input[@name = 'pass']",
		'login' : "//input[@name = 'login']",
	}

	try:
		driver.find_element_by_xpath(xpaths['email']).send_keys(email)
		driver.find_element_by_xpath(xpaths['password']).send_keys(password)
		driver.find_element_by_xpath(xpaths['login']).click()
	except:
		return 0

	return driver


def open_page(page_url = 'https://www.facebook.com/juicifix'):
	driver = web_driver()
	driver.get(page_url)
	time.sleep(2)
	return driver

def pagelikes():
	driver = open_page()
	time.sleep(5)
	scrol_number = 10
	like_links = []
	# while scrol_number > 0:
	# 	driver.find_element_by_xpath('//div').send_keys(Keys.PAGE_DOWN)
	# 	list_likes = driver.find_elements_by_xpath("//div[@class = 'UFILikeSentenceText']")
	# 	for like in list_likes:
	# 		like_links.append(like.get_attribute('href'))
	# 	print like_links
	# 	scrol_number -= 1

	driver.find_element_by_xpath('//div').send_keys(Keys.PAGE_DOWN)
	time.sleep(1)
	list_likes = driver.find_elements_by_xpath("//div[@class = 'UFILikeSentenceText']")
	for l in list_likes:
		print l.get_attribute("href")
		print l.text



if __name__ == '__main__':
	pagelikes()
