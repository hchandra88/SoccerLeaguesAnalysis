import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import webscraping

sns.set(style="darkgrid")
sns.set_palette("Dark2")

'''
webscraping.get_goal_stats()
webscraping.get_assist_stats()
webscraping.get_shot_stats()
webscraping.get_shotOnGoal_stats()
webscraping.get_post_stats()
webscraping.get_passes_stats()
webscraping.get_offsides_stats()
webscraping.get_crosses_stats()
webscraping.get_yellow_stats()
webscraping.get_red_stats()
webscraping.get_touch_stats()
webscraping.get_block_stats()
webscraping.get_int_stats()
webscraping.get_tackle_stats()
webscraping.get_clear_stats()
webscraping.get_error_stats()
webscraping.get_pen_stats()
webscraping.get_foul_stats()
webscraping.get_cleanSheet_stats()
webscraping.get_goalsAgainst_stats()
webscraping.get_saves_stats()
webscraping.get_punches_stats()
webscraping.get_highClaims_stats()
webscraping.get_ownGoals_stats()
'''

attack_df = pd.read_csv("goal_data.csv")
attack_df = pd.read_csv("assist_data.csv")
attack_df.to_csv('attack_data.csv')

'''
df = pd.read_csv("data_fram.csv")
print(df)

ax = sns.scatterplot(x = "GP", y = "GS", data = df)
ax.set_title("Number of Goals Scored vs. Games Played")
plt.show()
'''
