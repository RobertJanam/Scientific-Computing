import numpy as np

# Linear System for Precision Fertigation Blend Allocation
# x = kg of Blend Alpha, y = kg of Blend Beta
# Blend Alpha provides 0.10 kg N/kg and 0.20 kg P/kg
# Blend Beta provides 0.25 kg N/kg and 0.15 kg P/kg
# Target requirement: 50 kg Nitrogen, 70 kg Phosphorus

A = np.array([
    [0.10, 0.25],
    [0.20, 0.15]
])
b = np.array([50.0, 70.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Blend Alpha required: {solution[0]:.2f} kg")
print(f"Blend Beta required: {solution[1]:.2f} kg")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))