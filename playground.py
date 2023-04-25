import matplotlib.pyplot as plt
import numpy as np

A = [7.32, 7.04, 5.36, 7.36, 7.36, 7.08]
B = [10.2, 8.92, 5.96, 10.72, 11.56, 12.36]
f = [160, 200, 300, 140, 120, 100]
f = f*100

phi = np.arcsin(np.divide(A, B))

print(phi)
fig = plt.figure()
plt.scatter(phi, np.log(f))
plt.xlabel('Phasenverlauf in rad')
plt.ylabel('log(f)')
plt.grid()
plt.show()

f = [50, 320]
U_aus= [2, 5]
U_in = [5, 5]
