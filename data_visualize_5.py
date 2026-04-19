import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("student_data.csv")
print(data.head())
plt.scatter(data['Hours_Studied'], data['Marks'])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied vs Marks")
plt.show()

plt.plot(data['Marks'])
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.title("Marks Trend")
plt.show()

plt.bar(data['Hours_Studied'], data['Marks'])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours vs Marks (Bar Chart)")
plt.show()

corr = data.corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.show()