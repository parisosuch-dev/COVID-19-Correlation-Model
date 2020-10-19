import pandas as pd
import matplotlib.pyplot as plt
from stats import *
df = pd.read_csv('data/data.csv')
print(df) # print the df, the entire table
#print(df.shape) # shape of table
x = df["population"]
y = df["case_rate_per_100k"]
plt.scatter(x, y, s=5, c='purple')
plt.xlabel("population")
plt.ylabel("cases per 100k")
xReg, yReg = linearRegression(x,y)
plt.plot(xReg,yReg, color='red',linewidth=1.5)
b = slope(x,y)
a = intercept(x,y)
print("\nSlope: ", b)
print("\nIntercept: ", a)
plt.show()
