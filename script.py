import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

file = "Processed Data.xlsx"
data = pd.read_excel(file)

column1 = data.iloc[:, 0]
column2 = data.iloc[:, 1]

plt.plot(column1, column2)
plt.xlabel("Column 1")
plt.ylabel("Column 2")
plt.title("Plot of Column 1 vs Column 2")

plt.show()