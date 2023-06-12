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
import matplotlib.pyplot as pl
import os.path
from functionsSG import *

import parameters  as GPara # File contains all changing vaiables

# Read data from file "parameters.py"
slope = GPara.slope
cut = GPara.cut
dataBoundary = GPara.widthFit # millimeters


# Load data
file_location = GPara.file_location
filename = GPara.LVMMFilename
param0 = GPara.LVMMParam0
doAllPlots = GPara.doAllPlots
testChi2 = GPara.testChi2


x, y = load_data(file_location, filename, dataBoundary)
## Initial parameters for the non zero-field data fits
pname = ['A','C','q','D'] #parameters names

# Launch fit with the residuals function
plsq = leastsq(RealFuncResiduals, param0, args=(y, x), maxfev=10000, full_output=True)
paramFinal, err = plsq[0], plsq[1]
chi2  = sum(RealFuncResiduals(paramFinal,y,x)**2)

print('Final parameters ', paramFinal)
print('Initial guess ', param0)
print('Covariance matrix ', err)
print('chi2 ', chi2)

# Fit result and initial guess
fit = RealFunc(paramFinal, x)
initialGuess = RealFunc(param0, x)

# Plot results
figure(num=None, figsize=(8, 6), dpi=150)
plot(x, y, 'bo', label='data')
plot(x, fit,'r', label='fit')
plot(x, initialGuess ,'g', label='initial guess')
legend()
graph_name="LVMM-%s mA-RealFunc_fit.png"  % (filename[:-4])
output_name = os.path.join(file_location,graph_name)
print("Saving figure to ", output_name)
pl.savefig(output_name)


# Influence of parameter variation on chi2 (change the residual function as needed at *):
if testChi2:

    nbrOfPoints = 10
    multiplier = [0.1, 0.005, 0.01, 0.1]
    for index in range(0,4):
        test = ones((2*nbrOfPoints,4))
        param = paramFinal.copy()
        for i in range(-nbrOfPoints,nbrOfPoints):
            param[index] = paramFinal[index] + i*multiplier[index]
            test[i+nbrOfPoints] = param.copy()
        errors = []
        for param in test:
            errors.append(sum(RealFuncResiduals(param,y,x)**2)) # *
        figure(num=None, figsize=(8, 6), dpi=150)
        plot(test[:,index],errors)
        ylabel('chi2' )
        xlabel('parameter '+pname[index]+', center value: '+str(format(round(paramFinal[index],4))))
        fstr = pname[index] + "-"+(filename[:-4])
        graph_name="LVMM-%smA-RealFunc_chi2.png" % fstr
        output_name = os.path.join(file_location,graph_name)
        print("Saving figure to ", output_name)
        pl.savefig(output_name)

# Variation of fitting curve vor parameters variations
if doAllPlots:
    shift = [0.05, 0.08, 0.01, 0.001] # multiplier for shifting
    figure(num=None, figsize=(8, 6), dpi=150)
    param = paramFinal.copy() #copy into param, paramFinal is an array
    plot(x, y, 'bo')
    for i in range(-10,10):
        param[0] = paramFinal[0] + i*shift[0]
        plot(x, RealFunc(param, x))
        title('A (amplitude) variating in RealFunc')
    #save graph
    graph_name="%s-RealFunc_Amplitude.png" % (filename[:-4])
    output_name = os.path.join(file_location,graph_name)
    print("Saving figure to ", output_name)
    pl.savefig(output_name)

    figure(num=None, figsize=(8, 6), dpi=150)
    param = paramFinal.copy()
    plot(x, y, 'bo')
    for i in range(-10,10):
        param[1] = paramFinal[1] + i*shift[1]
        plot(x, RealFunc(param, x))
        title('C (Center) variating in RealFunc')
        #save graph
    graph_name="%s-RealFunc_Center.png" % (filename[:-4])
    output_name = os.path.join(file_location,graph_name)
    print("Saving figure to ", output_name)
    pl.savefig(output_name)

    figure(num=None, figsize=(8, 6), dpi=150)
    param = paramFinal.copy()
    plot(x, y, 'bo')
    for i in range(-10,10):
        param[2] = paramFinal[2] + i*shift[2]
        plot(x, RealFunc(param, x))
        title('q variating in RealFunc')
    #save graph
    graph_name="%s-RealFunc_q_variating.png" % (filename[:-4])
    output_name = os.path.join(file_location,graph_name)
    print("Saving figure to ", output_name)
    pl.savefig(output_name)

    figure(num=None, figsize=(8, 6), dpi=150)
    param = paramFinal.copy()
    plot(x, y, 'bo')
    for i in range(-10,10):
        param[3] = paramFinal[3] + i*shift[3]
        plot(x, RealFunc(param, x))
        title('D (vertical shift) variating in RealFunc')
        #save graph
    graph_name="%s-RealFunc_Background.png" % (filename[:-4])
    output_name = os.path.join(file_location,graph_name)
    print("Saving figure to ", output_name)
    pl.savefig(output_name)


show()
