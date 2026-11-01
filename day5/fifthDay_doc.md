
# EIGENVALUES, EIGENVECTORS AND ROOT FINDING METHODS

## Table of Contents
- [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Root Finding: Bisection and Fixed-Point Methods](#root-finding-bisection-and-fixed-point-methods)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**File:** `task_09_eigenvalues.py`

---

# Eigenvalues and Eigenvectors

---

## Inputs

```python
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])
```

to

```python
A = np.array([
    [0., 1., 1., 1.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [1., 1., 1., 0.]
])
```

### Explanation of Change

- An additional connection is introduced between nodes A and D.
- Changing the adjacency matrix modifies the network structure and increases the connectivity of nodes A and D.
- The dominant eigenvalue increases because the network has more connections.
- The eigenvector-based importance scores change to reflect the updated network structure.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Dominant eigenvalue: 2.5615528128088285

Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192

Verification error: approximately 0.0
```

The new output shows:

```text
Dominant eigenvalue: 3.0

Eigenvector-based importance:
A: 0.2500
B: 0.2500
C: 0.2500
D: 0.2500

Verification error: approximately 0.0
```

### Discussion

- The original network gives nodes B and C higher importance scores because they have more connections than nodes A and D.
- After introducing the additional connection between A and D, all four nodes become equally connected.
- Their eigenvector-based importance scores therefore become equal at 0.2500.
- The dominant eigenvalue increases from approximately 2.5616 to 3.0, indicating increased network connectivity.
- The verification error being approximately zero confirms that the calculated eigenvector satisfies the relationship Av = λv.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Analysing the importance of five routers in a computer communication network.
- Each router represents a node, while network connections between routers represent edges.
- The network is undirected, meaning connections are treated as mutual.
- Router importance is determined by the influence of its connections to other important routers.

**Input data:**

- A 5 × 5 adjacency matrix representing connections between five routers.
- Router identifiers A, B, C, D and E.
- The adjacency matrix contains binary values representing the presence or absence of connections.

**Output data**

- The dominant eigenvalue of the network adjacency matrix.
- Eigenvector-based importance scores for each router.
- Verification error for the eigenvector equation.

**Interpretation**

- Eigenvector centrality identifies routers that are connected to other influential routers.
- A higher importance score indicates greater structural influence within the communication network.
- The dominant eigenvalue describes the dominant connectivity structure of the network.
- Network administrators can use the importance scores to identify strategically influential routers when evaluating network structure.

---

**File:** `task_10_bisection_fixed_point.py`

---

# Root Finding: Bisection and Fixed-Point Methods

---

## Inputs

```python
def heat_balance(T):
    return T - 25 - 10*np.exp(-T/20)

solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

def g(T):
    return 25 + 10*np.exp(-T/20)

T = 30.0
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
def heat_balance(T):
    return T - 25 - 10*np.exp(-T/20)
```

to

```python
def heat_balance(T):
    return T - 30 - 10*np.exp(-T/20)
```

The fixed-point function was also updated from:

```python
def g(T):
    return 25 + 10*np.exp(-T/20)
```

to

```python
def g(T):
    return 30 + 10*np.exp(-T/20)
```

### Explanation of Change

- Increasing the baseline temperature from 25°C to 30°C increases the equilibrium temperature.
- The heat-balance function changes, shifting the point where the function crosses zero.
- The bisection method identifies the new root within the specified interval.
- Fixed-point iteration also approaches the new equilibrium temperature using the updated function.
- Both methods continue to converge because the updated function satisfies the required convergence conditions within the selected interval.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Bisection equilibrium temperature: 27.525211 C
Fixed-point equilibrium temperature: 27.525211 C
Fixed-point iterations: 13
```

The new output shows:

```text
Bisection equilibrium temperature: 32.017227 C
Fixed-point equilibrium temperature: 32.017227 C
Fixed-point iterations: 12
```

### Discussion

- The equilibrium temperature increases from approximately 27.53°C to 32.02°C following the increase in the baseline temperature.
- Both bisection and fixed-point methods produce approximately the same equilibrium temperature.
- The bisection method locates the root by repeatedly reducing the interval containing the solution.
- Fixed-point iteration approaches the equilibrium temperature through successive estimates.
- The graph illustrates the equilibrium point where the heat-balance function intersects the horizontal axis.
- The vertical dashed line identifies the estimated equilibrium temperature, while the horizontal line represents zero heat imbalance.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Determining the equilibrium operating temperature of a greenhouse under a simplified heat-balance model.
- The greenhouse has a baseline temperature contribution of 22°C.
- Additional heat gain decreases exponentially as temperature increases.
- The heat-balance equation is represented by f(T) = T - 22 - 8e^(-T/25).
- Equilibrium occurs when heat gain and heat loss balance each other.

**Input data:**

- A baseline temperature contribution of 22°C.
- An additional heat contribution of 8°C.
- An exponential decay constant of 25.
- A temperature search interval of [20, 40]°C.
- An initial fixed-point estimate of 25°C.
- A convergence tolerance of 1e-10.

**Output data**

- Equilibrium greenhouse temperature calculated using the bisection method.
- Equilibrium greenhouse temperature calculated using fixed-point iteration.
- Number of iterations required by the fixed-point method.
- A graph showing the heat-balance function and its estimated root.

**Interpretation**

- The bisection method determines the greenhouse equilibrium temperature by repeatedly narrowing the interval containing the root.
- Fixed-point iteration estimates the same equilibrium temperature through successive calculations.
- Both methods produce an equilibrium temperature of approximately 24.95°C.
- The graph identifies the temperature at which the heat-balance function becomes zero, indicating that the simplified model has reached thermal equilibrium.

---
