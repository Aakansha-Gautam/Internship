from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

search_query=input("Enter the query to be searched: ")
path="C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(path)

file=open('Task.csv','w')
writer=csv.writer(file)
writer.writerow('Link,Title,Description')

# creating the csv file:
path="C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(path)
driver.get('https://www.google.com/')



try:
    element=WebDriverWait(driver,10).until(
        EC. presence_of_element_located((By.XPATH,'//input[@class="gLFyf"]'))
    )
    # search=driver.find_element(By.XPATH,'//input[@class="gLFyf"]')
    element.send_keys(search_query)
    element.submit()
    main=element.find_element(By.XPATH,'//div[@class="tF2Cxc"]')
    for m in main:
        link=driver.find_element(By.XPATH,'//div[@class="yuRUbf"]//cite')
        title=m.find_element(By.XPATH,'//div[@class="yuRUbf"]//h3').text
        description=m.find_element(By.XPATH,'//div[@class="IsZvec"]//span').text
        writer.writerow(link.replace(","," ")+","+title.replace(","," ")+","+description.replace(","," ")+"/n")
    file.close()
except:
    driver.quit()

writer.writerow(link.replace(","," ")+","+title.replace(","," ")+","+description.replace(","," ")+"/n")
file.close()


#xpath python
# link-class="iUh30 qLRx3b tjvcx"
# title-class="LC20lb MBeuO DKV0Md"
# description- class="Z26q7c UK95Uc"

# selenium
# link-class="TbwUpd NJjxre"
# title-class="LC20lb MBeuO DKV0Md"
# description- class="IsZvec"
