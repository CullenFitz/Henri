import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from speak import speak
import webbrowser

def getNews():
    speak("Ok. getting you some news. This may take a moment.")
    print("Gathering News...")

    url = "https://www.cnn.com/"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    cnnPage = driver.page_source
    driver.quit()

    url = "https://www.foxnews.com/"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    foxPage = driver.page_source
    driver.quit()

    cnnSoup = BeautifulSoup(cnnPage, 'html.parser')
    cnnHeadline = cnnSoup.find('article', attrs={
        'class': 'cd cd--card cd--article cd--idx-0 cd--large cd--vertical cd--has-siblings cd--has-media cd--media__image cd--has-banner'})

    foxSoup = BeautifulSoup(foxPage, 'html.parser')
    foxHeadline = foxSoup.find('article', attrs={'class': 'article story-1'})

    cnnNews = cnnHeadline.text.strip()
    foxNews = foxHeadline.text.strip()

    speak("Ok. CNN says " + cnnNews)
    time.sleep(1)
    moreNews = input(speak("Do you want to hear more?"))
    if (moreNews == "yes"):
        speak("Ok. Fox News says " + foxNews)

def getFox():
        webbrowser.open("https://www.foxnews.com/")
def getCNN():
    webbrowser.open("https://www.cnn.com/")
def getMSNBC():
    webbrowser.open("https://www.msnbc.com/")








