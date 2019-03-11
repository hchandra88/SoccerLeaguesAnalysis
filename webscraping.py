import numpy as np
import pandas as pd
from selenium import webdriver
import time

def get_premStandard_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=1&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('premStandard_data.csv')
    browser.close()
    
def get_premForward_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=1&season=20180&category=STANDARD&pos=Forward&team=0&isOpp=0&sort=3&sortOrder=0')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('premForward_data.csv')
    browser.close()
    
def get_premMidfield_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=1&season=20180&category=STANDARD&pos=Midfielder&team=0&isOpp=0&sort=3&sortOrder=0')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('premMidfield_data.csv')
    browser.close()
    
def get_premDefense_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=1&season=20180&category=STANDARD&pos=Defender&team=0&isOpp=0&sort=3&sortOrder=0')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('premDefense_data.csv')
    browser.close()