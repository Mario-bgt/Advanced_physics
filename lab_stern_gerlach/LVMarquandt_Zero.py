# Created by S. Bosma, Jan 2013 (sbosma@physik.uzh.ch)
# modified Jan 2018 by ruby@physik.uzh.ch

# Fitting script for the Stern-Gerlach data
# To determine parameter for double gaussian of zero field
# or for a single function with one data file
# shows Influence of parameter variations
# helps to find good initial parameters


from pylab import plot, show, figure, legend, title, xlabel, ylabel
from scipy.optimize import leastsq
from numpy import ones, array
import matplotlib.pyplot as plt
import os.path
from functionsSG import *
import parameters  as GPara # File contains all changing vaiables

# Read data from file "parameters.py"
dataBoundary = GPara.widthMeas # millimeters
file_location = GPara.file_location
filename = GPara.fileZeroField
ConvPrecision = GPara.ConvPrecision
param0 = GPara.Zeroparam0 # 7 Initial Parameter Zerofield (pname)

pt_mm =  666.7 # measured points per mm with 'grob' on Phywe apparatus
Nlimit = floor(ConvPrecision*pt_mm) # Rate of undersampling

x, y = load_data(file_location, filename, dataBoundary)
## Initial parameters for the double gaussian zero field fit  -> copy final parameters to FuncionSG ~ line 21 (fittedDoubleGaussianParam)
pname = ['xc1', 'w1', 'A1', 'xc2', 'w2', 'A2', 'B'] #parameter names

plsq = leastsq(zf_FuncResiduals, param0, args=(y, x), maxfev=10000, full_output=True)
paramFinal, err = plsq[0], plsq[1]
chi2  = sum(zf_FuncResiduals(paramFinal,y,x)**2)

print('Final parameters ', paramFinal)
print('Initial guess ', param0)
print('Covariance matrix ', err)
print('chi2 ', chi2)

# Fit result and initial guess
fit = zf_Func(paramFinal, x)
initialGuess = zf_Func(param0, x)

xu, yu = [],[]
xo, yo = [],[]
count = 0


for i in range(len(x)):
    xo.append(x[i])     # original data
    yo.append(y[i])
    if count == Nlimit:
        xu.append(x[i]) # undersampled data
        yu.append(y[i])
        count = 0
    else:
        count += 1

# Fill in the
#param0 = array([0.19, 5.0, 2.8, 0.04, 1.24, 1.5, 0.4])

# Double gaussian funtion, simulating the atom distribution when the applied magnetic field is 0
yzf = zf_Func(paramFinal, xu)
fig = plt.figure(num=None, figsize=(6, 7), dpi=150)
plt.plot(xo,yo, label='data',lw=3)
plt.plot(xu,yu,'ro',markersize=3, label='undersampled data')
plt.plot(xu,yzf,'g+',markersize=10, label='simulated data')
plt.plot(x, initialGuess ,'k', label='initial guess')
plt.legend()
plt.xlabel('distance in mm')
plt.ylabel('detector signal')
plt.title('zero field data')
graph_name="%s-Nullfeld.png" % (filename[:-4])
output_name = os.path.join(file_location,graph_name)
print("Saving figure to ", output_name)
pl.savefig(output_name)
plt.show()
