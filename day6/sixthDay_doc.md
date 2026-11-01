
# NEWTON-RAPHSON, SECANT METHODS AND NONLINEAR EQUATION SOLVING

## Table of Contents
- [Newton-Raphson and Secant Methods](#newton-raphson-and-secant-methods)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Polynomial and Nonlinear Equation Solving](#polynomial-and-nonlinear-equation-solving)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**File:** `task_11_newton_secant.py`

---

# Newton-Raphson and Secant Methods

---

## Inputs

```python
cash_flows = [-10000, 3000, 3500, 4000, 2500]

def npv(rate):
    return sum(
        cf / (1 + rate)**t
        for t, cf in enumerate(cash_flows)
    )

def d_npv(rate):
    return sum(
        -t * cf / (1 + rate)**(t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
cash_flows = [-10000, 3000, 3500, 4000, 2500]
```

to

```python
cash_flows = [-10000, 3000, 3500, 4500, 2500]
```

### Explanation of Change

- Increasing the third-year cash inflow from 4000 to 4500 increases the total expected investment returns.
- This changes the Net Present Value (NPV) function and consequently shifts the Internal Rate of Return (IRR).
- Both Newton-Raphson and Secant methods calculate a higher IRR because the investment generates an additional cash inflow.
- The methods continue to locate the root by iteratively finding the rate at which the NPV becomes zero.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution:   approximately 0.000000
```

The new output shows:

```text
IRR using Newton-Raphson: 13.229999%
IRR using Secant method: 13.229999%
NPV at Newton solution:   approximately 0.000000
```

### Discussion

- The IRR increases from approximately 11.54% to 13.23% after increasing the third-year cash inflow.
- Both methods produce nearly identical IRR values, demonstrating that they converge towards the same root.
- Newton-Raphson uses the derivative of the NPV function to calculate successive estimates.
- The Secant method estimates the derivative using two previous approximations, eliminating the need to explicitly provide a derivative.
- An NPV close to zero confirms that the calculated IRR satisfies the investment's break-even condition.
- Newton-Raphson requires fewer iterations in this example because it uses derivative information to improve its estimates.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Evaluating the financial viability of installing a solar energy system for a business.
- The initial installation investment is $15,000.
- The business expects annual cash inflows of $4,000, $4,500, $5,000 and $4,500 over four years.
- The objective is to determine the Internal Rate of Return at which the investment's Net Present Value becomes zero.
- The investment is evaluated without additional financing costs or taxes.

**Input data:**

- Initial investment of -$15,000.
- Annual cash inflows of $4,000, $4,500, $5,000 and $4,500.
- Initial Newton-Raphson estimate of 10%.
- Initial Secant estimates of 5% and 20%.
- Convergence tolerance of `1e-12`.

**Output data**

- Internal Rate of Return calculated using Newton-Raphson.
- Internal Rate of Return calculated using the Secant method.
- Net Present Value at the calculated rates.

**Interpretation**

- Newton-Raphson and Secant methods determine the investment's Internal Rate of Return by finding the discount rate that makes the Net Present Value equal to zero.
- Both methods produce an IRR of approximately 7.53%, indicating the estimated annual return of the solar installation investment under the stated assumptions.
- A near-zero NPV confirms that the calculated rate satisfies the investment's break-even condition.
- The two methods provide alternative numerical approaches to solving the same financial equation.

---

**File:** `task_12_nonlinear_equations.py`

---

# Polynomial and Nonlinear Equation Solving

---

## Inputs

```python
def equations(z):
    x, y = z

    return [
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ]

for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
return [
    x**2 + y**2 - 4,
    y - (x**2 - 1)
]
```

to

```python
return [
    x**2 + y**2 - 9,
    y - (x**2 - 1)
]
```

### Explanation of Change

- The circle equation changes from a radius of 2 to a radius of 3.
- Increasing the circle's radius expands its boundary while the parabola remains unchanged.
- This changes the intersection coordinates because the two curves now meet at different positions.
- The nonlinear solver calculates the new intersection points using the supplied initial guesses.
- The system continues to have two intersection points within the selected solution region.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: approximately [0.0, 0.0]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991 1.30277564]
Residuals: approximately [0.0, 0.0]
Converged: True
```

The new output shows:

```text
Initial guess: [1.0, 1.0]
Intersection: [1.83637723 2.37228132]
Residuals: approximately [0.0, 0.0]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.83637723 2.37228132]
Residuals: approximately [0.0, 0.0]
Converged: True
```

### Discussion

- The positive x-coordinate increases from approximately 1.52 to 1.84, while the corresponding y-coordinate increases from approximately 1.30 to 2.37.
- The negative x-coordinate changes from approximately -1.52 to -1.84, producing a symmetrical intersection on the opposite side of the y-axis.
- The solver identifies two intersection points because the circle and parabola cross at two locations.
- Both solutions report `True` for convergence, confirming that the numerical solver successfully located the intersection points.
- Residuals approximately equal to zero confirm that the calculated coordinates satisfy both nonlinear equations.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Determining the intersection between a circular safety boundary and a parabolic movement path for a warehouse robot.
- The circular boundary represents the maximum operating distance of a robot from its reference point.
- The robot's movement path is represented by the parabola y = x² - 1.
- The safety boundary has a radius of 3 metres.
- The objective is to determine the coordinates where the robot's movement path intersects the circular boundary.

**Input data:**

- A circular boundary equation represented by x² + y² = 9.
- A parabolic movement equation represented by y = x² - 1.
- Two initial guesses: `[1.0, 1.0]` and `[-1.0, 1.0]`.
- A nonlinear equation solver using `scipy.optimize.root`.

**Output data**

- Two intersection coordinates between the circular safety boundary and the parabolic movement path.
- Residual values for both nonlinear equations.
- Convergence status for each calculated intersection.

**Interpretation**

- The nonlinear solver determines the coordinates where the robot's parabolic movement path intersects its circular operating boundary.
- The two intersection points are approximately (1.836, 2.372) and (-1.836, 2.372).
- Near-zero residuals confirm that the calculated coordinates satisfy both equations.
- These intersection points can help identify where a robot's movement path reaches the limits of its defined operating region.

---
