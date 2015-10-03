from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login import web_driver
import time

def open_page(page_url = 'https://www.facebook.com/juicifix'):
	driver = web_driver()
	driver.get(page_url)
	time.sleep(2)
	return driver

def pagelikes():
	driver = open_page()
	time.sleep(5)
	like_links = []
	profile_links = []

	for _ in range(2):
		driver.find_element_by_xpath('//div').send_keys(Keys.PAGE_DOWN)
		time.sleep(1)

	for element_like in driver.find_elements_by_xpath("//div[@class = 'UFILikeSentenceText']//a[@class='UFINoWrap']"):
		if element_like.get_attribute('href') not in like_links:
			like_links.append(element_like.get_attribute('href'))

	for element_like in driver.find_elements_by_xpath("//div[@class = 'UFILikeSentenceText']//a[@class='profileLink']"):
		if element_like.get_attribute('href') not in profile_links:
			profile_links.append(element_like.get_attribute('href'))

	profile_from_links = get_profile(driver, like_links[2:])
	for profile in profile_from_links:
		if profile not in profile_links:
			profile_links.append(profile)

	return profile_links[1:]

def get_profile(driver, like_links):
	profile_links = []
	for url in like_links:
		driver.get(url)
		time.sleep(3)
		temp = driver.find_elements_by_xpath("//li[@class = 'fbProfileBrowserListItem']//div[@class = 'fsl fwb fcb']/a")
		for element in temp:
			if element.get_attribute('href') not in profile_links:
				profile_links.append(element.get_attribute('href'))
	return profile_links


if __name__ == '__main__':
	print pagelikes()
