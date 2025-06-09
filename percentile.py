#this code calculates the value in your array according to percentile value you provide
import numpy as np
import re
data = input("Enter the numbers (separted by space): ")
data = data.split()
data = [float(x) for x in data]
data = np.array(data)
#data = np.array([2, 6, 4, 10, 8, 14, 12, 18, 16, 20])
#data will be sorted using nump sort
data = np.sort(data)
percentile_value = float(input("Enter the percentile value: ")) #percentile value
p_100 = percentile_value / 100 #p value
n = len(data)

np_1 = n * p_100
np_2 = str(np_1)
np_3 = n * (1- p_100)

def check_last_two_chars(text, np_1, n):
    if re.search(r"\.0$", text):
        temp = int(np_1)
        arg2 =  n - temp
        return temp, arg2

    else:
        add_up = round(0.5 + np_1)
        arg2 = round(0.5 + np_3)
        return add_up, arg2
    
check1 = check_last_two_chars(np_2, np_1, n)


def find_indices(arr, check1):
    n = len(arr)
    valid_indices = []
    
    required_before = check1[0]  # including current
    required_after = check1[1]   # including current

    for i in range(n):
        if i >= required_before - 1 and i + required_after - 1 < n:
            valid_indices.append(arr[i])
    
    return valid_indices

res = find_indices(data, check1)
res = np.mean(res)
print(res)



    



 




