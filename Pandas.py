import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

city = pd.read_csv("https://raw.githubusercontent.com/kwagner4821/Pandas/main/bea-2006(1).csv")

print(city)
y = city["pcgmp"]
x = np.log(city["pop"])

plt.scatter(x, y)
plt.show()