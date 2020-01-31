

from selenium import webdriver
from bs4 import BeautifulSoup
import re
# import webbrowser
import time
import os


print("Initialized scraper")
print("Please Enter Your 9anime url \n")
url = input()

driver = webdriver.Chrome()
driver.get(url)


# no need to click tab again and again
tab = driver.find_element_by_xpath('//span[@data-name="35"]')
driver.execute_script("arguments[0].click();", tab)

episodes = driver.find_elements_by_css_selector('.server[data-name="35"] a')
for link in episodes:
    # episodeUrl = "https://9anime.to"+x[link]
    # driver.get(episodeUrl)
    driver.execute_script("arguments[0].click();", link)
    time.sleep(5)
    iframe = driver.find_element_by_xpath(
        '//iframe[@style="width: 100%; height: 100%;"]')
    driver.switch_to.frame(iframe)
    videoUrl = driver.find_element_by_tag_name('video').get_attribute("src")

    # driver.get(videoUrl)

    # efficient to start download from js as driver doesnt get side tracked
    driver.execute_script("window.open('"+videoUrl+"')")

    # driver switch back to default from iframe
    driver.switch_to.default_content()

driver.close()
