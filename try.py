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


def get_value(filename,id):
    
    path="C:\\Program Files (x86)\\chromedriver.exe"
    option = Options()
    option.add_argument('--headless')
    driver=webdriver.Chrome(path,options=option)
    driver.maximize_window()
# driver.set_window_size(1550,926)
    try:
        driver.get('https://www.google.com')
        try:
            language = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,'English')))
            if language != 'English':
                language.send_keys(Keys.RETURN)
        except:
            pass
        with open(filename,'r')as file:
            search_query=file.readlines()
        for i in search_query:
            driver.get('https://www.google.com')
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'//div/input[1]'))
            )

            element.send_keys(i.strip())
            element.send_keys(Keys.RETURN)
            image_path="C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\files"
            if not os.path.exists(f"{image_path}\\{id}"):
                os.makedirs(f"{image_path}\\{id}")
            full_image(image_path,i,driver)
            element_image(image_path,i,driver)
            main=driver.find_elements(By.XPATH,'//div[contains(@class,"g Ww4FFb") or contains(@jscontroller,"SC7lYd")]')
            main=driver.find_elements(By.XPATH,'//div[contains(@class,"box--ujueT")]')
            title=all_value(main)[0]
            description=all_value(main)[1]
            link=all_value(main)[2]
            for r in range(0,len(title)):
                create_csv(i,title[r],description[r],link[r])
    finally:
        print("Value stored")
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
    df.to_csv(f'{s}.csv',index=False)



get_value(r"C:\Users\aakan\OneDrive\Desktop\flask\files\one2023_01_24_13_21_32_969491.txt",67)