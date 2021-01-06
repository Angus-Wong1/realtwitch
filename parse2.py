import pyautogui
import pickle
import os
import requests
from selenium import webdriver
import time
import urllib
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from rapidtag import tag
from shuffle import shuffle
with open('twitchdict.pickle','rb') as pi:
    d = pickle.load(pi)
with open('trackingId.csv','r') as tr:
    trackingIds = tr.read().split(',')

pyautogui.FAILSAFE = True
fp = webdriver.FirefoxProfile()
options = Options()
#options.headless = True
mp4Path = []
jpgPath = []



def upload(title,description,tags,mp4):
    print('start upload')
    browser = webdriver.Firefox(firefox_profile=fp,options=options)

    browser.get('https://www.youtube.com')

    with open('data.pickle','rb') as f:
        data = pickle.load(f)
    for i in data:
        browser.add_cookie(i)
    time.sleep(.5)
    browser.get('https:/www.youtube.com/upload')

    browser.implicitly_wait(10)
    browser.find_element_by_xpath("//input[@type='file']").send_keys(mp4)

    browser.implicitly_wait(10)
    time.sleep(1)
    title_field = browser.find_element_by_id('textbox')
    title_field.click()
    time.sleep(.1)
    title_field.clear()
    time.sleep(.2)
    browser.implicitly_wait(1)
    title_field.click()
    time.sleep(.1)
    title_field.clear()
    time.sleep(.1)
    title_field.send_keys(title)
    time.sleep(1)

    time.sleep(1)
    browser.implicitly_wait(10)
    desc = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div')
    time.sleep(1)
    desc.click()
    time.sleep(2)
    desc.clear()

    time.sleep(2)
    browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div').send_keys(description)

    time.sleep(3)

    browser.implicitly_wait(10)
    time.sleep(1)
    browser.find_element_by_name('NOT_MADE_FOR_KIDS').click()

    browser.implicitly_wait(10)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="details"]/div/div/ytcp-button/div').click()

    time.sleep(2)
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-advanced/ytcp-form-input-container/div[1]/div[2]/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input').send_keys(tags)

    time.sleep(2)
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div').click()

    time.sleep(1)
    browser.implicitly_wait(10)
    browser.find_element_by_id('next-button').click()
    time.sleep(.5)
    browser.implicitly_wait(10)
    browser.find_element_by_name('PUBLIC').click()

    time.sleep(2)
    browser.implicitly_wait(10000000)
    browser.find_element_by_xpath("//*[text()='Finished processing']")
    browser.find_element_by_id('done-button').click()
    time.sleep(3)

    browser.close()


def getMp4(arg):
    browser = webdriver.Firefox(firefox_profile=fp,options=options)

    browser.get(arg)
    browser.refresh()
    html = browser.page_source

    soup = BeautifulSoup(html,'lxml')
    links = soup.find('video')
    browser.close()

    if type(links.get('src')) == str:
        return(links.get('src'))
    else:
        getMp4(arg)


def downloadMp4(video_links):

    shuffle()
    dirpath = os.getcwd()

    for link in video_links:
        index = video_links.index(link)
        up = open('uploaded.txt','r+')
        uplist = up.read().split(',')
        file_name = link.split('/')[-1]
        #thumb = str((d['thumbnails'][index])).split(',')[0]
        mp4url = d['url'][index]
        poop = mp4url.index('?')
        fuckly = mp4url[0:poop]

        if d['slug'][index] not in uplist:
            try:
                names = (d['broadcaster'][index])
                tagstring = tag(names['name'])
                print(names)
                urllib.request.urlretrieve(getMp4(fuckly),dirpath+'/Mp4/'+file_name)
                games = (d['game'][index])
                titles = (d['title'][index])

                upload(names['name']+': '+titles,'Credits: https://www.twitch.tv/'+names['name']+' #'+ games +' #'+names['name'],tagstring,dirpath+'/Mp4/'+file_name)
                time.sleep(2)

            except TypeError:
                print('TypeError')


            finally:
                print('uploaded')
                up.write(','+d['slug'][index])
                up.close()


        mp4Path.append(dirpath+'/Mp4/'+file_name)
        os.chdir(dirpath + '/Mp4')
        mp4list = [os.remove(mp4) for mp4 in os.listdir(dirpath+'/Mp4')]
        os.chdir(dirpath)
downloadMp4(trackingIds)
