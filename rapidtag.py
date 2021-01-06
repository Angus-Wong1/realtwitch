from tkinter import Tk
import selenium
import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
fp = webdriver.FirefoxProfile()
options = Options()
#options.headless = True
def tag(name):
    while True:
        try:

            root = Tk()
            print('tried getting tag')
            browser = webdriver.Firefox(firefox_profile=fp,options=options)
            browser.get('https://rapidtags.io/generator')
            browser.implicitly_wait(5)
            browser.find_element_by_id('searchInput').send_keys(name)
            browser.implicitly_wait(5)
            browser.find_element_by_class_name('icon-search').click()
            time.sleep(2)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            browser.implicitly_wait(5)
            copy = browser.find_element_by_class_name('copy')
            browser.execute_script("arguments[0].scrollIntoView();",copy)
            copy.click()
            time.sleep(.5)
            clip = root.clipboard_get()
            p = ''
            y = clip.split(',')[:-5]
            for i in y:
                p = p+i+','
            return p
            break
        except:
            print('failed \n')
            browser.close()
        finally:
            if 'normal' == root.state():
                root.quit()
                browser.close()
