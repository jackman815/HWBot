import os

from selenium import webdriver
import json
import requests
from dotenv import load_dotenv
load_dotenv()


def grab_courses_list(mycourses):
    courses = []
    for course in mycourses:
        courses.append([course.find_element_by_tag_name('a').get_attribute('innerHTML'),
                        course.find_element_by_tag_name('a').get_attribute('href')])
    return courses


def getCookies(browser):
    cookies = {}
    for cookie in browser.get_cookies():
        cookies[cookie['name']] = cookie['value']
    return cookies


def getMCfg(browser):
    return browser.execute_script("return M.cfg")


def getSesskey(browser):
    return browser.execute_script("return M.cfg['sesskey']")


def getRecentEvents(sesskey, mcookies):
    postData = [{"index":0,"methodname":"core_calendar_get_action_events_by_timesort","args":{"limitnum":6,"timesortfrom":1619452800,"timesortto":1620057600,"limittononsuspendedevents":True}}]
    link = "https://moodle2021.vtc.edu.hk/lib/ajax/service.php?sesskey="+sesskey+"&info=core_calendar_get_action_events_by_timesort"
    r = requests.post(link, verify=False, cookies=mcookies, data=json.dumps(postData))
