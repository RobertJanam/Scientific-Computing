
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# RC charging circuit:
# dV/dt = (Vs - V)/(R*C)
Vs = 5.0          # supply voltage (V)
R = 1000.0        # resistance (ohms)
C = 0.001         # capacitance (farads)
V0 = 0.0          # initial capacitor voltage

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

print(f"Final capacitor voltage: {solution.y[0][-1]:.4f} V")
print(f"Supply voltage: {Vs:.2f} V")
print(f"Time constant: {R*C:.2f} seconds")
print(f"Solver successful: {solution.success}")

plt.plot(solution.t, solution.y[0], label="Capacitor voltage")
plt.axhline(Vs, linestyle="--", label="Supply voltage")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.title("RC circuit charging response")
plt.legend()
plt.grid(True)
plt.show()
