import wget
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pyautogui
import time

driver = webdriver.Firefox()

url="https://www.kickassanime.rs/anime/death-note-dub-529702"
driver.get(url)

soup=BeautifulSoup(driver.page_source,"html.parser")

fileWrite= open("output.html","w")
fileWrite.write(str(soup))
f=open("output.html","r")
f1=f.readlines()
x=re.findall("/[a-z]+/[a-z]+-[\w]+-[\w]+-[\w]*[0-9]/[\w\d-]+",str(f1))

file=open("links.txt","w")
def getVideoURL(url):
    element= driver.find_element_by_id("player_html5_api")
    src= element.get_attribute("src")
    print(src)

for data in x:
    file.write(str(data)+"\n")

for links in x:
    episodeURL="https://www.kickassanime.rs"+links
    driver.get(episodeURL)
    time.sleep(8)
    pyautogui.click()
    time.sleep(5)
    pyautogui.click()
    time.sleep(10)
    getVideoURL(episodeURL)
driver.close()
