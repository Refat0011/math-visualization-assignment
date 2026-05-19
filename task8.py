import numpy as np
import matplotlib.pyplot as plt

# Task 1: Mathematical Function Visualization

# Create x values
x = np.linspace(-10, 10, 200)

# Create functions
y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

# Create figure
plt.figure(figsize=(10, 6))

# Plot functions
plt.plot(x, y1, label='y = x', linestyle='-')
plt.plot(x, y2, label='y = x^2', linestyle='--')
plt.plot(x, y3, label='y = sin(x)', linestyle=':')
plt.plot(x, y4, label='y = e^(-0.1x) * cos(x)', linestyle='-.')

# Add title and labels
plt.title('Mathematical Function Visualization')
plt.xlabel('x values')
plt.ylabel('y values')

# Add legend and grid
plt.legend()
plt.grid(True)

# Save image
plt.savefig('function_plot.png')

# Show plot
plt.show()


# Task 2: Your Own Equation

# Create x values
x2 = np.linspace(-10, 10, 300)

# Custom equation
# This equation combines cubic and sine functions
y_custom = 0.03 * x2**3 - 0.4 * x2**2 + np.sin(x2) + 2

# Create figure
plt.figure(figsize=(10, 6))

# Plot custom equation
plt.plot(x2, y_custom, color='purple', linewidth=2)

# Add title and labels
plt.title('Custom Mathematical Equation')
plt.xlabel('x values')
plt.ylabel('y values')

# Add grid
plt.grid(True)

# Save image
plt.savefig('own_equation.png')

# Show plot
plt.show()

# Task 3: Student Score Data Visualization

# Student data
students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]

midterm = [85, 72, 90, 66, 78, 92, 60, 74, 88, 95]

final = [80, 70, 94, 68, 75, 90, 65, 72, 84, 96]

# Calculate total scores
total = []

for i in range(len(midterm)):
    score = 0.4 * midterm[i] + 0.6 * final[i]
    total.append(score)

# A. Scatter Plot
plt.figure(figsize=(8, 6))

plt.scatter(midterm, final)

plt.title("Midterm vs Final Scores")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")

plt.grid(True)

plt.savefig("score_scatter.png")

plt.show()


# B. Histogram
plt.figure(figsize=(8, 6))

plt.hist(total, bins=5)

plt.title("Distribution of Total Scores")
plt.xlabel("Total Scores")
plt.ylabel("Frequency")

plt.grid(True)

plt.savefig("score_histogram.png")

plt.show()


# C. Bar Chart
plt.figure(figsize=(10, 6))

plt.bar(students, total)

plt.title("Student Total Scores")
plt.xlabel("Students")
plt.ylabel("Total Score")

plt.grid(True)

plt.savefig("score_bar_chart.png")

plt.show()


# Task 4: Best-Fit Line / Simple Prediction

# Create best-fit line
slope, intercept = np.polyfit(midterm, final, 1)

# Predicted values
prediction_line = slope * np.array(midterm) + intercept

# Create figure
plt.figure(figsize=(8, 6))

# Original data points
plt.scatter(midterm, final, label='Original Data')

# Best-fit line
plt.plot(midterm, prediction_line, color='red', label='Best-Fit Line')

# Title and labels
plt.title("Best-Fit Prediction Line")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")

# Legend and grid
plt.legend()
plt.grid(True)

# Save image
plt.savefig("score_prediction.png")

# Show plot
plt.show()

# Prediction examples
pred1 = slope * 50 + intercept
pred2 = slope * 75 + intercept
pred3 = slope * 100 + intercept

print("Predicted final score for midterm 50:", pred1)
print("Predicted final score for midterm 75:", pred2)
print("Predicted final score for midterm 100:", pred3)