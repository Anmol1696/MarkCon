from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from login import web_driver
# from profile import main_profile
import time

def open_page(page_url = 'http://www.xombom.com/mobile/vodafone-mobile-numbers/mumbai-metro/'):
	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 0)
	driver = webdriver.Firefox(profile)

	driver.get(page_url)
	time.sleep(5)
	return driver

def get_well(driver, url = None):
	numbers = []
	if url: driver.get(url)
	time.sleep(5)

	well = driver.find_elements_by_xpath("//div[@class = 'well']//a")

	for a in well:
		numbers.append(a.get_attribute('href'))

	return (driver, numbers)

def get_final_number(driver, url):
	numbers = []
	driver.get(url)
	time.sleep(5)

	well = driver.find_elements_by_xpath("//div[@class = 'well']//a")

	for a in well:
		numbers.append(a.text)
	return numbers

def get_base_numbers():
	numbers = []
	driver = open_page()
	# print numbers
 	return get_well(driver, None)

def get_series():
	base = get_base_numbers()
	driver = base[0]
	numbers = []
	for base_num in base[1]:
		numbers.append(get_well(driver, base_num)[1])
		print numbers
	return (driver, numbers)

def get_numbers():
	numbers = []
	base = get_series()
	driver = base[0]
	for series_num in base[1]:
		numbers.append(get_final_number(driver, series_num))
		print numbers
	return numbers

def check_true_caller(driver, number):
	facebook_numbers = []
	driver.get('https://www.truecaller.com/in/' + str(number))
	details = driver.find_element_by_xpath("//div[@class = 'detailView__list']").text

	if '@' in details:
		facebook_numbers.append(number)

if __name__ == '__main__':
	print get_numbers()
