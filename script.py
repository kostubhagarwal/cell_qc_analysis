import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

file = "Processed Data.xlsx"
data = pd.read_excel(file)

column1 = data.iloc[:, 0]
column2 = data.iloc[:, 1]
column3 = data.iloc[:, 2]

plt.scatter(column1, column3)
plt.xlabel("index")
plt.ylabel("IR")
plt.title("IR distribution")

plt.show()

plt.scatter(column1, column2)
plt.xlabel("index")
plt.ylabel("OCV")
plt.title("OCV distribution")

plt.show()