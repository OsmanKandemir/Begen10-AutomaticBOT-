#! /usr/bin/env python
#! -*- coding : utf-8 -*-

import re
import mechanize
import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select



#CodingFacebookShareLikeBot #OsmanKandemir
#Site : http://begen10.com/index.php

print """

	
	Please get token from the begen10


	  """

entertoken = raw_input("Please Enter The Your Token : ")
likelink = raw_input("Please Enter The Your Share Link : ")

browser = webdriver.Firefox()
browser.get("http://begen10.com/index.php")
count = 0

while count <= 1:
	count = count + 1
	token = browser.find_element_by_id("token")
	token.send_keys(entertoken)
	log_but2 = "//input[@class='btn btn-success btn-lg']"
	browser.find_element_by_xpath(log_but2).click()


#browser.find_element_by_xpath(".//*[@id='bekleyin']/form/fieldset/div/div[2]/div/select[1]/option[text()='male']").click()

browser.find_element_by_xpath(".//*[@id='bekleyin']/form/fieldset/div/div[2]/div/select[1]/option[5]").click() #SelectBox
head = browser.find_element_by_xpath("//input[contains(@class, 'validate[required]')]")
#browser.find_element_by_classname("validate[required]")
head.send_keys(likelink)

log_but3 = "//input[@id='Gonderiliyor']"
browser.find_element_by_xpath(log_but3).click()


while(1):
	
	log_but4 = "//li[@class='graphs']"
	browser.find_element_by_xpath(log_but4).click()
	time.sleep(5)
	log_but5 = "//li[@class='link']"
	browser.find_element_by_xpath(log_but5).click()
	time.sleep(1)
	if not 'id="theTime"' in browser.page_source.encode("utf-8"):
		browser.find_element_by_xpath(".//*[@id='bekleyin']/form/fieldset/div/div[2]/div/select[1]/option[5]").click() #Select Box
		head = browser.find_element_by_xpath("//input[contains(@class, 'validate[required]')]")
		head.send_keys(likelink)
		log_but3 = "//input[@id='Gonderiliyor']"
		browser.find_element_by_xpath(log_but3).click()
		
