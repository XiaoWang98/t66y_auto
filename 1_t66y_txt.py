# coding:utf-8
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup

firefox_options = Options()
firefox_options.add_argument("--headless")  # 让firefox在后台不显示界面

driver = webdriver.Firefox(options=firefox_options)     # 打开 firefox 浏览器

for i in range(1,101): # 有一百页能访问到
    print('进度:     '+str(i)+'%')

    driver.get("https://t66y.com/thread0806.php?fid=26&search=&page="+str(i))
    html = driver.page_source       # get html

    soup = BeautifulSoup(html, "html.parser")
    data = soup.select('h3')        # 获取h3标签对应的那条语句
    print(len(data)) 
    # print(str(data[3])[13:42]) # 13：42是链接

    f = open('test.txt','a',encoding="utf-8")
    for j in range(0,len(data)):
        f.write(data[j].get_text()+'￥https://t66y.com/'+str(data[j])[13:42]+'\n')# get_text是获取语句中的标题
 
    f.close()


driver.close()
