import numpy as np
data = np.array([2, 3, 4, 7, 9, 11])
min = min(data)
max = max(data)
mean = np.mean(data)
sd = np.std(data)

norm_data = [0]

#Min-max normalization
def min_max(data, min, max, norm_data):
    
    for element in data:
        value = (element - min) / (max - min)
        norm_data.append(value)
    return norm_data
a = min_max(data, min, max, norm_data)
print(f"Min-Max normalized data: {a}")

#z - score normalisation
z = [0]
def z_score(data, mean, sd, z):
    for element in data:
        value = (element - mean) / sd
        z.append(value)
    return z
b = z_score(data, mean, sd, z)
print(f"z-score normalized data: {b}")