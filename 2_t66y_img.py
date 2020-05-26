# coding:utf-8
import os
import cv2 as cv
from bs4 import BeautifulSoup
import re
import requests
import time

httpimg = re.compile(r'ess-data="(http\S*\.(png|jpg|jpeg))"')
httptorr=re.compile(r'http://www.rmdown.com/link.php\?hash=[a-zA-Z0-9]{0,200}')

l=[]
proxies={ "http": "http://127.0.0.1:20196", "https": "http://127.0.0.1:20196", } 
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

headers2 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 't66y.com',
            
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/53 7.36'
            
        }


def gethtml(url):
# url='https://t66y.com/htm_data/2005/26/3942503.html'

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    response = requests.get(url,headers=headers,proxies=proxies)
    soup=BeautifulSoup(response.text,'lxml')
    print(response)
    return soup


def product_imgandlink(soup): # 获取目标链接

    dlink=re.findall(httptorr,str(soup))
    imgs_link = re.findall(httpimg,str(soup)) #找寻所以符合表达式的字符
    return dlink,imgs_link



def img_download(url,name): # 下载图片模块
    import requests
    proxies={ "http": "http://127.0.0.1:20196", "https": "http://127.0.0.1:20196", } 
    r = requests.get(url,headers=headers2,proxies=proxies)
    with open('./t66y_26/'+name+'.jpg', 'wb') as f:
        f.write(r.content)  


def validateTitle(title): # 替换windows文件名不允许的字符 该模块代码来源：https://www.polarxiong.com/archives/Python-%E6%9B%BF%E6%8D%A2%E6%88%96%E5%8E%BB%E9%99%A4%E4%B8%8D%E8%83%BD%E7%94%A8%E4%BA%8E%E6%96%87%E4%BB%B6%E5%90%8D%E7%9A%84%E5%AD%97%E7%AC%A6.html
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


if __name__ == "__main__":

    f = open("20200525_26.txt","r",encoding="utf-8")               
    lines = f.readlines()  
    for line in lines:
        l.append(line.split('￥'))  

    f.close()  
    d = open("20200525_26_zzlink.txt","a",encoding="utf-8")   # 读取先前的txt
    for i in range(0,len(l)):
        # print(str(l[i][1]))
        
        soup=gethtml(str(l[i][1][0:46]))
        # time.sleep(10)
        # print(soup)

        try:
            dlink,imgs_link=product_imgandlink(soup)
        except:
            print(str(i)+' product_imgandlink失败')
        name=str(l[i][0])
        name=validateTitle(name)
        for j in range(0,len(imgs_link)):
            print("进度："+str(i/100)+"%")
            # print(imgs_link[j][0])
            # print(i)
            # print(j)
            try:
                img_download(str(imgs_link[j][0]),name+str(j)) # 下载图片
            except:
                print(str(i)+' img_download失败')
        try:

            d.write(name+'￥'+str(dlink[0])+'\n') # 将name和种子链接写入txt
            print(i)
        except:
            print(str(i)+' d.write失败')
    d.close()

        

