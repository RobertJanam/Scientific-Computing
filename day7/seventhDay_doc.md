# INTERPOLATION AND CURVE FITTING AND APPROXIMATION

## Table of Contents
- [Interpolation](#interpolation)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Curve Fitting and Approximation](#curve-fitting-and-approximation)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**File:** `task_13_interpolation.py`

---

# Interpolation

---

## Inputs

```python
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)

temperature = np.array([
    18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0
])

linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

target_time = 10.5
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
temperature = np.array([
    18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0
])
```

to

```python
temperature = np.array([
    18.0, 20.0, 24.5, 24.0, 25.0, 25.5, 25.0
])
```

### Explanation of Change

- The temperature reading at 10:00 increases from 22.5°C to 24.5°C.
- Changing this measurement affects the estimated temperatures between 10:00 and 11:00.
- Linear interpolation produces estimates based on straight-line segments between neighbouring measurements.
- Cubic spline interpolation adjusts its smooth polynomial curves to accommodate the modified measurement.
- Consequently, both interpolation methods produce different temperature estimates at 10:30.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Linear estimate at 10:30: 23.25 C
Cubic estimate at 10:30: 23.36 C
```

The new output shows:

```text
Linear estimate at 10:30: 24.25 C
Cubic estimate at 10:30: 24.52 C
```

### Discussion

- The linear estimate increases from 23.25°C to 24.25°C because the 10:00 measurement was increased by 2°C.
- The cubic spline estimate increases from approximately 23.36°C to 24.52°C because the spline curve adjusts to the modified measurement.
- Linear interpolation connects neighbouring measurements using straight lines, while cubic spline interpolation uses smooth cubic polynomial segments.
- The graph displays the original hourly measurements alongside the estimated temperature values at ten-minute intervals.
- The scatter points represent actual measurements, while the two curves represent the estimated temperatures using the different interpolation methods.
- Both methods estimate values between known measurements, but their results may differ because of their mathematical approaches.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Estimating soil moisture levels between scheduled measurements in a precision agriculture system.
- A soil moisture sensor records moisture percentages at hourly intervals.
- The agricultural monitoring system requires estimated moisture readings every ten minutes.
- Linear interpolation and cubic spline interpolation are used to estimate the missing intermediate measurements.
- The recorded measurements are assumed to represent continuous changes in soil moisture between observation times.

**Input data:**

- Hourly soil moisture measurements and their corresponding observation times.
- Linear interpolation using `interp1d()`.
- Cubic spline interpolation using `CubicSpline()`.
- Ten-minute intervals for generating intermediate estimates.
- A selected observation time for comparing the two interpolation methods.

**Output data**

- Estimated soil moisture percentages using linear interpolation.
- Estimated soil moisture percentages using cubic spline interpolation.
- A graph comparing the original measurements and the interpolated curves.

**Interpretation**

- Interpolation estimates soil moisture values at times when the sensor does not record measurements.
- Linear interpolation provides estimates using straight-line relationships between neighbouring observations.
- Cubic spline interpolation produces smooth curves between the recorded measurements.
- The estimated values can help an agricultural monitoring system track soil moisture changes more frequently without requiring continuous sensor readings.
- The graph provides a visual comparison of the measured and estimated soil moisture values.

---

**File:** `task_14_curve_fitting.py`

---

# Curve Fitting and Approximation

---

## Inputs

```python
users = np.array(
    [50, 100, 150, 200, 250, 300, 350],
    dtype=float
)

response_ms = np.array(
    [82, 95, 115, 145, 185, 238, 305],
    dtype=float
)

def model(x, a, b, c):
    return a*x**2 + b*x + c

parameters, covariance = curve_fit(
    model, users, response_ms
)
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
response_ms = np.array(
    [82, 95, 115, 145, 185, 238, 305],
    dtype=float
)
```

to

```python
response_ms = np.array(
    [82, 95, 115, 165, 185, 238, 305],
    dtype=float
)
```

### Explanation of Change

- The measured server response time at 200 concurrent users increases from 145 ms to 165 ms.
- Changing this measurement affects the quadratic curve fitted to the collected server performance data.
- The `curve_fit()` function recalculates the model parameters to minimize the sum of squared residuals between measured and predicted response times.
- The fitted coefficients, Root Mean Square Error (RMSE), and predicted response time at 400 users consequently change.
- The updated curve reflects the modified server performance measurements.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Fitted model: y = 0.002167x^2 + -0.1345x + 85.00
RMSE: 1.55 ms
Predicted response at 400 users: 377.86 ms
```

The new output shows:

```text
Fitted model: y = 0.001786x^2 + 0.0179x + 76.43
RMSE: 6.47 ms
Predicted response at 400 users: 369.29 ms
```

### Discussion

- The fitted quadratic model changes because the measured response time at 200 users increases by 20 ms.
- The RMSE increases from approximately 1.55 ms to 6.47 ms, indicating that the updated model has larger prediction errors across the measured observations.
- The predicted response time at 400 concurrent users decreases from approximately 377.86 ms to 369.29 ms because the fitted model recalculates all its coefficients to accommodate the updated measurements.
- A lower RMSE indicates that the fitted model follows the observed measurements more closely.
- The scatter points represent the actual server response-time measurements, while the fitted curve represents the estimated quadratic relationship.
- The graph extends to 400 concurrent users, allowing the fitted model to estimate response time beyond the measured data range.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Estimating electricity consumption costs in a commercial building based on the number of operating electrical appliances.
- The number of operating appliances represents the independent variable.
- The corresponding electricity consumption represents the dependent variable.
- Electricity consumption is assumed to increase nonlinearly as more appliances operate simultaneously.
- A quadratic mathematical model is used to approximate the relationship between the number of appliances and electricity consumption.

**Input data:**

- Recorded numbers of operating electrical appliances at different observation periods.
- Corresponding electricity consumption measurements in kilowatt-hours (kWh).
- A quadratic model represented by y = ax² + bx + c.
- The `curve_fit()` function for estimating the model parameters.
- A set of appliance counts for plotting the fitted curve and estimating consumption.

**Output data**

- Estimated quadratic model coefficients.
- Predicted electricity consumption values.
- Root Mean Square Error (RMSE) for evaluating the model's fitting accuracy.
- A graph comparing the observed electricity consumption measurements with the fitted quadratic curve.

**Interpretation**

- Curve fitting establishes a mathematical relationship between the number of operating appliances and electricity consumption.
- The quadratic model captures nonlinear changes in electricity consumption as appliance usage increases.
- RMSE measures how closely the fitted model follows the recorded electricity consumption measurements.
- The fitted model can help building administrators estimate electricity consumption at different appliance usage levels.
- The graph provides a visual comparison between actual consumption measurements and the estimated mathematical relationship.

---
