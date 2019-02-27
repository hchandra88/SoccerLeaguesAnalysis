import numpy as np
import pandas as pd
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.premierleague.com/stats/top/players/goals?se=210')
time.sleep(2)

table = browser.find_element_by_class_name('table.statsTable').get_attribute('outerHTML')
data = pd.read_html(table)
data_df = data[0]
print(data_df)
browser.close()
data_df.to_csv('data_fram.csv')
