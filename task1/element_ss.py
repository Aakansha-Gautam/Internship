from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def element_image(path,query,driver):
    # height=height = driver.execute_script("return document.body.parentNode.scrollHeight")
    width=driver.execute_script("return document.documentElement.scrollWidth")
    driver.set_window_size(1550,926)
    height=926
    page=driver.find_element(By.TAG_NAME,"body")
    # val=page.get_size()
    # h=val['height']
    page_height = driver.execute_script("return document.documentElement.scrollHeight")
    print(page_height)
    i=1
    scrolled=0
    while True:
        driver.save_screenshot(f'{path}\\{query}\\_{i}{query}.png')
        scrolled= driver.execute_script("return window.pageYOffset + window.innerHeight")
        page.send_keys(Keys.PAGE_DOWN)
        print(scrolled,page_height)
        i+=1
        if (scrolled+1)>= page_height:  #//4012 //4938
            break