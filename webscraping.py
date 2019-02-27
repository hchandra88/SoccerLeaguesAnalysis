import numpy as np
import pandas as pd
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.foxsports.com/soccer/stats?competition=1&season=20180&category=STANDARD')
time.sleep(2)

table = browser.find_element_by_class_name('wisbb_standardTable').get_attribute('outerHTML')
data = pd.read_html(table)
data_df = data[0]
print(data_df)
browser.close()
data_df.to_csv('data_fram.csv')
