# coding:utf-8
import os
import cv2 as cv
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
firefox_options = Options()
firefox_options.add_argument("--headless")  # 让firefox在后台不显示界面
driver = webdriver.Firefox(options=firefox_options)     # 打开 firefox 浏览器


l=[]

f = open("20200525_26.txt","r",encoding="utf-8")               
lines = f.readlines()  
for line in lines:
    l.append(line.split('￥'))   
f.close()  
wait = WebDriverWait(driver, 20)

driver.get(str(l[0][1]))
html = driver.page_source       # get html
soup = BeautifulSoup(html, "html.parser")

# cv.imwrite('./img/'+str(l[0][0])+'.jpg', img)

repattern = re.compile(r"ess-data='(.*?)'")
imgs_link = re.findall(repattern,str(soup))
print(imgs_link)

# s = open('a.txt','a',encoding="utf-8")
# s.write(str(soup))
# s.close

driver.close()