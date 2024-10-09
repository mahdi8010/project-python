from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import time 
import random as rn




id=''
password=''
hastag=""

#tedad=int(input("tedad lotfan ? "))
tedad=10
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(8)

s1=driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
s1.send_keys(id)
time.sleep(8)
s2=driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
s2.send_keys(password)

time.sleep(9)
s3=driver.find_element_by_css_selector('#loginForm > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB > button').click()

time.sleep(8)

b=driver.get(f'https://www.instagram.com/explore/tags/{hastag}/')

time.sleep(4)
i=0
b=driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(4)
v=range(int(tedad))
for i in v : 
      b1=driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
      post=driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(8) > div:nth-child(1) > a > div.eLAPa > div._9AhH0').click()

      time.sleep(4)
      follo=driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
      text=follo.text
      print(f't={text}')

      b=driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
      
      if text =='Follow':
         follow =driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button').click()
         time.sleep(3)
         like=driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button').click()
         time.sleep(3)
         exit_post=driver.find_element_by_css_selector('body > div._2dDPU.QPGbb.CkGkG > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > div > svg').click()
      else:
         exit_post=driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.NOTWr > button').click()  

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

driver.close()


print('tamam shod')
