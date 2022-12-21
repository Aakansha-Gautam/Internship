import pandas as pd
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from full import full_image
from element_ss import element_image

search_query=input("Enter the word to be searched: ")
def get_value():
    
    path="C:\\Program Files (x86)\\chromedriver.exe"
    option = Options()
    option.add_argument('--headless')
    driver=webdriver.Chrome(path,options=option)
    driver.get('https://www.daraz.com.np/#')
    driver.maximize_window()
    # driver.set_window_size(1550,926)
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//input[@id="q"]'))
        )
        element.send_keys(search_query)
        element.send_keys(Keys.RETURN)
        image_path="C:\\Users\\aakan\\OneDrive\\Desktop\\In\\task2"
        if not os.path.exists(f"{image_path}\\{search_query}"):
            os.makedirs(f"{image_path}\\{search_query}")
        full_image(image_path,search_query,driver)
        element_image(image_path,search_query,driver)
        main=driver.find_elements(By.XPATH,'//div[contains(@class,"box--ujueT")]')
        t=all_value(main)[0]
        p=all_value(main)[1]
        l=all_value(main)[2]
        create_csv(search_query,t,p,l)
    finally:
        print("Value stored")
def all_value(main):
    title_result=[]
    price_result=[]
    link_result=[]
    for m in main:
        title=m.find_elements(By.XPATH,".//div[contains(@class,'title')]")
        price=m.find_elements(By.XPATH,'.//div[contains(@class,"price")]//span[contains(@class,"currency")] ')
        link=m.find_elements(By.XPATH,'.//div[starts-with(@class,"title")]//a')
        for t in title:
            if t.text!="":
                title_result.append(t.text)
            else:
                title_result.append("Not Found")
    
        for p in price:
            if p.text!="":
                price_result.append(p.text)
            else:
                price_result.append("Not Found")
        for l in link:
            if l.get_attribute("href")!="":
                link_result.append(l.get_attribute("href"))
            else:
                link_result.append("Not Found")

    return[title_result,price_result,link_result]



def create_csv(s,t,p,l):
    dictonary={"Search_Query":s,"Title":t,"Price":p,"Link":l}
    df=pd.DataFrame(dictonary,columns=['Search_Query','Title','Price','Link'])
    df['Price']=df['Price'].str.replace("^Rs.","",regex=True)
    df.to_csv('task2.csv',mode='a',index=False)

get_value()