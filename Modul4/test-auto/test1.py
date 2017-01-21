from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest2,os,time
try:
    data="Hi.How are you?"
    dir = os.path.dirname(__file__)
    chromedriver = "C:/Users/swatch/Desktop/test-auto/chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    driver.get('http://chatbot-lbcswatch.rhcloud.com/wasluianca.html')


    timp_f=[0]*100
    st=0;
    for i in range(0,100):
        st=time.time()
        driver.find_element(By.ID,value="msg").send_keys(data)
        driver.find_element(By.ID,value="msg").send_keys(u'\ue007')
        timp_f[i]=time.time()-st
        print(time.time()-st)
    rez=0
    for i in range(0,100):
        rez+=timp_f[i]
    print(rez/100)
    open("timp_r.txt","wb").write("Input : "+data+" ? \r\n Numar teste: 100 \r\n Acelasi input: Da \r\n Timp mediu :"+str(rez/100))
except AttributeError:
    print "error"