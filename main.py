from function import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://moodle2021.vtc.edu.hk/")
input()
mycourses = browser.find_element_by_class_name('mycourses').find_elements_by_tag_name('li')
data = []

courses = grab_courses_list(mycourses)

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
                                  current_activity.find_element_by_css_selector('.activityinstance>a').get_attribute('href')])

        activitys.append([topic.find_element_by_css_selector('.sectionname>span>a').get_attribute('innerHTML'),
                          activity_list])
    data.append([course[0], activitys])
    #browser.implicitly_wait(1)
print(data)
browser.quit()

