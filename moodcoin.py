import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
#import spacy
import random
#from spacytextblob.spacytextblob import SpacyTextBlob
from nrclex import NRCLex
import pandas as pd
from datetime import datetime


#I made a "coin" that's pegged to the mood of a social media platform.  It detects trust across all posts, incentivizing good behavior.  
You can do #any emotion, short it with anger etc.

moodcoin=10.00      #moodcoin starts at 10.

browser = webdriver.Firefox()
#Get 100 "skeets"
browser.get("https://firesky.tv/")
x=1
time.sleep(3)
skeets=[]
xworked=[]
while x<200:
    try:
        try:
        #path="/html/body/main/a[{}]/div[1]/span[2]".format(x)
            skeet = browser.find_element(By.XPATH, "/html/body/main/a[{}]".format(x))
            
        except:
            x=x+20
            if x>198:
                x=2
            continue
        skeets.append(skeet.text)
        xworked.append(x)
        x=x+1
        skeemotion=NRCLex(skeet.text)
        trust=round(float(skeemotion.top_emotions[3][1]),5)
        moodcoin=round(moodcoin+(moodcoin*trust), 2)
        moodper=round((trust)*100, 2)
        if moodper<0:
            sign="is down"
        else:
            sign="is up"
        print("Trust={}\nMoodcoin {} {}%: ${}\n".format(trust,sign,moodper,moodcoin))
#Do English only for now, but add openai later (or something free).
        
    except:
        #print("Fuck!!")
        x=x+1
        
