import numpy as np

# Lidar sensor scan field-of-view bounding box coordinates [x, y] in meters
scan_bounds = np.array([
    [0.0, 0.0],
    [2.0, 0.0],
    [2.0, 4.0],
    [0.0, 4.0]
])

# Chassis orientation change: 30-degree heading rotation
heading_angle = np.deg2rad(30)
rotation_matrix = np.array([
    [np.cos(heading_angle), -np.sin(heading_angle)],
    [np.sin(heading_angle),  np.cos(heading_angle)]
])

# Sensor calibration gain scaling (range calibration factors)
scale_matrix = np.array([
    [1.2, 0.0],
    [0.0, 0.8]
])

# Combined coordinate transformation
transformation = rotation_matrix @ scale_matrix
transformed_bounds = scan_bounds @ transformation.T

print("Original Lidar bounds:\n", scan_bounds)
print("Transformation matrix:\n", transformation)
print("Transformed Lidar bounds:\n", transformed_bounds)
print("Determinant (Area Scaling Factor):", np.linalg.det(transformation))