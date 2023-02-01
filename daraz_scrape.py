from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd
from sqlalchemy import create_engine
import os
from sqlalchemy import create_engine
from full import full_image
from element_ss import element_image
import psycopg2
connected=None
cursor=None
  
def get_value_daraz(filename,id):
    path="C:\\Program Files (x86)\\chromedriver.exe"
    option = Options()
    option.add_argument('--headless')
    driver=webdriver.Chrome(path,options=option)
    try:
        # connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
        # cursor=connected.cursor()
        # insert=f'''update scrape_info set platform='daraz' where id={id}'''
        # cursor.execute(insert)
        driver.get('https://www.daraz.com.np/#')
        with open(filename,'r')as file:
            for i in file.readlines():
                driver.get('https://www.daraz.com.np/#')
                element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'//input[@id="q"]'))
                )
                element.send_keys(i.strip())
                element.send_keys(Keys.RETURN)
                i_path="C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\files"
                image_path=os.path.join(i_path,id+"_daraz")
                if not os.path.exists(image_path):
                    os.mkdir(image_path)
                final=os.path.join(image_path,i.strip())
                if not os.path.exists(final):
                    os.mkdir(final)
                full_image(final,i.strip(),driver)
                element_image(final,i.strip(),driver)
                main=driver.find_elements(By.XPATH,'//div[contains(@class,"box--ujueT")]')
                title=all_value(main)[0]
                price=all_value(main)[1]
                link=all_value(main)[2]
                create_csv(id,i,title,price,link)
    # except psycopg2.DatabaseError as e:
    #     print(e)
    finally:
        # if connected is not None:
        #     connected.close()
        # if cursor is not None:
        #     cursor.close()
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

def create_csv(id,s,t,p,l):
    dictonary={"Id":id,"Search_Query":s,"Title":t,"Price":p,"Link":l}
    df=pd.DataFrame(dictonary,columns=['Id','Search_Query','Title','Price','Link'])
    df['Price']=df['Price'].str.replace("^Rs.","",regex=True)
    df2 = df.stack().reset_index()
    df2= df2.rename(columns={'level_0': 'Index','level_1':'Topic', 0: 'Value'})
    column_length=df.columns[:]
    c_l=len(column_length)
    df2.drop(df2.loc[df2['Topic']=="index"].index, inplace=True)
    i=0
    j=1
    indexing=[]
    first_value=df.iloc[0].Search_Query
    for d in df['Search_Query']:
        i+=1
        if(first_value!=d):
            j+=1
            i=1
            first_value=d
        for a in range (1,c_l+1):
            indexing.append(str(j)+"."+str(i)+"."+str(a))
    df2['Index']=pd.Series(indexing)
    engine = create_engine("postgresql+psycopg2://postgres:1223@localhost:5432/first")
    df2.to_sql(name='final_daraz',con=engine,index=False,if_exists='append')
    # connected=None
    # cursor=None
    # try:
    #     connected=psycopg2.connect(host="localhost",user="postgres",password=1223,database="first")
    #     cursor=connected.cursor()
    #     insert=f'''update scrape_info set platform='daraz' where id={id}'''
    #     cursor.execute(insert)

    # except psycopg2.DatabaseError as e:
    #     print(e)
    # finally:
    #     if connected is not None:
    #         connected.close()
    #     if cursor is not None:
    #         cursor.close()



