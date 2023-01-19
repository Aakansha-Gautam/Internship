from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def get_value(search_query,id,path_):
    path="C:\\Program Files (x86)\\chromedriver.exe"
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(path,options=options)
    driver.get('https://www.google.com/')
    language = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/div/div/a')))
    if language != 'English':
        language.send_keys(Keys.RETURN)
   
    
        try:
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'//div/input[1]'))
            )

            element.send_keys(search_query)
            element.send_keys(Keys.RETURN)
            main=driver.find_elements(By.XPATH,'//div[contains(@class,"g Ww4FFb") or contains(@jscontroller,"SC7lYd")]')
            t=all_value(main)[0]
            d=all_value(main)[1]
            l=all_value(main)[2]
            create_csv(search_query,t,d,l,path_)
        finally:
            print("Value stored")
    else: 
        pass
def all_value(main):
    link_result=[]
    title_result=[]
    description_result=[]
    for m in main:
        link=m.find_elements(By.XPATH,'.//h3[@class="LC20lb MBeuO DKV0Md"]//parent::a')
        title=m.find_elements(By.XPATH,'.//h3[@class="LC20lb MBeuO DKV0Md"]')
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


def create_csv(s,t,d,l,path_):
    dictonary={"Search_Query":s,"Title":t[:5], "Description":d[:5],"Link":l[:5]}
    df=pd.DataFrame(dictonary,columns=['Search_Query','Title', 'Description', 'Link'])

    df["Description"] = df['Description'].str.replace((".*—")," ",regex=True)
    df.to_csv(f'{path_}.csv',index=False)
    database(f'{path_}.csv')

def database(file):
    try:
        engine = create_engine("postgresql+psycopg2://postgres:1223@localhost:5432/first")
        df2=pd.read_csv(file,encoding="utf-8")
        df2.to_sql(name='final',con=engine,index=False,if_exists='append')
        print("file copied to db")
    except(Exception,psycopg2.DatabaseError) as e:
        print (e)



