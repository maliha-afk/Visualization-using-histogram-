import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import seaborn as sb


missingva=["N/a","na",np.nan]
pda=pd.read_csv("Penguins Data (1).csv",na_values=missingva)
pdf=pd.DataFrame(pda)

#print(pdf.isnull().sum())
pdfex=pdf.interpolate()
pdfimp=pdfex.fillna(0)
#print(pdfimp.isnull().sum())

plt.figure(figsize=(10,8))
sb.histplot(x="Culmen Length (mm)",y="Culmen Depth (mm)",data=pdfimp, color="blue")
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Culmen Depth (mm)")
plt.title("histogram of penguins's Culmen Length & Depth (mm) ")
plt.show()

plt.figure(figsize=(10,8))
sb.histplot(x="Flipper Length (mm)",y="Body Mass (g)",data=pdfimp, color="red")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.title("histogram of penguins's Flipper Length (mm) & Body Mass (g) ")
plt.show()

