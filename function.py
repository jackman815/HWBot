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


def fetch_all_assin(browser):
    mycourses = browser.find_element_by_class_name('mycourses').find_elements_by_tag_name('li')
    courses = grab_courses_list(mycourses)
    data = []

    for course in courses:
        activitys = []
        browser.get(course[1])
        topics = browser.find_elements_by_css_selector('.topics>li')
        for topic in topics:
            activity_list = []
            for activity in topic.find_elements_by_css_selector('.content>.section.img-text>.activity'):
                if (len(activity.find_elements_by_class_name('contentwithoutlink')) > 0):
                    continue
                current_activity = activity.find_element_by_css_selector('.activityinstance')
                activity_list.append([current_activity.find_element_by_css_selector('.instancename').text,
                                      current_activity.find_element_by_css_selector(
                                          '.activityinstance>a').get_attribute('href')])

            activitys.append([topic.find_element_by_css_selector('.sectionname>span>a').get_attribute('innerHTML'),
                              activity_list])
        data.append([course[0], activitys])


def getCookies(browser):
    cookies = {}
    for cookie in browser.get_cookies():
        cookies[cookie['name']] = cookie['value']
    return cookies


def getMCfg(browser):
    return browser.execute_script("return M.cfg")


def getSesskey(browser):
    return browser.execute_script("return M.cfg['sesskey']")


def fetchRecentEvents(sesskey, mcookies, timesortfrom,timesortto):
    postData = [{"index": 0, "methodname": "core_calendar_get_action_events_by_timesort",
                 "args": {"limitnum": 26, "timesortfrom": timesortfrom, "timesortto": timesortto,
                          "limittononsuspendedevents": True}}]
    link = os.getenv("moodle_host")+"/lib/ajax/service.php?sesskey=" + sesskey + "&info=core_calendar_get_action_events_by_timesort"
    r = requests.post(link, verify=False, cookies=mcookies, data=json.dumps(postData))
    return r


def getRecentEvents(response):
    response = json.loads(response.text)
    events = response[0]['data']['events']
    for i in events:
        print(i)
    return events
