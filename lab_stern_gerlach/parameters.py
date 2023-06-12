# This file contains most of the variables/parameters which have to be adjusted


#**************************************************************
#                 Adaptation necessary !!!
#
# put your own locations here  !!!   for windows:  \ -> \\
file_location = 'C:\\Users\\Institut\\Desktop\\Praktikum_Jan_2019\\LaNoMa\\'
#
# put your filenames here. Must be a list, even for single file (ex. filenames = ['320.txt'])
filenames = [ 'T118.5_B400.txt', 'T118,3_B510.txt']
# your referenz mesurement without magnetic field ("zerofield")
fileZeroField = 'T119,3_B0.txt'
#
#**************************************************************


# width of measurement (-widthMeas to +widthMeas in mm)
widthMeas = 7.0

# width  of fit (-widthFit to +widthFit in mm)
widthFit = 7

# if  True: removes slope in background in defined fit range
slope = False

# if True: cuts background, data below smallest y-value
cut = False

# determindes undersampling rate used in "funconsSG" and "LVMarqunadt_Zero" (default 0.1)
# undersamplingRate = ConvPrecision*pt_mm (pt_mm = measured points per mm with 'grob' on Phywe apparatus)
ConvPrecision = 0.1

# Two different Methodes to use zerofield (used in "funconsSG"):
# FitApp = 1: Faster RealFunc and EvenMoreRealFunc by loading zero field data once using fitted approximation,
# build a new, smaller (undersampled) x-axis and use fitted Double-Gaussian for the zerofield
# FitApp = 2: using the direct data (default)
FitApp = 2

# Fit-functions: 'NotSoIdealFunc', 'IdealFunc', 'RealFunc'(usually good), 'EvenMoreRealFunc'(good but extremely slow)
function = 'RealFunc'

# Start parameters [A, C, q, D] for funtions:
    # [[NotSoIdealFunc], [IdealFunc], [RealFunc], [EvenMoreRealFunc]]
Param0 = [[20, - 0.02, 1.9,  0.8],
           [5, -0.01, 2.1, 0.8],
           [1.52701345, -0.04892301, 1.50104867,  0.01113391],
           [2.31567987, -0.05694363, 1.49770967, 0.17984022]]

# -------------------------------------------
# For LVMarquandt_Measurment
LVMMFilename = '500.txt'
# Start parameters [A, C, q, D] for LVMMFilename (RealFunc)
LVMMParam0 = [6.7, -5.97e-02, 2.8, 3.8e-03]
# When True, this will plot the chi square for values around  all the final values of the fit parameters
testChi2 = True
# When True, the plots also show what happens when the fitting function parameters are changed a bit.
doAllPlots = False
# ------------------------------------------
# Initial Parameter Zerofield used in "LVMarqunadt_Zero"
Zeroparam0 = [0, 0.5, 0.2, 0.1, 0.6, 0.6, 0.4]
# -------------------------------------------

# magneic field in mA
magFields = [400, 510]

# in Celsius
Temp = 118.5



