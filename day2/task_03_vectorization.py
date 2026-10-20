import numpy as np
import timeit

# Simulated vehicle velocity readings in kilometers per hour (km/h)
rng = np.random.default_rng(42)
velocity_kmh = rng.uniform(0, 140, 1_000_000)

def loop_version():
    squared = []
    for value in velocity_kmh:
        mps = value / 3.6
        squared.append(mps ** 2)
    return squared

def vectorized_version():
    mps = velocity_kmh / 3.6
    return mps ** 2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

result = vectorized_version()

print("First five squared velocity values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")
