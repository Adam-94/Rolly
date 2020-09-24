from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PIL import Image

import time

def screenshot(message):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get("https://radai.github.io/dnd5tools/?q="+message)
    time.sleep(0.5)

    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')

    driver.set_window_size(required_width, required_height)
    driver.find_element_by_css_selector("#results").screenshot("screenshot.png")  # avoids scrollbar
    driver.set_window_size(original_size['width'], original_size['height'])
