from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import re
import numpy as np
import pandas as pd
from full import full_image
from element_ss import element_image
search_query=input("Enter the word to search: ")
def get_value():
    path="C:\Program Files (x86)\chromedriver.exe"
    options = Options()
    
    options.add_argument('--headless')
    driver = webdriver.Chrome(path,options=options)
    driver.get('https://www.google.com/')
    language=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/a')

    language=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/a')
    if language != 'English':
        language.send_keys(Keys.RETURN)
   
    
        try:
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'//div/input[1]'))
            )

            element.send_keys(search_query)
            element.send_keys(Keys.RETURN)
            image_path="C:\\Users\\aakan\\OneDrive\\Desktop\\In\\task1"
            if not os.path.exists(f"{image_path}\\{search_query}"):
                os.makedirs(f"{image_path}\\{search_query}")
            full_image(image_path,search_query,driver)
            element_image(image_path,search_query,driver)
            main=driver.find_elements(By.XPATH,'//div[@class="g Ww4FFb vt6azd tF2Cxc" or @jscontroller="SC7lYd"]')
            t=all_value(main)[0]
            d=all_value(main)[1]
            l=all_value(main)[2]
            # i=all_value(main)[3]
            create_csv(search_query,t,d,l)
        finally:
            print("Value stored")
    else: 
        pass
def all_value(main):
    link_result=[]
    title_result=[]
    description_result=[]
    for m in main:
        link=m.find_elements(By.XPATH,".//h3[@class='LC20lb MBeuO DKV0Md']//parent::a")
        title=m.find_elements(By.XPATH,".//div[@class='yuRUbf']//h3 | .//h3")
        description=m.find_elements(By.XPATH,'.//div[contains(@class,"VwiC3b")]')
        for l in link:
            if l.get_attribute("href")!="":
                link_result.append(l.get_attribute("href"))
            else:
                link_result.append("Not Found")
        for t in title:
            if t.text!="":
                title_result.append(t.text)
            else:
                title_result.append("Not Found")
    
        for d in description:
            if d.text!="":
                description_result.append(d.text)
            else:
                    description_result.append("Not Found")
    return[title_result,description_result,link_result]


def create_csv(s,t,d,l):

    dictonary={"Search_Query":s,"Title":t[:5], "Description":d[:5],"Link":l[:5]}
    df=pd.DataFrame(dictonary,columns=['Search_Query','Title', 'Description', 'Link'])

    df["Description"] = df['Description'].str.replace((".*—")," ",regex=True)
    df.to_csv(f'{search_query}.csv',index=False)

get_value()

