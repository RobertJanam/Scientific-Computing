# FOUNDATIONS AND NUMPY FUNDAMENTALS

## Table of Contents

- [Instruction 1](#instruction-1-change-one-input-and-explain-how-the-result-changes)
- [Instruction 2](#instruction-2-meaning-of-the-output)
- [Instruction 3](#instruction-3-modify-the-program-to-solve-a-different-but-related-real-world-case)

---
**File:** `task_02_numpy_arrays.py`

## Instruction 1: Change one input and explain how the result changes

Changed: 
```python

    temperatures_f[:6] 

```

to

```python

    temperatures_f[:10]

```

---

## Instruction 2: Meaning of the output

The previous output showed:

```text

    [65.3  64.4  64.04 63.5  64.22 66.2 ]

```

The new output shows:

```text

    [65.3  64.4  64.04 63.5  64.22 66.2  70.7  74.84 78.08 80.78]

```

### Discussion

- By replacing the limit from `[:6]` to `[:10]`, the output now displayed a sequential total of 10 values; 4 of which weren't appearing before.

---

## Instruction 3: Modify the program to solve a different but related real-world case

**Assumptions:**

- Tracking hourly average wind speeds over 24 hours at a wind turbine site.
- Winds above 25 km/h are optimal for energy. Speeds over 90 km/h require safety shutdown.

**Input data:**

- An array of 24 hourly wind speed readings measured in meters per second (m/s).

**Output data**

- The daily average, lowest, and highest wind speeds in m/s, alongside the first 10 values converted to kilometers per hour (km/h).

**Interpretation**

- The maximum wind speed reached 14.20 m/s (51.12 km/h), meaning the turbine operated consistently within safe limits throughout the day without requiring a shutdown.

---