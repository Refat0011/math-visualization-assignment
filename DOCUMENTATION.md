# Detailed Project Documentation

# 📌 Project Title

Math Visualization Assignment

---

# 📖 Project Overview

This project is a Python-based mathematical visualization and student score analysis system developed using NumPy and Matplotlib.

The main objective of this project is to demonstrate how mathematical equations and datasets can be visualized using graphs and prediction models.

The project contains:

1. Mathematical function visualization
2. Custom equation plotting
3. Student score data analysis
4. Best-fit line prediction

---

# 🛠️ Libraries Used

## 1. NumPy

NumPy is used for:
- Mathematical calculations
- Creating arrays
- Generating x-values
- Using mathematical functions
- Linear prediction using `np.polyfit()`

Import statement:

```python
import numpy as np
```

---

## 2. Matplotlib

Matplotlib is used for:
- Plotting graphs
- Creating charts
- Adding labels and titles
- Saving figures as images

Import statement:

```python
import matplotlib.pyplot as plt
```

---

# 📂 Task 1 — Mathematical Function Visualization

## Objective

Plot multiple mathematical functions in one graph.

Functions used:

```python
y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)
```

---

# Step-by-Step Explanation

## Step 1 — Create x values

```python
x = np.linspace(-10, 10, 200)
```

### Explanation

- `np.linspace()` generates evenly spaced values.
- `-10` is the starting value.
- `10` is the ending value.
- `200` means 200 points are generated.

This creates smooth curves.

---

## Step 2 — Create equations

```python
y1 = x
```

Creates a linear equation.

```python
y2 = x**2
```

Creates a quadratic equation.

```python
y3 = np.sin(x)
```

Creates a sine wave.

```python
y4 = np.exp(-0.1 * x) * np.cos(x)
```

Creates a damped cosine wave.

---

## Step 3 — Create Figure

```python
plt.figure(figsize=(10, 6))
```

### Explanation

Creates a graph window with width 10 and height 6.

---

## Step 4 — Plot Functions

```python
plt.plot(x, y1)
```

Plots the graph.

Different line styles were used to distinguish functions.

---

## Step 5 — Add Labels and Title

```python
plt.title("Mathematical Function Visualization")
```

Adds graph title.

```python
plt.xlabel("x values")
```

Adds x-axis label.

```python
plt.ylabel("y values")
```

Adds y-axis label.

---

## Step 6 — Add Legend and Grid

```python
plt.legend()
```

Shows function names.

```python
plt.grid(True)
```

Displays grid lines.

---

## Step 7 — Save Figure

```python
plt.savefig("function_plot.png")
```

Saves graph as PNG image.

---

# 📂 Task 2 — Custom Equation Visualization

## Objective

Create and visualize a custom mathematical equation.

Equation used:

```python
y_custom = 0.03 * x2**3 - 0.4 * x2**2 + np.sin(x2) + 2
```

---

# Explanation

This equation combines:
- Cubic function
- Quadratic function
- Trigonometric function

The graph demonstrates how multiple mathematical expressions can be combined into one smooth curve.

---

# 📂 Task 3 — Student Score Visualization

## Dataset

```python
students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
```

```python
midterm = [85, 72, 90, 66, 78, 92, 60, 74, 88, 95]
```

```python
final = [80, 70, 94, 68, 75, 90, 65, 72, 84, 96]
```

---

# Total Score Formula

```python
total = 0.4 * midterm + 0.6 * final
```

### Explanation

- Midterm contributes 40%
- Final contributes 60%

---

# A. Scatter Plot

## Objective

Compare midterm and final scores visually.

### Code

```python
plt.scatter(midterm, final)
```

### Explanation

Each point represents one student.

This graph helps identify relationships between scores.

---

# B. Histogram

## Objective

Show distribution of total scores.

### Code

```python
plt.hist(total, bins=5)
```

### Explanation

Histogram groups scores into ranges.

It helps analyze score frequency and distribution.

---

# C. Bar Chart

## Objective

Compare student total scores.

### Code

```python
plt.bar(students, total)
```

### Explanation

Each bar represents one student's total score.

This graph makes comparison easier.

---

# 📂 Task 4 — Best-Fit Line Prediction

## Objective

Predict final scores from midterm scores.

---

# Step 1 — Create Prediction Line

```python
slope, intercept = np.polyfit(midterm, final, 1)
```

### Explanation

`np.polyfit()` calculates the best straight line.

Equation:

```python
final = slope × midterm + intercept
```

---

# Step 2 — Generate Predicted Values

```python
prediction_line = slope * np.array(midterm) + intercept
```

Creates predicted y-values for plotting.

---

# Step 3 — Plot Prediction Line

```python
plt.plot(midterm, prediction_line)
```

Draws the regression line.

---

# Step 4 — Prediction Examples

```python
pred1 = slope * 50 + intercept
```

Predicts final score for midterm = 50.

Similar calculations were done for:
- 75
- 100

---

# 📊 Generated Output Files

The program automatically generates:

```plaintext
function_plot.png
own_equation.png
score_scatter.png
score_histogram.png
score_bar_chart.png
score_prediction.png
```

---

# 💡 Importance of Visualization

Visualization helps:
- Understand mathematical functions
- Analyze datasets
- Compare values visually
- Identify patterns and relationships
- Predict future outcomes

Graphs make complex mathematical concepts easier to understand.

---

# 🔬 Role of NumPy

NumPy was used for:
- Array generation
- Mathematical calculations
- Trigonometric functions
- Exponential functions
- Polynomial fitting

---

# 🎨 Role of Matplotlib

Matplotlib was used for:
- Plotting graphs
- Creating charts
- Adding labels
- Adding legends
- Displaying grids
- Saving figures

---

# ⚠️ Challenges Faced

Some challenges during development:
- Understanding graph plotting
- Managing multiple figures
- Creating prediction lines
- Formatting charts correctly

These were solved using NumPy and Matplotlib functions.

---

# ✅ Conclusion

This project successfully demonstrates:
- Mathematical visualization
- Data analysis
- Prediction modeling
- Python graph plotting

The assignment improved understanding of:
- NumPy
- Matplotlib
- Graph analysis
- Data visualization techniques

---

# 👤 Author

Refat
