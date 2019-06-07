import pandas as pd
from selenium import webdriver
import time

def EPLPassing():
    browser = webdriver.Firefox()
    
    browser.get('https://www.premierleague.com/stats/top/clubs/total_pass')
    time.sleep(3)
    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('totalpass.csv')
    
    browser.get('https://www.premierleague.com/stats/top/clubs/total_through_ball')
    time.sleep(3)
    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('totalthrough.csv')
    
    browser.get('https://www.premierleague.com/stats/top/clubs/total_long_balls')
    time.sleep(3)
    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('totallong.csv')
    
    browser.get('https://www.premierleague.com/stats/top/clubs/backward_pass')
    time.sleep(3)
    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('backward_pass.csv')
    
    browser.get('https://www.premierleague.com/stats/top/clubs/total_cross')
    time.sleep(3)
    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('crosses.csv')
    
    browser.get('https://www.premierleague.com/stats/top/clubs/corner_taken')
    time.sleep(3)
    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('corners.csv')
    
    browser.close()

def get_premTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=1&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('premTopGoals.csv')
    browser.close()
    
def get_laligaTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=2&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('laligaTopGoals.csv')
    browser.close()
    
def get_bundTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=4&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('bundTopGoals.csv')
    browser.close()
    
def get_ligue1TopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=43&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('ligue1TopGoals.csv')
    browser.close()
    
def get_serieATopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=3&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('serieATopGoals.csv')
    browser.close()
    
def get_uclTopGoals():
    browser = webdriver.Firefox()
    browser.get('https://www.foxsports.com/soccer/team-stats?competition=7&season=20180&category=STANDARD')
    time.sleep(3)
    table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    data_df.to_csv('uclTopGoals.csv')
    browser.close()
    
#data collection
get_bundTopGoals()
get_premTopGoals()
get_laligaTopGoals()
get_ligue1TopGoals()
get_serieATopGoals()
get_uclTopGoals()