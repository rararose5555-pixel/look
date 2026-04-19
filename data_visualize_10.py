import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("student_data.csv")

plt.figure()
plt.plot(data['Name'], data['Marks'], marker='o')
plt.title("Marks Trend")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.scatter(data['Hours_Studied'], data['Marks'])
plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()

plt.figure()
plt.bar(data['Name'], data['Attendance'])
plt.title("Attendance of Students")
plt.xlabel("Student")
plt.ylabel("Attendance")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.barh(data['Name'], data['Math'])
plt.title("Math Marks")
plt.xlabel("Math Marks")
plt.ylabel("Student")
plt.show()

plt.figure()
plt.hist(data['Science'], bins=5, edgecolor='black')
plt.title("Science Marks Distribution")
plt.xlabel("Science Marks")
plt.ylabel("Frequency")
plt.show()

plt.figure()
subject_totals = data[["Math", "Science", "English"]].sum()
plt.pie(subject_totals, labels=subject_totals.index, autopct='%1.1f%%', startangle=90)
plt.title("Total Contribution of Each Subject")
plt.show()

plt.figure()
plt.boxplot(data["Marks"])
plt.title("Box Plot of Overall Marks")
plt.ylabel("Marks")
plt.show()

plt.figure()
plt.fill_between(range(len(data)), data['English'], alpha=0.4)
plt.plot(range(len(data)), data['English'])
plt.title("English Marks Trend")
plt.xlabel("Student Index")
plt.ylabel("English Marks")
plt.show()

plt.figure()
plt.step(data['Name'], data['Attendance'])
plt.title("Attendance Step Plot")
plt.xlabel("Student")
plt.ylabel("Attendance")
plt.xticks(rotation=45)
plt.show()

data.set_index('Name')[['Math','Science','English']].plot(
    kind='bar',
    stacked=True
)
plt.title("Subject Contribution per Student")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()