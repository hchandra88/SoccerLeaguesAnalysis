import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os

url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
python_button.click()










'''
sns.set(style="darkgrid")
sns.set_palette("Dark2")

df = pd.read_csv("randomData.csv")
print(df)

ax = sns.scatterplot(x = "numGoals", y = "numGames", data = df)
ax.set_title("Number of Games vs. Goals Scored")
'''
