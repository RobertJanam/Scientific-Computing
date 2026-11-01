
# NUMERICAL OPTIMIZATION AND MONTE CARLO METHODS

## Table of Contents
- [Task 19: Numerical Optimization](#task-19-numerical-optimization)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Task 20: Random Numbers and Monte Carlo Methods](#task-20-random-numbers-and-monte-carlo-methods)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**Files:**
- `task_19_optimization.py`
- `task_20_monte_carlo.py`

---

# Task 19: Numerical Optimization

---

## Inputs

```python
# Cost per unit
Type A = 12
Type B = 18

# Capacity per unit
Type A = 100
Type B = 170

# Required total capacity
1000

# Initial allocation
x0 = [5, 3]
```

The program uses `scipy.optimize.minimize()` with the SLSQP method to minimize the total operating cost while satisfying the minimum capacity requirement.

---

## Instruction 1: Change one input and explain how the result changes

**Changed input:**

The cost per unit of Type B server is changed from 18 to 25.

```python
def cost(z):
    x, y = z
    return 12*x + 25*y
```

**Explanation of Change**

Increasing the cost of Type B servers makes them more expensive relative to Type A servers. Since Type A provides 100 capacity units at a cost of 12, while Type B provides 170 capacity units at a cost of 25, Type A becomes the more economical option per capacity unit.

The optimizer therefore changes its allocation from Type B servers to Type A servers.

---

## Instruction 2: Meaning of the output

**Previous output:**

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

**New output:**

```text
Optimization success: True
Type A allocation: 10.000
Type B allocation: 0.000
Total capacity: 1000.00
Minimum planning cost: 120.00
Best nearby integer solution: (120, 10, 0, 1000)
```

### Discussion

The original optimization allocates approximately 5.882 units of Type B because this produces the required capacity at the lowest cost. The continuous solution has a minimum planning cost of approximately 105.88.

After increasing the cost of Type B, the optimizer allocates 10 units of Type A instead. This provides exactly 1000 capacity units at a cost of 120.

The output demonstrates how numerical optimization selects the most economical allocation while satisfying a constraint. The integer search additionally identifies a solution using whole server units, since actual servers cannot normally be allocated in fractions.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

A delivery company operates two types of vehicles. Type A vehicles carry 100 packages and cost 12 units to operate per trip. Type B vehicles carry 170 packages and cost 18 units per trip.

The company wants to transport at least 1000 packages while minimizing operating costs. Vehicle allocations are non-negative.

**Input data:**

```python
from scipy.optimize import minimize

# x = number of Type A vehicle trips
# y = number of Type B vehicle trips

def delivery_cost(z):
    x, y = z
    return 12*x + 18*y

def package_constraint(z):
    x, y = z
    return 100*x + 170*y - 1000

constraints = {
    "type": "ineq",
    "fun": package_constraint
}

bounds = [(0, None), (0, None)]

solution = minimize(
    delivery_cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization success:", solution.success)
print(f"Type A vehicle trips: {x:.3f}")
print(f"Type B vehicle trips: {y:.3f}")
print(f"Packages transported: {100*x + 170*y:.2f}")
print(f"Minimum operating cost: {solution.fun:.2f}")
```

**Output data**

```text
Optimization success: True
Type A vehicle trips: 0.000
Type B vehicle trips: 5.882
Packages transported: 1000.00
Minimum operating cost: 105.88
```

**Interpretation**

The optimization model determines the combination of vehicle trips that transports at least 1000 packages at the lowest operating cost. In this case, Type B vehicles provide the required capacity at a lower cost per package, so the optimizer selects them.

---

# Task 20: Random Numbers and Monte Carlo Methods

---

## Inputs

```python
rng = np.random.default_rng(42)

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000
```

The program uses NumPy's random number generator to simulate 100,000 possible server-demand scenarios. Demand is generated using a normal distribution with a mean of 850 and a standard deviation of 120.

The overload probability is estimated by dividing the number of simulations where demand exceeds capacity by the total number of simulations.

---

## Instruction 1: Change one input and explain how the result changes

**Changed input:**

The server capacity is reduced from 1000 to 900.

```python
capacity = 900.0
```

**Explanation of Change**

Reducing server capacity means the server can handle less incoming demand before becoming overloaded. More randomly generated demand scenarios will therefore exceed the available capacity.

As a result, the estimated overload probability increases.

---

## Instruction 2: Meaning of the output

**Previous output:**

```text
Estimated overload probability: 10.6160%
Number of overload cases: 10616 out of 100000
```

**New output:**

```text
Estimated overload probability: 33.5940%
Number of overload cases: 33594 out of 100000
```

### Discussion

In the original simulation, 10,616 out of 100,000 demand scenarios exceed the server capacity of 1000. This gives an estimated overload probability of 10.6160%.

After reducing the capacity to 900, the number of overload scenarios increases to 33,594, giving an estimated probability of 33.5940%.

The graph shows the running overload probability as the number of simulations increases. As more random scenarios are generated, the estimate generally stabilizes around the underlying probability.

This demonstrates how Monte Carlo methods can be used to estimate risk when demand is uncertain.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

A researcher wants to estimate the value of π using Monte Carlo simulation. Random points are generated inside a square with coordinates between -1 and 1. Points whose distance from the origin is less than or equal to 1 lie inside the inscribed circle.

The ratio of points inside the circle to the total number of points approximates the ratio of the circle's area to the square's area. Therefore, π can be estimated using:

\[
\pi \approx 4 \times \frac{\text{Points inside circle}}{\text{Total points}}
\]

**Input data:**

```python
import numpy as np

rng = np.random.default_rng(42)

N = 100_000

# Generate random coordinates inside the square
x = rng.uniform(-1, 1, N)
y = rng.uniform(-1, 1, N)

# Check whether each point lies inside the unit circle
inside = x**2 + y**2 <= 1

# Estimate pi
pi_estimate = 4 * inside.mean()

print(f"Estimated value of pi: {pi_estimate:.6f}")
print(f"Points inside circle: {inside.sum()}")
print(f"Total points: {N}")
```

**Output data**

The program produces an estimated value of π close to 3.141593. The exact estimate depends on the random sample generated.

**Interpretation**

The simulation estimates π by comparing the number of randomly generated points inside a unit circle with the total number of points inside the surrounding square.

As the number of simulations increases, the estimated value generally approaches the actual value of π. This demonstrates how Monte Carlo methods can estimate mathematical quantities through repeated random sampling.
```
