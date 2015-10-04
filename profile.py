from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login import web_driver
from form_csv import *
import time
import unicodedata

xpaths = {
	'name' : "//div[@class = '_6-e']",
	'sex' : "//div[@class = 'lfloat _ohe']",
	'lives' : "//ul[@class = 'uiList _1pi3 _4kg _6-h _703 _4ks']/li[3]",
	'job' : "//ul[@class = 'uiList _1pi3 _4kg _6-h _703 _4ks']/li[1]",
	'education' : "//ul[@class = 'uiList _1pi3 _4kg _6-h _703 _4ks']/li[2]"
}

class Info:
	def __init__(self, url = None, name = None, sex = None, lives = None, job = None, education = None):
		self.name = name
		self.sex = sex
		self.lives = lives
		self.job = job
		self.education = education
		self.url = url

def main_profile(profile_links, driver):
	csv_form()

	for link in profile_links:
		single_profile(link, driver)
		time.sleep(1)

def single_profile(url, driver):
	driver.get(url + u'/about')
	person = Info(url)
	person.name = unicodedata.normalize('NFKD', getting_name(driver)).encode('ascii','ignore').replace(',','-')
	person.sex = unicodedata.normalize('NFKD', getting_sex(driver)).encode('ascii','ignore').replace(',','-')
	person.lives = unicodedata.normalize('NFKD', getting_lives(driver)).encode('ascii','ignore').replace(',','-')
	person.job = unicodedata.normalize('NFKD', getting_job_education(driver, 'job')).encode('ascii','ignore').replace(',','-')
	person.education = unicodedata.normalize('NFKD', getting_job_education(driver, 'education')).encode('ascii','ignore').replace(',','-')

	add_info(person)

def getting_name(driver):
	return driver.find_element_by_xpath(xpaths['name']).text

def getting_sex(driver):
	try:
		text = str(driver.find_element_by_xpath(xpaths['sex']).text)
		print text
	except: return '-'

	if " him " in text or " he " in text:
		return u'M'
	elif " she " in text or " her " in text:
		return u'F'
	else: return u"-"

def getting_lives(driver):
	try:
		location_text = driver.find_element_by_xpath(xpaths['lives']).text.split('\n')[0]
	except:
		return u'-'

	if 'No' not in location_text:
		return location_text.split("Lives in")[1]
	else: return u'-'

def getting_job_education(driver, var):
	job_text = driver.find_element_by_xpath(xpaths[var]).text.split('\n')[0]
	if 'No' not in job_text:
		return job_text
	else: return u'-'

if __name__ == "__main__":
	single_profile()
