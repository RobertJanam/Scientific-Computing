import numpy as np

# 1. Floating-point comparison for orbit intervals
calculated_orbit = 0.15 + 0.15
expected_orbit = 0.30

print("0.15 + 0.15 =", calculated_orbit)
print("Exact comparison:", calculated_orbit == expected_orbit)
print("Tolerance-based comparison:", np.isclose(calculated_orbit, expected_orbit))

# 2. Absolute and relative error in rocket trajectory approximations
true_distance = np.sqrt(3)
approx_distance = 1.732

absolute_error = abs(true_distance - approx_distance)
relative_error = absolute_error / abs(true_distance)

print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

# 3. Numerically unstable vs stable formulation for field perturbations
for x in [1e-5, 1e-10, 1e-15, 1e-20]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.16f}, stable={stable:.16f}")
