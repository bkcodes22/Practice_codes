import numpy as np
data = input("Enter the data points you need to check:  ")
data = data.split()
data = [float(x) for x in data]
data = np.array(data)
#data = np.array([2,4,4,4,5,4,4,4,6,6])
n = len(data)
mean = np.mean(data)
sd = np.std(data)
sd_input = float(input('How many standard deviations you need to check ?: '))

#this function calculates chebyshev bound (1-1/k^2 * 100)
def calc_chebyshev(k):
    bound_max = (1 - 1/k**2) * 100
    return bound_max

max_bound = calc_chebyshev(sd_input)
print(f"Maximum allowed bound is {max_bound} %")

#this function calculates the intrevals
def calc_intrevals(x, k, s):
    x_minus_ks = x - (k * s)
    x_plus_ks = x + (k * s)
    return x_minus_ks, x_plus_ks

intrevals = calc_intrevals(mean, sd_input, sd)
intrevals = np.asarray(intrevals)

cnt = 0

for element in data:
    if element > intrevals[0] and element < intrevals[1]:
        cnt += 1
    else:
        pass

percent = cnt/n * 100
print(f"Observed bound in the data is {percent} %")

if percent >= max_bound:
    print("Data follows chebyshev's inequality!")
else:
    print("Data doesn't follow chebyshev's inequality")