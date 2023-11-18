import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# load data
data = np.loadtxt('data.txt')
marks = []
for i in range(len(data)):
    marks.append(data[i][1])

nicht_best_mark = [3.5 for i in range(10)]
# sort the marks
marks += nicht_best_mark
marks.sort()


def linear(x, a, b):
    return a*x + b


fit = curve_fit(linear, np.arange(len(marks)), marks)
# plot data
plt.plot(marks, 'ro', label='data')
plt.plot(linear(np.arange(len(marks)), fit[0][0], fit[0][1]), 'b-', label='fit')
plt.grid(True)
plt.title('marks of solid state physics')
plt.ylabel('marks')
plt.xlabel('students')
plt.legend()
plt.show()

# print fit
print('a: ', fit[0][0])
print('b: ', fit[0][1])
print(f'fit: {fit[0][0]}*x + {fit[0][1]}')

# calculate mean and median
print('mean: ', np.mean(marks))
print('median: ', marks[int(len(marks)/2)])

# calculate standard deviation
print('standard deviation: ', np.std(marks))

# calculate variance
print('variance: ', np.var(marks))
