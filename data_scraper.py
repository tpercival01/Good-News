from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from urllib.request import urlopen
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def twitter_animals():
    driver = webdriver.Firefox()
    twitter_animals = "https://twitter.com/search?q=%23animals&src=typed_query"
    driver.get(twitter_animals)
    


# reddit - top - day - COMPLETED
def reddit_top_day():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    reddit_top_day = "https://www.reddit.com/r/popular/top/?t=day"
    driver.get(reddit_top_day)

    # scroll to end of screen to load more content

    for i in range(20):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  
        time.sleep(1)

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "lxml")
    articles = soup.body.find_all("shreddit-post")

    # create a dict to store all the relevant data
    article_data = {}
    for idx,i in enumerate(articles):
        article_data[idx] = {}
        article_data[idx]["title"] = i.get("post-title")
        article_data[idx]["author"] = i.get("author")
        article_data[idx]["href"] = i.get("content-href")
        article_data[idx]["type"] = i.get("post-type")

    article_data_dataframe = pd.DataFrame(article_data).transpose()

    driver.quit()
    return article_data_dataframe