import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# -----------------------------
# Read CSV Files
# -----------------------------

employee = pd.read_csv("employee.csv")
student = pd.read_csv("student.csv")

# -----------------------------
# Department Wise Expense
# -----------------------------

expense = employee.groupby("Department")["Employee Salary"].sum()

# -----------------------------
# Department Wise Revenue
# -----------------------------

revenue = student.groupby("Department")["Fees"].sum()

# -----------------------------
# Employee Count
# -----------------------------

employee_count = employee.groupby("Department").size()

# -----------------------------
# Student Count
# -----------------------------

student_count = student.groupby("Department").size()

# -----------------------------
# Mentor Capacity
# -----------------------------

mentor_capacity = employee.groupby("Department")["Mentor Capacity"].sum()

# -----------------------------
# Combine Everything
# -----------------------------

report = pd.DataFrame({
    "Revenue": revenue,
    "Expense": expense,
    "Employees": employee_count,
    "Students": student_count,
    "Capacity": mentor_capacity
}).fillna(0)

# -----------------------------
# Calculations
# -----------------------------

report["Profit/Loss"] = report["Revenue"] - report["Expense"]

report["Capacity Utilization %"] = (
    report["Students"] / report["Capacity"]
) * 100

report["Students per Mentor"] = (
    report["Students"] / report["Employees"]
)

# -----------------------------
# Suggestion
# -----------------------------

suggestions = []

for util in report["Capacity Utilization %"]:

    if util >= 90:
        suggestions.append("Add More Employees")
    else:
        suggestions.append("No Requirement")

report["Suggestion"] = suggestions

# -----------------------------
# Totals
# -----------------------------

print("\n================ COLLEGE REPORT ================\n")

print("Total Employee Salary :", employee["Employee Salary"].sum())
print("Total Student Revenue :", student["Fees"].sum())

print("\nDepartment Wise Report\n")

print(report)

# -----------------------------
# GRAPH 1
# Revenue vs Expense
# -----------------------------

departments = report.index

x = np.arange(len(departments))

width = 0.35

plt.figure(figsize=(8,5))

plt.bar(
    x-width/2,
    report["Revenue"],
    width,
    label="Revenue"
)

plt.bar(
    x+width/2,
    report["Expense"],
    width,
    label="Expense"
)

plt.xticks(x, departments)

plt.title("Revenue vs Expense")

plt.xlabel("Department")

plt.ylabel("Amount")

plt.legend()

plt.grid(axis="y")

plt.show()

# -----------------------------
# GRAPH 2
# Profit/Loss
# -----------------------------

colors = []

for value in report["Profit/Loss"]:

    if value >= 0:
        colors.append("green")
    else:
        colors.append("red")

plt.figure(figsize=(8,5))

plt.bar(
    report.index,
    report["Profit/Loss"],
    color=colors
)

plt.title("Department Wise Profit / Loss")

plt.xlabel("Department")

plt.ylabel("Profit")

plt.grid(axis="y")

plt.show()

# -----------------------------
# GRAPH 3
# Capacity Utilization
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(
    report.index,
    report["Capacity Utilization %"],
    color="orange"
)

plt.axhline(
    y=100,
    color="red",
    linestyle="--",
    label="Maximum Capacity"
)

plt.title("Capacity Utilization (%)")

plt.xlabel("Department")

plt.ylabel("Utilization (%)")

plt.legend()

plt.grid(axis="y")

plt.show()
# -----------------------------
# LINEAR REGRESSION
# Profit/Loss Prediction
# -----------------------------

print("\n================ LINEAR REGRESSION ================\n")

# X = Department numbers (0,1,2,...)
X = np.arange(len(report)).reshape(-1, 1)

# y = Profit/Loss
y = report["Profit/Loss"].values

# Create and Train Model
model = LinearRegression()

model.fit(X, y)

# Predict Profit/Loss
predicted_profit = model.predict(X)

# Create Prediction Report
prediction_report = pd.DataFrame({
    "Department": report.index,
    "Actual Profit/Loss": y,
    "Predicted Profit/Loss": predicted_profit.round(2)
})

print(prediction_report)

# -----------------------------
# GRAPH 4
# Linear Regression
# -----------------------------

plt.figure(figsize=(8,5))

# Actual values
plt.scatter(
    X,
    y,
    color="blue",
    s=100,
    label="Actual Profit/Loss"
)

# Regression Line
plt.plot(
    X,
    predicted_profit,
    color="red",
    linewidth=2,
    label="Regression Line"
)

plt.xticks(
    X.flatten(),
    report.index
)

plt.xlabel("Department")

plt.ylabel("Profit/Loss")

plt.title("Linear Regression - Profit/Loss Prediction")

plt.legend()

plt.grid(True)

plt.show()

# -----------------------------
# Predict Next Department
# -----------------------------

next_department = np.array([[len(report)]])

next_profit = model.predict(next_department)

print("\nPredicted Profit/Loss for Next Department :",
      round(next_profit[0], 2))

# -----------------------------
# Model Accuracy
# -----------------------------

accuracy = model.score(X, y) * 100

print("Model Accuracy : {:.2f}%".format(accuracy))

# -----------------------------
# Suggestions
# -----------------------------

print("\n================ SUGGESTIONS ================\n")

for dept in report.index:

    print(
        dept,
        "->",
        report.loc[dept, "Suggestion"]
    )

# -----------------------------
# Final Summary
# -----------------------------

print("\n================ SUMMARY ================\n")

print("Total Revenue :", report["Revenue"].sum())

print("Total Expense :", report["Expense"].sum())

print("Overall Profit/Loss :",
      report["Profit/Loss"].sum())

print("Average Capacity Utilization : {:.2f}%".format(
    report["Capacity Utilization %"].mean()
))

print("Average Students per Mentor : {:.2f}".format(
    report["Students per Mentor"].mean()
))