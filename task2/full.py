def full_image(path,query,driver):
    height = driver.execute_script("return document.body.parentNode.scrollHeight")
    width = driver.execute_script("return document.body.parentNode.scrollWidth")
    driver.set_window_size(width, height)
    driver.save_screenshot(f'{path}\\{query}\\_full.png')