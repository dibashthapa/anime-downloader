
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import webbrowser
import time
import os
print("Initialized scraper")
print("Please Enter Your 9anime url \n")
url=input()

driver = webdriver.Chrome()
driver.get(url)
soup=BeautifulSoup(driver.page_source,"html.parser")
fileWrite= open("output.html","w")
fileWrite.write(str(soup))
webbrowser.get("firefox")
f=open("output.html","r")
f1=f.readlines()
x=re.findall("/[\w]+/[\w]+-[\w]+-[\w]+[.0-9a-z]+/[0-9a-z]+",str(f1))
urls=[]
length=len(x)//3


for link in range(length*2,len(x)):
    episodeUrl="https://9anime.to"+x[link]
    driver.get(episodeUrl)
    tab = driver.find_element_by_xpath('//span[@data-name="35"]')
    driver.execute_script("arguments[0].click();", tab)
    episodes = driver.find_elements_by_css_selector('.server[data-name="35"] a')
    driver.execute_script("arguments[0].click();", episodes[0])
    time.sleep(5)
    iframe = driver.find_element_by_xpath(
        '//iframe[@style="width: 100%; height: 100%;"]')
    driver.switch_to.frame(iframe)
    videoUrl = driver.find_element_by_tag_name('video').get_attribute("src")
    time.sleep(3)

    driver.get(videoUrl)
    time.sleep(3)

driver.close()
