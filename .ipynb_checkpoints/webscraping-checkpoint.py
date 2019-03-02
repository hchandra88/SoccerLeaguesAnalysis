import numpy as np
import pandas as pd
from selenium import webdriver
import time

def get_goal_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/goals')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('goal_data.csv')
    browser.close()

def get_assist_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/goal_assist')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('assist_data.csv')
    browser.close()
    
def get_shot_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/total_scoring_att')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('shots_data.csv')
    browser.close()
    
def get_shotOnGoal_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/ontarget_scoring_att')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('shotsOnGoal_data.csv')
    browser.close()
    
def get_post_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/hit_woodwork')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('post_data.csv')
    browser.close()

def get_passes_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/total_pass')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('pass_data.csv')
    browser.close()
    
def get_offsides_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/total_offside')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('offsides_data.csv')
    browser.close()
    
def get_crosses_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/total_cross')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('crosses_data.csv')
    browser.close()
    
def get_yellow_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/yellow_card')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('yellow_data.csv')
    browser.close()
    
def get_red_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/red_card')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('red_data.csv')
    browser.close()
    
def get_touch_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/touches')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('touch_data.csv')
    browser.close()
    
def get_block_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/outfielder_block')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('block_data.csv')
    browser.close()
    
def get_int_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/interception')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('int_data.csv')
    browser.close()

def get_tackle_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/total_tackle')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('tackle_data.csv')
    browser.close()
    
def get_clear_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/total_clearance')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('clear_data.csv')
    browser.close()
    
def get_error_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/error_lead_to_goal')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('error_data.csv')
    browser.close()

def get_pen_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/penalty_conceded')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('pen_data.csv')
    browser.close()
    
def get_foul_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/fouls')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('foul_data.csv')
    browser.close()

def get_cleanSheet_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/clean_sheet?po=GOALKEEPER')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('cleanSheet_data.csv')
    browser.close()
    
def get_goalsAgainst_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/goals_conceded?po=GOALKEEPER')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('goalsAgainst_data.csv')
    browser.close()
    
def get_saves_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/saves?po=GOALKEEPER')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('saves_data.csv')
    browser.close()
    
def get_punches_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/punches?po=GOALKEEPER')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('punches_data.csv')
    browser.close()

def get_highClaims_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/total_high_claim?po=GOALKEEPER')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('highClaims_data.csv')
    browser.close()
    
def get_ownGoals_stats():
    browser = webdriver.Firefox()
    browser.get('https://www.premierleague.com/stats/top/players/own_goals')
    time.sleep(10)

    table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
    data = pd.read_html(table)
    data_df = data[0]
    print(data_df)
    data_df.to_csv('ownGoals_data.csv')
    browser.close()