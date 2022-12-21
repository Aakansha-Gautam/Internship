from  selenium import webdriver

# path="C:\Users\aakan\Downloads\Downloaded_Application\driver\chromedriver.exe"
path = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get('https://www.youtube.com/')