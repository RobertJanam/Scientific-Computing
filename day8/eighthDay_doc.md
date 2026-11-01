
# NUMERICAL DIFFERENTIATION AND NUMERICAL INTEGRATION

## Table of Contents
- [Numerical Differentiation](#numerical-differentiation)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Numerical Integration](#numerical-integration)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**File:** `task_15_numerical_differentiation.py`

---

# Numerical Differentiation

---

## Inputs

```python
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)

position = np.array([
    0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0
])
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
position = np.array([
    0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0
])
```

to

```python
position = np.array([
    0.0, 4.8, 10.2, 18.1, 22.7, 30.0, 38.0
])
```

### Explanation of Change

- The recorded GPS position at 3 seconds increases from 16.1 metres to 18.1 metres.
- Changing this measurement affects the estimated speeds at the neighbouring time points because numerical differentiation uses differences between nearby position measurements.
- The central difference method recalculates the estimated speeds using the updated position value.
- The forward and backward difference calculations remain unchanged because the first and last position measurements were not modified.
- The resulting speed estimates reflect the change in the recorded GPS position.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
t=0s, position=0.0m, estimated speed=4.80m/s
t=1s, position=4.8m, estimated speed=5.10m/s
t=2s, position=10.2m, estimated speed=5.65m/s
t=3s, position=16.1m, estimated speed=6.25m/s
t=4s, position=22.7m, estimated speed=6.95m/s
t=5s, position=30.0m, estimated speed=7.65m/s
t=6s, position=38.0m, estimated speed=8.00m/s
```

The new output shows:

```text
t=0s, position=0.0m, estimated speed=4.80m/s
t=1s, position=4.8m, estimated speed=5.10m/s
t=2s, position=10.2m, estimated speed=6.65m/s
t=3s, position=18.1m, estimated speed=6.25m/s
t=4s, position=22.7m, estimated speed=5.95m/s
t=5s, position=30.0m, estimated speed=7.65m/s
t=6s, position=38.0m, estimated speed=8.00m/s
```

### Discussion

- The estimated speed at 2 seconds increases from 5.65 m/s to 6.65 m/s because the modified position measurement affects the central difference calculation at that point.
- The estimated speed at 4 seconds decreases from 6.95 m/s to 5.95 m/s because the same modified measurement affects the neighbouring central difference calculation.
- The speed estimates at the beginning and end remain unchanged because their calculations use position measurements that were not modified.
- Forward difference estimates the rate of change at the beginning using the next measurement.
- Central difference estimates the rate of change at interior points using measurements before and after each point.
- Backward difference estimates the rate of change at the final point using the preceding measurement.
- The graph displays how the estimated vehicle speed changes over time based on the recorded GPS positions.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Monitoring water consumption in a commercial building using a digital water meter.
- The meter records cumulative water volume at regular time intervals.
- The objective is to estimate the instantaneous water consumption rate at each recorded time.
- Forward, central and backward difference methods are used to estimate the rate of change of cumulative water volume.
- Water consumption is measured in litres, while time is measured in seconds.

**Input data:**

- Time measurements in seconds.
- Cumulative water volume measurements in litres.
- Forward difference for the first measurement.
- Central difference for interior measurements.
- Backward difference for the final measurement.

**Output data**

- Estimated water consumption rate at each recorded time in litres per second.
- A graph showing how the estimated water consumption rate changes over time.

**Interpretation**

- Numerical differentiation estimates the rate at which water consumption changes over time.
- Higher estimated values indicate periods of greater water usage.
- Lower estimated values indicate periods of reduced water usage.
- The resulting measurements can help building administrators monitor water consumption patterns and identify periods of unusually high usage.

---

**File:** `task_16_numerical_integration.py`

---

# Numerical Integration

---

## Inputs

```python
time_hours = np.array([
    0, 2, 4, 6, 8, 10, 12
], dtype=float)

power_kw = np.array([
    0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9
])

energy_trapezoid = np.trapezoid(
    power_kw, time_hours
)

energy_simpson = simpson(
    power_kw, x=time_hours
)
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
power_kw = np.array([
    0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9
])
```

to

```python
power_kw = np.array([
    0.8, 1.0, 1.4, 2.2, 1.6, 1.2, 0.9
])
```

### Explanation of Change

- The recorded power consumption at 6 hours increases from 1.8 kW to 2.2 kW.
- Increasing this measurement raises the estimated total electrical energy consumption because the power-versus-time curve has a higher value at that interval.
- The trapezoidal rule recalculates the accumulated energy using trapezoids formed between neighbouring measurements.
- Simpson's rule recalculates the energy using parabolic approximations across the measurement intervals.
- Both methods produce higher energy estimates because the modified power reading increases the area under the power-versus-time curve.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule:   15.800 kWh
Difference between estimates: 0.100 kWh
```

The new output shows:

```text
Energy using trapezoidal rule: 16.500 kWh
Energy using Simpson's rule:   16.867 kWh
Difference between estimates: 0.367 kWh
```

### Discussion

- The trapezoidal energy estimate increases from 15.700 kWh to 16.500 kWh because the power measurement at 6 hours increases.
- Simpson's energy estimate increases from 15.800 kWh to approximately 16.867 kWh because the updated measurement changes the parabolic approximation.
- Both methods estimate the accumulated electrical energy consumed over the 12-hour observation period.
- The trapezoidal rule approximates the area under the power curve using straight-line segments between neighbouring measurements.
- Simpson's rule approximates the area using parabolic segments and is often more accurate for smooth functions.
- The difference between the two estimates increases from 0.100 kWh to approximately 0.367 kWh, showing that the numerical approximation method affects the estimated accumulated energy.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Estimating the total distance travelled by a delivery vehicle using recorded speed measurements.
- The vehicle's speed is recorded every two hours during a journey.
- The objective is to calculate the total distance travelled over the observation period.
- The trapezoidal rule and Simpson's rule are used to approximate the accumulated distance from the speed-versus-time measurements.
- Speed is measured in kilometres per hour, while time is measured in hours.

**Input data:**

- Time measurements in hours.
- Corresponding vehicle speed measurements in kilometres per hour.
- Trapezoidal integration using `np.trapezoid()`.
- Simpson's integration using `scipy.integrate.simpson()`.

**Output data**

- Estimated total distance travelled using the trapezoidal rule.
- Estimated total distance travelled using Simpson's rule.
- Difference between the two distance estimates.

**Interpretation**

- Numerical integration calculates the accumulated distance travelled by integrating vehicle speed over time.
- The trapezoidal rule approximates the distance using trapezoidal areas between consecutive speed measurements.
- Simpson's rule uses parabolic approximations to estimate the accumulated distance.
- The difference between the two estimates demonstrates how numerical integration methods can produce slightly different approximations of the same accumulated quantity.
- The calculated distance can help delivery operators estimate journey distances when continuous speed measurements are unavailable.

---
