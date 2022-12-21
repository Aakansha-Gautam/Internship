from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
# path="C:\Users\aakan\Downloads\Downloaded_Application\driver\chromedriver.exe"
# path = "C:\Program Files (x86)\chromedriver.exe"
# driver=webdriver.Chrome(path)



path="C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(path)
# driver.get('https://www.google.com/')


def result(search_query):
    browser=driver.get('https://www.google.com/')
    box=browser.find_element(By.XPATH,'//div[@class="a4bIc"]//input')
    box.send_keys(search_query)
    box.submit()
    link=browser.find_elements(By.XPATH,'//div[@class="yuRUbf"]//cite').get_attribute("href")
    result=[]
    for l in link:
        print(l)
        result.append(l)
    browser.close()
    return result

search_query=input("Enter the query to be searched: ")
result(search_query)

#     title=browser.find_elements(By.XPATH,'//div[@class="yuRUbf"]//h3').text
#     description=browser.find_elements(By.XPATH,'//div[@class="IsZvec"]//span').text
# # file=open('Task.csv','w')
# file.write('Link,Title,Description')


# # creating the csv file:
# # path="C:\Program Files (x86)\chromedriver.exe"
# # # driver= webdriver.Chrome(path)
# # driver.get('https://www.google.com/')



# # try:
# #     element=WebDriverWait(driver,10).until(
# #         EC. presence_of_element_located((By.XPATH,'//input[@class="gLFyf"]'))
# #     )
# search=driver.find_element(By.XPATH,'//div[@class="a4bIc"]//input')
# search.send_keys(search_query)
# search.submit()
# search.find_elements(By.XPATH,'//div[@class="tF2Cxc"]')
#     # for m in main:
#     #     link=m.find_elements(By.XPATH,'//div[@class="yuRUbf"]//cite').get_attribute("href")
#     #     title=m.find_elements(By.XPATH,'//div[@class="yuRUbf"]//h3').text
#     #     description=m.find_elements(By.XPATH,'//div[@class="IsZvec"]//span').text
#     # output=[]
#     # for i in link:
#     #     output.append(link[i])
#     # print(output)

#     #     file.write(link.replace(","," ")+","+title.replace(","," ")+","+description.replace(","," ")+"/n")
#     # file.close()
# # except:
# #     file.write(link.replace(","," ")+","+title.replace(","," ")+","+description.replace(","," ")+"/n")
# #     file.close()
#     # driver.quit()
#     # output=[]
#     # for i in link:
#     #     output.append(link[i])
#     # print(output)

# # output=[]
# # for i in link:
# #     output.append(link[i])
# # print(output)


# # import time
# # # path="C:\Users\aakan\Downloads\Downloaded_Application\driver\chromedriver.exe"
# # path = "C:\Program Files (x86)\chromedriver.exe"
# # driver=webdriver.Chrome(path)

# # #task 1:
# # driver.get('https://techwithtim.net')
# # # # close the webpage 
# # # # driver.close() as soon as the websie opens it closes
# # # # driver.quit()
# # # # print(driver.title)
# # # search=driver.find_element("name","s")
# # # search.send_keys("test")
# # # search.send_keys(Keys.RETURN)


# # # main= driver.find_element("id","main")
# # # print(main.text)

# # #task 2:
# # # we will be using a webbrowser where we will be searching things up and printing it in the terminal
# # #accessing element in html
# # # while acccessing the data from the webpaage first we should search on the basis of the id if not name and at last class

# # # driver.get("https://www.daraz.com.np/#")

# # # search=driver.find_element("id","q")
# # # search.send_keys("fryer")
# # # search.send_keys(Keys.RETURN)


# # # # revision:
# # # path=""
# # # driver.Chrome(path)
# # # driver.get("link")
# # # driver.title

# # # driver.find_element("id",'dfd')
# # # driver.send_keys("test")
# # # deriver.send_keys(Keys.RETUR
# # # N)
# # #navigating between the pages:
# # # link=driver.find_element("link_text","Python Programming")
# # # link.click()

# # try:
# #     element=WebDriverWait(driver,10).until(
# #         EC. presence_of_element_located((By.LINK_TEXT,"Python Programming"))
# #     )
# #     element.click()

# # except:
#     # driver.quit()
