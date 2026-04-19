import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("student_data.csv")
print("Dataset:")
print(data)

X = data[['Hours_Studied']]
y = data['Marks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nEvaluation Metrics:")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.show()

new_data = np.array([[6]])
prediction = model.predict(new_data)

print("\nPredicted Marks for 6 hours study:", prediction[0])