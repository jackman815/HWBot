from selenium import webdriver


def grab_courses_list(mycourses):
    courses = []
    for course in mycourses:
        courses.append([course.find_element_by_tag_name('a').get_attribute('innerHTML'),
                        course.find_element_by_tag_name('a').get_attribute('href')])
    return courses
