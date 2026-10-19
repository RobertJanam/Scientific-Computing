import numpy as np

# 24 hourly wind speed readings in meters per second (m/s)

wind_speeds_ms = np.array([
    4.5, 5.0, 5.2, 6.1, 5.8, 7.0,
    8.5, 9.8, 11.2, 12.5, 13.8, 14.2,
    14.0, 13.5, 12.1, 10.5, 9.2, 8.0,
    7.4, 6.5, 5.8, 5.0, 4.8, 4.2
])

mean_wind = np.mean(wind_speeds_ms)
min_wind = np.min(wind_speeds_ms)
max_wind = np.max(wind_speeds_ms)

# Vectorized conversion: m/s to km/h

wind_speeds_kmh = wind_speeds_ms * 3.6

# Output
print(f"Daily mean wind speed: {mean_wind:.2f} m/s")
print(f"Minimum wind speed: {min_wind:.2f} m/s")
print(f"Maximum wind speed: {max_wind:.2f} m/s")
print("First ten kmh readings:", np.round(wind_speeds_kmh[:10], 1))