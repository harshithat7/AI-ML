import numpy as np
readings = np.arange(24)
print("Original shape:", readings.shape)
reshaped = readings.reshape(4, 3, 2)
print("Reshaped (4, 3, 2):", reshaped.shape)
final = reshaped.transpose(0, 2, 1)
print("Final shape:", final.shape)
print(final)