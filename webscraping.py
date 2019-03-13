import pandas as pd
from selenium import webdriver
import time


def get_premTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=1&season=20180&category=STANDARD&pos=0&team=0&sort=3&sortOrder=0')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('premTopGoals.csv')
    browser.close()
    
def get_laligaTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=2&season=20180&category=STANDARD&pos=0&team=0&sort=3&sortOrder=0')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('laligaTopGoals.csv')
    browser.close()
    
def get_bundTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=4&season=20180&category=STANDARD&pos=0&team=0&sort=3&sortOrder=0')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('bundTopGoals.csv')
    browser.close()
    
def get_ligue1TopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=43&season=20180&category=STANDARD&pos=0&team=0&sort=3&sortOrder=0')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('ligue1TopGoals.csv')
    browser.close()
    
def get_serieATopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/stats?competition=3&season=20180&category=STANDARD&pos=0&team=0&sort=3&sortOrder=0')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('serieATopGoals.csv')
    browser.close()