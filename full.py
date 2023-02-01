def full_image(path,query,driver):
    height = driver.execute_script("return document.body.parentNode.scrollHeight")
    width = driver.execute_script("return document.body.parentNode.scrollWidth")
    driver.set_window_size(width, height)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot(f'{path}\\_full{query}.png')