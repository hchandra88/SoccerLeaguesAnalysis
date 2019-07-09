import pandas as pd
from selenium import webdriver
import time

def get_premTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=1&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('TopGoals/premTopGoals.csv')
    browser.close()
    
def get_laligaTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=2&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('TopGoals/laligaTopGoals.csv')
    browser.close()
    
def get_bundTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=4&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('TopGoals/bundTopGoals.csv')
    browser.close()
    
def get_ligue1TopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=43&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('TopGoals/ligue1TopGoals.csv')
    browser.close()
    
def get_serieATopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=3&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('TopGoals/serieATopGoals.csv')
    browser.close()
    
def get_uclTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.uefa.com/uefachampionsleague/season=2019/statistics/round=2000980/clubs/kind=goals/index.html')
    time.sleep(3)
    table = browser.find_element_by_id('dbClubStats').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('TopGoals/uclTopGoals.csv')
    browser.close()
 
'''
def get_uclAttempts():
    browser = webdriver.Firefox()
    browser.get('https://www.uefa.com/uefachampionsleague/season=2019/statistics/round=2000980/clubs/kind=attempts/index.html')
    time.sleep(3)
    table = browser.find_element_by_id('dbClubStats').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('uclAttempts.csv')
    browser.close()
'''
    
#data collection
get_premTopGoals()
get_bundTopGoals()
get_laligaTopGoals()
get_ligue1TopGoals()
get_serieATopGoals()
get_uclTopGoals()
#get_uclAttempts()