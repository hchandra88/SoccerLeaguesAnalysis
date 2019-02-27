import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")
sns.set_palette("Dark2")

df = pd.read_csv("data_fram.csv")
print(df)

ax = sns.scatterplot(x = "GP", y = "GS", data = df)
ax.set_title("Number of Goals Scored vs. Games Played")
plt.show()
