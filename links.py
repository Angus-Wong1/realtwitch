from selenium import webdriver
from remove import remove
from time import sleep
from selenium.webdriver.firefox.options import Options
f = open("top100slugs.txt","w+")
options = Options()
options.headless = True
def poop(url):
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    driver.implicitly_wait(10)
    i = 1
    while i <= 200:
        links = driver.find_elements_by_xpath("//a[@data-a-target='preview-card-image-link']")
        driver.execute_script('arguments[0].scrollIntoView(true);', links[len(links)-1])
        print(i)
        i+=20
        sleep(1)

    links = driver.find_elements_by_xpath("//a[@data-a-target='preview-card-image-link']")
    for link in links:
        f.write(str(link.get_attribute('href'))+ ",")

    driver.close()
x = ['https://www.twitch.tv/directory/game/Just%20Chatting/clips?range=7d','https://www.twitch.tv/directory/game/Among%20Us/clips?range=7d','https://www.twitch.tv/directory/game/League%20of%20Legends/clips?range=7d']
for i in x:
    poop(i)


remove()
