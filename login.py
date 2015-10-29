from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def web_driver(email = '', password = ''):
	baseurl = 'https://www.facebook.com/login'
	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 0)
	driver = webdriver.Firefox(profile)
	driver.set_page_load_timeout(30)
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

if __name__ == "__main__":
	web_driver()
