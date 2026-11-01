
# ORDINARY DIFFERENTIAL EQUATIONS AND NUMERICAL SOLUTION OF ODES USING SCIPY

## Table of Contents
- [Ordinary Differential Equations – Euler Method](#ordinary-differential-equations--euler-method)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Numerical Solution of ODEs Using SciPy](#numerical-solution-of-odes-using-scipy)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**File:** `task_17_euler_ode.py`

---

# Ordinary Differential Equations – Euler Method

---

## Inputs

```python
T_ambient = 25.0
T_initial = 90.0
k = 0.12
h = 1.0
end_time = 30.0
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
k = 0.12
```

to

```python
k = 0.18
```

### Explanation of Change

- The cooling constant increases from 0.12 to 0.18, indicating a faster rate of heat loss.
- Increasing the cooling constant makes the temperature difference between the object and its surroundings decrease more rapidly.
- Euler's method calculates lower temperature values at corresponding time intervals because the object cools faster.
- The exact mathematical solution also produces a lower final temperature.
- The numerical difference between the Euler approximation and the exact solution changes because the cooling rate has increased while the time step remains constant.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Euler temperature after 30 min: 26.40 C
Exact temperature after 30 min: 26.78 C
Final absolute error: 0.3720 C
```

The new output shows:

```text
Euler temperature after 30 min: 25.17 C
Exact temperature after 30 min: 25.29 C
Final absolute error: 0.1248 C
```

### Discussion

- The Euler estimated temperature decreases from approximately 26.40°C to 25.17°C because the cooling constant increases.
- The exact temperature also decreases from approximately 26.78°C to 25.29°C, confirming that the object approaches the ambient temperature more quickly.
- Euler's method estimates the temperature by repeatedly applying the update equation T(n+1) = T(n) + h f(t(n), T(n)).
- The exact solution provides a reference for evaluating the accuracy of the numerical approximation.
- The absolute error decreases from approximately 0.3720°C to 0.1248°C in this particular comparison.
- The graph compares the Euler approximation with the exact solution, illustrating how closely the numerical method follows the actual cooling behaviour.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Predicting the growth of a bacterial population in a controlled laboratory environment.
- The initial bacterial population is 500 organisms.
- The population grows at a proportional rate of 0.15 per hour.
- The population growth is represented by the differential equation dP/dt = rP.
- Euler's method is used to estimate population changes over time.
- The growth rate remains constant throughout the observation period.

**Input data:**

- Initial population of 500 organisms.
- Growth rate of 0.15 per hour.
- Time step of 1 hour.
- Observation period of 24 hours.
- Population growth function represented by dP/dt = 0.15P.

**Output data**

- Estimated bacterial population at each hourly interval.
- Final estimated population after 24 hours.
- Exact population calculated using the exponential growth equation.
- Absolute error between the numerical estimate and the exact solution.
- A graph comparing the Euler approximation and exact population growth.

**Interpretation**

- Euler's method estimates bacterial population changes by repeatedly applying the population growth equation.
- The population increases over time because the growth rate is positive.
- The exact exponential growth solution provides a reference for evaluating the accuracy of Euler's method.
- The graph illustrates the difference between the numerical approximation and the exact population growth curve.
- The results can help researchers estimate population development over a specified observation period.

---

**File:** `task_18_scipy_ode.py`

---

# Numerical Solution of ODEs Using SciPy

---

## Inputs

```python
Vs = 5.0
R = 1000.0
C = 0.001
V0 = 0.0

def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]

t_eval = np.linspace(0, 5, 200)

solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    method="RK45"
)
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
R = 1000.0
```

to

```python
R = 1500.0
```

### Explanation of Change

- The circuit resistance increases from 1000 ohms to 1500 ohms while the capacitance remains constant.
- Increasing resistance increases the RC time constant, calculated as the product of resistance and capacitance.
- A larger time constant means that the capacitor charges more slowly.
- The `solve_ivp()` function recalculates the voltage values using the updated differential equation.
- Consequently, the capacitor reaches a lower voltage within the same five-second observation period.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Final capacitor voltage: 4.9657 V
Supply voltage: 5.00 V
Time constant: 1.00 seconds
Solver successful: True
```

The new output shows:

```text
Final capacitor voltage: 4.8213 V
Supply voltage: 5.00 V
Time constant: 1.50 seconds
Solver successful: True
```

### Discussion

- The final capacitor voltage decreases from approximately 4.9657 V to 4.8213 V because the increased resistance slows down the charging process.
- The time constant increases from 1.00 second to 1.50 seconds, indicating that the circuit responds more slowly.
- The supply voltage remains constant at 5.00 V because it was not modified.
- The `solve_ivp()` function numerically solves the differential equation using the specified time interval and initial voltage.
- The solver's successful status confirms that the numerical integration completed successfully.
- The graph illustrates how the capacitor voltage increases over time towards the supply voltage.
- The horizontal dashed line represents the maximum voltage the capacitor approaches during charging.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Modelling the cooling of industrial equipment using Newton's law of cooling.
- The equipment initially operates at 100°C.
- The surrounding temperature is 25°C.
- The cooling constant is 0.08 per minute.
- The cooling process is represented by the differential equation dT/dt = -k(T - T_ambient).
- SciPy's `solve_ivp()` is used to numerically estimate the equipment temperature over time.
- The temperature is evaluated over a period of 30 minutes.

**Input data:**

- Initial equipment temperature of 100°C.
- Ambient temperature of 25°C.
- Cooling constant of 0.08 per minute.
- Initial time of 0 minutes.
- Final time of 30 minutes.
- Temperature differential equation represented by Newton's law of cooling.
- Evaluation points generated using `np.linspace()`.

**Output data**

- Estimated equipment temperature at the requested time points.
- Final equipment temperature after 30 minutes.
- Numerical solver success status.
- A graph showing the equipment's temperature reduction over time.

**Interpretation**

- `solve_ivp()` numerically solves the cooling differential equation without manually implementing each integration step.
- The equipment temperature decreases over time as heat is transferred to the surrounding environment.
- The temperature gradually approaches the ambient temperature of 25°C.
- The numerical results demonstrate how differential equation solvers can model physical systems that change continuously over time.
- The graph provides a visual representation of the equipment's cooling behaviour and can help estimate how long equipment requires to reach a desired operating temperature.

---
