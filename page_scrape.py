from selenium import webdriver
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

if __name__ == '__main__':
	open_page()
