from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login import web_driver
from profile import main_profile
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
		if check_true_caller(driver, a.text):
			numbers.append(a.text)
	return numbers[0]

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
		print numbers[0]
	return (driver, numbers[0])

def get_numbers():
	numbers = []
	base = get_series()
	driver = base[0]
	f.open('profiles_people.txt', 'a')
	for series_num in base[1]:
		numbers.append(get_final_number(driver, series_num))
		try:
			# open_page(get_final_number(driver, series_num), driver)
			profile = get_profile_id(open_page(get_final_number(driver, series_num), driver)[1])[0]
			f.write(profile + '\n')
		except:
			pass
	f.close()

	return numbers

def open_page(number, driver):
	# driver = web_driver()
	page_url = "https://www.facebook.com/search/str/%s/keywords_users" % (str(number))
	driver.get(page_url)
	time.sleep(2)
	return driver

def get_profile_id(driver):
	xpaths = {
		'profile_id' : "//div[@class = 'clearfix']//a[@class = '_8o _8s lfloat _ohe']"
	}

	profile = driver.find_element_by_xpath(xpaths['profile_id']).get_attribute('href')
	return (profile, driver)

def find_profiles


if __name__ == '__main__':
