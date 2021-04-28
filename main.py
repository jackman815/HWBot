from function import *
from selenium import webdriver
import time



browser = webdriver.Chrome("chromedriver.exe")
browser.get(os.getenv("moodle_host")+"/my")
input()
timesortfrom = 1619452800
timesortto = 1620057600
data = getRecentEvents(fetchRecentEvents(getSesskey(browser), getCookies(browser), timesortfrom, timesortto))
browser.quit()
