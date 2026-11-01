
# GAUSSIAN ELIMINATION AND ITERATIVE METHODS FOR LINEAR SYSTEMS

## Table of Contents
- [Gaussian Elimination and LU Decomposition](#gaussian-elimination-and-lu-decomposition)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Iterative Methods for Linear Systems](#iterative-methods-for-linear-systems)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**File:** `task_07_gaussian_lu.py`

---

# Gaussian Elimination and LU Decomposition

---

## Inputs

```python
A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])

measurement_sets = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
measurement_sets[0] = np.array([15.0, 10.0, 10.0])
```

to

```python
measurement_sets[0] = np.array([18.0, 10.0, 10.0])
```

### Explanation of Change

- Increasing the first measurement from 15 to 18 changes the right-hand side vector while keeping the coefficient matrix constant.
- This changes the solution values because the system must satisfy a higher first measurement requirement.
- LU decomposition reuses the same factorized coefficient matrix to calculate the updated solution without repeating the factorization.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: approximately 0.0

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

The new output shows:

```text
Measurement set 1
Solution: [5.80487805 5.21951220 5.07317073]
Residual norm: 0.0
```

### Discussion

- The first solution changed from approximately [5, 5, 5] to [5.805, 5.220, 5.073] after increasing the first measurement.
- The remaining measurement sets retain their original solutions because their input vectors were not changed.
- The residual norm remains approximately zero, confirming that the calculated solution satisfies the linear system.
- The direct solution and LU solution produce equivalent results for the same input vector.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Modelling structural responses at three connected points of a bridge under different loading conditions.
- The coefficient matrix represents the simplified stiffness relationships between the three structural points.
- Different measurement vectors represent different applied load conditions.
- The structural coefficient matrix remains constant while the applied loads change.

**Input data:**

- A 3 × 3 structural stiffness matrix and multiple load vectors representing different loading conditions.
- The load vectors are [15, 10, 10], [16, 11, 9] and [14, 12, 11].

**Output data**

- Calculated displacement values at the three structural points for each load condition.
- Residual norms to verify the accuracy of the calculated solutions.
- A direct solution for comparison with the LU decomposition result.

**Interpretation**

- LU decomposition separates the structural coefficient matrix into lower and upper triangular matrices.
- The factorized matrices can be reused to calculate structural responses under different loading conditions.
- This reduces repeated computational work when analysing a structure with an unchanged stiffness matrix.

---

**File:** `task_08_iterative_linear.py`

---

# Iterative Methods for Linear Systems

---

## Inputs

```python
A = np.array([
    [ 2., -1., 0., 0., 0.],
    [-1.,  2., -1., 0., 0.],
    [ 0., -1.,  2., -1., 0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

b = np.array([100., 0., 0., 0., 20.])
```

---

## Instruction 1: Change one input and explain how the result changes

Changed:

```python
b = np.array([100., 0., 0., 0., 20.])
```

to

```python
b = np.array([80., 0., 0., 0., 30.])
```

### Explanation of Change

- The left boundary temperature decreases from 100°C to 80°C, while the right boundary temperature increases from 20°C to 30°C.
- Changing the boundary influence vector changes the temperature distribution across the five interior grid points.
- Both Jacobi and Gauss-Seidel methods calculate new temperature estimates until the difference between successive iterations falls below the specified tolerance.
- The convergence process remains valid because the coefficient matrix is unchanged and remains diagonally dominant.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Jacobi temperatures: [86.66666665 73.33333331 59.99999997 46.66666664 33.33333332]

Gauss-Seidel temperatures: [86.66666665 73.33333330 59.99999997 46.66666665 33.33333332]

Direct solution: [86.66666667 73.33333333 60. 46.66666667 33.33333333]
```

The new output shows:

```text
Jacobi temperatures: [71.66666665 63.33333331 54.99999997 46.66666664 38.33333332]

Gauss-Seidel temperatures: [71.66666665 63.33333330 54.99999997 46.66666665 38.33333332]

Direct solution: [71.66666667 63.33333333 55. 46.66666667 38.33333333]
```

### Discussion

- The temperature at the first interior grid point decreases from approximately 86.67°C to 71.67°C because the left boundary temperature decreases.
- The temperature at the last interior grid point increases from approximately 33.33°C to 38.33°C because the right boundary temperature increases.
- Both iterative methods produce results that closely match the direct solution obtained using `np.linalg.solve()`.
- Jacobi converges in approximately 150 iterations, while Gauss-Seidel converges in approximately 75 iterations for the specified tolerance.
- The graph demonstrates convergence by showing how the maximum change between successive estimates decreases as the number of iterations increases.
- Gauss-Seidel converges faster because it immediately uses updated values within the same iteration, while Jacobi uses values from the previous iteration.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Modelling the steady-state concentration of a pollutant across five connected water-treatment compartments.
- Each compartment exchanges pollutant concentration with its neighbouring compartments.
- The left boundary has a concentration of 80 units, while the right boundary has a concentration of 30 units.
- The coefficient matrix represents the simplified exchange relationships between neighbouring compartments.
- The system is assumed to have reached steady state, meaning concentration values no longer change with time.

**Input data:**

- A 5 × 5 coefficient matrix representing the relationships between neighbouring compartments.
- A boundary influence vector `[80, 0, 0, 0, 30]`.
- An initial concentration estimate of zero for all five interior compartments.
- A convergence tolerance of `1e-8` and a maximum of 500 iterations.

**Output data**

- Estimated pollutant concentrations in the five interior compartments using the Jacobi method.
- Estimated pollutant concentrations using the Gauss-Seidel method.
- A direct solution for comparison.
- Convergence graphs showing the maximum change between successive estimates for both methods.

**Interpretation**

- The iterative methods estimate pollutant concentrations across connected compartments until the system approaches a steady-state solution.
- Jacobi and Gauss-Seidel provide numerical approximations that can be compared with the direct solution.
- The convergence graph helps evaluate how quickly each method approaches the final concentration distribution.
- Gauss-Seidel generally requires fewer iterations than Jacobi for this system because it uses newly calculated values immediately during each iteration.

---
