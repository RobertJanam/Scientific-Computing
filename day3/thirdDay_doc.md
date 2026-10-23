# MATRIX ALGEBRA AND LINEAR SYSTEMS

## Table of Contents
- [Matrix Algebra](#matrix-algebra)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Linear Systems](#linear-systems)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**File:** `task_05_matrix_algebra.py`

---

# Matrix Algebra

---

## Inputs

```python
angle = np.deg2rad(45)
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])
```

---

## Instruction 1: Change one input and explain how the result changes

Changed: 
```python
angle = np.deg2rad(45)
```

to

```python
angle = np.deg2rad(90)
```

### Explanation of Change
- Rotating by 90 degrees maps spatial vectors directly onto perpendicular coordinate axes
- The transformation projects original x-coordinates entirely onto y-coordinates and original y-coordinates onto negative x-coordinates, altering point direction while preserving overall planar area scaling.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Original points: 
 [[0. 0.]
  [1. 0.]
  [1. 1.]
  [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
  [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
  [ 1.41421356 -1.06066017]
  [ 2.82842712  0.        ]
  [ 1.41421356  1.06066017]]
Determinant: 3.0
```

The new output shows:

```text
Original points: 
 [[0. 0.]
  [1. 0.]
  [1. 1.]
  [0. 1.]]
Transformation matrix:
 [[ 0.  -1.5]
  [ 2.   0. ]]
Transformed points:
 [[ 0.   0. ]
  [ 0.  -1.5]
  [ 2.  -1.5]
  [ 2.   0. ]]
Determinant: 3.0
```

### Discussion

- At 90 degrees, cosine terms evaluate to zero, removing cross-axis mixing and isolating directional scaling onto orthogonal axes.
- The determinant remains constant at , demonstrating that rotational reorientation preserves boundary area expansion regardless of angle.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Transforming Lidar sensor bounding box coordinates relative to an autonomous vehicle chassis.
- The vehicle undergoes a 30-degree heading orientation change and applies gain calibration scaling factors across sensor axes.

**Input data:**

- An array of 2D bounding corner coordinates in meters, a 30-degree rotation matrix, and an axial scaling matrix .

**Output data**

- Original bounding coordinates, transformation matrix, transformed spatial points, and area determinant factor.

**Interpretation**

- Matrix multiplication computes combined angular rotation and sensor gain scaling in a single operation, enabling real-time coordinate mapping for autonomous navigation.

---

**File:** `task_06_linear_systems.py`

---

# Linear Systems

---

## Inputs

```python
b = np.array([20.0, 72.0])
```

---

## Instruction 1: Change one input and explain how the result changes

Changed: 
```python
b = np.array([20.0, 72.0])
```

to

```python
b = np.array([28.0, 88.0])
```

### Explanation of Change
- Updating target resource consumption raises total workload demands.
- Modifying the right-hand side constant vector while holding coefficient matrix constant shifts the intersection point of the linear system.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

The new output shows:

```text
Type A servers: 5
Type B servers: 4
Verification A @ solution: [28. 88.]
Residual: [0. 0.]
Residual norm: 0.0
```

### Discussion

- Type A server allocations increased from 3 to 5 to meet increased CPU capacity requirements, while Type B servers remained at 4.
- A zero residual norm confirms exact numerical convergence without solver rounding drift.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Calculating optimal nutrient blend ratios for precision agricultural fertigation.
- Blend Alpha supplies Nitrogen and Phosphorus per kg; Blend Beta supplies $25\%$ Nitrogen and $15\%$ Phosphorus per kg.
- Field targets require Nitrogen and Phosphorus.

**Input data:**

- Nutrient contribution matrix and target nutrient requirement vector.

**Output data**

- Mass requirements for Blend Alpha and Blend Beta, matrix verification, residual vector, and residual norm.

**Interpretation**

- Solving via linear elimination determines exact chemical nutrient allocations to hit agricultural targets without manual estimation.

---
