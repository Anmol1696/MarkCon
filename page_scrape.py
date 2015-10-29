from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login import web_driver
from profile import main_profile
import time

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

def main():
	profiles = []
	f = open("phone/new_number.csv", 'r')
	numbers = f.readlines()
	f.close()

	f = open("profiles_1.csv", 'a')

	print len(numbers)

	driver = web_driver()

	for number in numbers:
		number = int(number[:-2])
		try:
			temp = get_profile_id(open_page(number, driver))
			profile = temp[0].split("?")[0]
			driver = temp[1]
			if profile not in profiles:
				profiles.append(profile)
				f.write(profile + ',\n')
				print profile
		except:
			pass
	main_profile(profiles, driver)

if __name__ == '__main__':
	main()
