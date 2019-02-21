import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("randomData.csv")
print(df)

ax = sns.scatterplot(x = "numGoals", y = "numGames", data = df)
ax.set_title("Iris Sepal vs. Petal Length")
plt.show()
