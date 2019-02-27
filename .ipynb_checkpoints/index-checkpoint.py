import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")
sns.set_palette("Dark2")

df = pd.read_csv("randomData.csv")
print(df)

ax = sns.scatterplot(x = "numGoals", y = "numGames", data = df)
ax.set_title("Number of Games vs. Goals Scored")
plt.show()
