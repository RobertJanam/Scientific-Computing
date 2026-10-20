# VECTORIZATION AND NUMERICAL ERRORS

## Table of Contents
- [Vectorization](#vectorization)
    - [Inputs](#inputs)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
    - [Instruction 2](#instruction-2-meaning-of-the-output)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)
- [Numerical Errors](#numerical-errors)
    - [Inputs](#inputs-1)
    - [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes-1)
    - [Instruction 2](#instruction-2-meaning-of-the-output-1)
    - [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case-1)

---

**File:** `task_03_vectorization.py`

---

# Vectorization

---

## Inputs

```python
    rng.uniform(0, 140, 1_000_000)
```

---

## Instruction 1: Change one input and explain how the result changes

Changed: 
```python
    rng = np.random.default_rng(42)
```

to

```python
    rng = np.random.default_rng()
```

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
    [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
```

Running the code again:

```text
    [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
```

The new output shows:

```text
    [0.001227   0.00465638 0.01090225 0.05878204 0.00200415]
```

Running the code again:

```text
    [0.00115537 0.00368316 0.00342734 0.03495641 0.03455516]
```

### Discussion

- By removing the seed `(42)` to `()`, the output now displayed random values every different runtime. 
- Previously, the seed ensured the same sequence of numbers will be picked every runtime.
- However, when it was removed, the output generated different sequence of numbers every time.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Tracking high-frequency velocity data over 1,000,000 readings for an autonomous vehicle braking test.
- Speeds below 30 km/h are ideal for residential zones. Speeds over 120 km/h trigger an emergency safety override.

**Input data:**

- An array of 1,000,000 vehicle velocity readings measured in kilometers per hour (km/h).

**Output data**

- The first five squared velocity values converted to meters per second, alongside a benchmarking comparison of loop vs. vectorized conversion speeds.

**Interpretation**

- The vectorized processing method converted 1,000,000 velocity metrics in a fraction of a millisecond, providing a massive speedup over standard Python loops required for real-time safety critical updates.

---

**File:** `task_04_numerical_errors.py`

---

# Numerical Errors

---

## Inputs

```python
    [1e-4, 1e-8, 1e-12]
```

---

## Instruction 1: Change one input and explain how the result changes

Changed: 
```python
    [1e-4, 1e-8, 1e-12]
```

to

```python
    [1e-4, 1e-8, 1e-12, 1e-16]
```

### Explanation of Change
- Adding `1e-16` introduces a value that matches the limit of standard 64-bit floating-point precision (which can hold roughly 15–17 significant decimal digits). 
- This forces the un-stabilized `direct` formula to fail completely due to rounding limits, exposing severe code instability that wasn't fully visible at `1e-12`.

---

## Instruction 2: Meaning of the output

The previous output showed:

```text
    x=1e-04: direct=0.499987500624, stable=0.499987500625
    x=1e-08: direct=0.499999996961, stable=0.499999998750
    x=1e-12: direct=0.500044450291, stable=0.500000000000
```

The new output shows:

```text
    x=1e-04: direct=0.4999875006239662, stable=0.4999875006249609
    x=1e-08: direct=0.4999999969612645, stable=0.4999999987500000
    x=1e-12: direct=0.5000444502911705, stable=0.4999999999998750
    x=1e-16: direct=0.0000000000000000, stable=0.5000000000000000
```

### Discussion

- **Binary Rounding:** Binary storage truncates fractions, creating minor errors (e.g., `0.1+0.2 != 0.3`). Fix this by using `np.isclose()`.
- **Absolute vs. Relative:** Absolute error finds raw distance (\(\vert\text{True}-\text{Approx}\vert\)); relative error scales it to reveal percentage significance.
- **Catastrophic Cancellation:** At `x=1e-16`, subtracting almost identical floating-point numbers in the numerator of the `direct` formula drops the structural precision to zero. Rewriting the algebraic expression into an addition-based, stable fractional form completely eliminates this subtraction step, preserving accurate outputs down to `1e-16`.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Tracking high-precision orbital calculations over extreme distances for an aerospace trajectory model.
- Positional discrepancies under 1 millimeter are acceptable. Distances computed with structural subtractions risk severe truncation errors near cosmic horizons.

**Input data:**

- Floating-point representations of physical orbital intervals and close-range gravitational field perturbations.

**Output data**

- Tolerance-based equality validations, true versus approximate trajectory error metrics, and an evaluation comparing unstable subtraction vs. stable division behaviors at microscopic scales.

**Interpretation**

- Standard algebraic formulations broke down completely at deep decimal positions due to arithmetic constraints, whereas the transformed stable algorithm preserved micro-level spatial precision over extreme scales.

---
