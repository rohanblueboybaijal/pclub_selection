import requests
from bs4 import BeautifulSoup
import pandas as pd 
from selenium import webdriver
import re

url = 'https://summerofcode.withgoogle.com/archive/2019/projects/'

driver = webdriver.Chrome('/usr/bin/chromedriver')

driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

items = driver.find_elements_by_class_name("archive-project-card__student-name")

names =[]
projects = []
organisations =[]


data = soup.findAll("md-card")

for d in data:
    stud_name=d.find('a', href=True)
    stud_name = d.find('a', href= True).text
    names.append(stud_name)
    x = d.div.findAll('div')
    projects.append(x[0].text)
    org = x[1].text
    s = re.split(":", org)
    organisations.append(s[1])

print(len(names))
print(len(projects))
print(len(organisations))

df = pd.DataFrame({'Name': names, 'Organisation':organisations, 'Project':projects})
df.to_csv('Details.csv', index=False, encoding = 'utf-8')
