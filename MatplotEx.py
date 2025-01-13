import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# sns.distplot([0, 1, 2, 3, 4, 5])
#
# plt.show()

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
#
# plt.plot(xpoints, ypoints)
# plt.show()


df = pd.read_csv('dataframeex.csv')
print(df)
print(df.to_string())