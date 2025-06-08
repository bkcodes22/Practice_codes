#this code calculates varince of the given data by mnaual method and np.var built in  function
import numpy as np
data = input("Enter the numbers (separted by space): ")
data = data.split()
data = [float(x) for x in data]
data_array = np.array(data)
averge_square = np.mean(data_array) ** 2
n = len(data_array)
nx_2 = averge_square * n
sum = np.array([])

for element in data_array:
    i_2 = element ** 2
    sum = np.append(sum, i_2)

total = np.sum(sum)
variance = (total - nx_2) / (n-1)
print(f"Variance of the data by manual method is: {variance}")

#direct method 
variance_direct = np.var(data_array, ddof=1)
print(f"Variance of the data by direct method is: {variance_direct}")
    

    

