# -*- coding: utf-8 -*-
"""
Created Do Jan 17 2019
This script let you do the fitting and plotting for the Stern-Gerlach-Experiment automatically.
It also saves the plot and the output-Data automatically in the data folder.

@author: ruby@physik.uzh.ch
based partially on jungfranckianer & fraublauwal
"""

from scipy import array
import matplotlib.pyplot as pl
from scipy.optimize import leastsq
from numpy import sqrt, diag
import functionsSG as fSG
import os.path
import parameters  as GPara


FUNCTION_DICT = {"NotSoIdealFunc" : fSG.NotSoIdealFunc,
                "IdealFunc" : fSG.IdealFunc,
                "RealFunc" : fSG.RealFunc,
                "EvenMoreRealFunc": fSG.EvenMoreRealFunc}

RESIDUAL_DICT = {"NotSoIdealFunc" : fSG.NotSoIdealFuncResiduals,
                "IdealFunc" : fSG.IdealFuncResiduals,
                "RealFunc" : fSG.RealFuncResiduals,
                "EvenMoreRealFunc": fSG.EvenMoreRealFuncResiduals}

PARA_DICT  = {"NotSoIdealFunc" : 0,
                "IdealFunc" : 1,
                "RealFunc" : 2,
                "EvenMoreRealFunc": 3}


# Read data from file "parameters.py"
file_location = GPara.file_location
filenames = GPara.filenames
widthFit = GPara.widthFit
aParam0 = GPara.Param0

errqList = array([[0.]*len(filenames)]*4)
qList = array([[0.]*len(filenames)]*4)


def doAll(file_location, filename, function_name, nFile):
    '''
    Fits, plots, and saves Stern-Gerlach data
    Input: file path, fit function
    Output: graph, final fit parameters, initial guess, covariance matrix, chi2, summary files.
    '''

    function_in_use = FUNCTION_DICT[function_name]
    residual_in_use = RESIDUAL_DICT[function_name]
    nPara = PARA_DICT[function_name]
    print("\n\n -------- Processing file %s" % filename)

    x, y = fSG.load_data(file_location, filename, widthFit)
    

    #intial parameter for funtions (usually only 'A' differs)

    #do fit
    pname = ['A', 'Center', 'q', 'D']
    param0 = aParam0[nPara] #initial params
    plsq = leastsq(residual_in_use, param0, args=(y, x), maxfev=1000, full_output=True)
    paramFinal, err = plsq[0], plsq[1]
    fit = function_in_use(paramFinal, x)
    initialGuess = function_in_use(param0, x)
    qList[nPara][nFile-1]=paramFinal[2]         # q-values for summary file
    aParam0[nPara]=paramFinal
    errqList[nPara][nFile-1]=sqrt(diag(err))[2] # error q-values for summary file
    #show results and plot
    pl.figure(num=None, figsize=(6, 7), dpi=150)
    pl.plot(x, y, 'bo', label=' data')
    pl.plot(x, fit, 'r', label='fit')
    pl.plot(x, initialGuess,'g', label='initial guess')
    pl.legend()
    pl.xlabel('Distance [mm]')
    pl.ylabel('Voltage [V]')
    pl.title('%s at %s' % (function_name,filename))

    print('Final parameters', paramFinal)
    print('Error',sqrt(diag(err)))
    print('Initial guess', param0)
    print('Covariance matrix', err)
    chi2  = sum(residual_in_use(paramFinal,y,x)**2)
    print('chi2 ', chi2)

    #save graph
    graph_name="%s-%s.pdf" % (function_name,filename[:-4])
    output_name = os.path.join(file_location,graph_name)
    print("Saving figure to ", output_name)
    pl.savefig(output_name)

    #save fit info
    text_output_name = os.path.join(file_location,graph_name[:-4]+".txt")
    print("Saving fit info to ", text_output_name)
    out_f = open(text_output_name,"w")
    out_f.write(graph_name[:-4]+'.txt\n')
    out_f.write('Fit Parameter:  ')
    out_f.write(str(pname)+'\n')
    out_f.write('Initial Parameter:  ')
    out_f.write(str(param0)+'\n')
    out_f.write('Final Parameter:  ')
    out_f.write(str(paramFinal)+'\n')
    out_f.write('Error:  ')
    out_f.write(str(sqrt(diag(err)))+'\n')
    out_f.write('Chi2:  ')
    out_f.write(str(chi2)+'\n\n')
    out_f.write('txt_cov:  ')
    out_f.write(str(err)+'\n')
    out_f.write('output of least square fit\n')
    for piece in plsq:
        out_f.write(str(piece)+'\n')
    out_f.close()

    #save summary file

    if nFile == len(filenames):
        for i in range(len(errqList[nPara])):
            errqList[nPara][i]="%0.4f" % errqList[nPara][i]
        for i in range(len(qList[nPara])):
            qList[nPara][i]="%0.4f" % qList[nPara][i]
        text_output_name = os.path.join(file_location,function_name+"_Summay.txt")
        print("Saving fitresults into", text_output_name)
        out_sf = open(text_output_name,"w")
        out_sf.write('Summary.txt\n')
        out_sf.write('Filenames:  ')
        out_sf.write(str(filenames)+'\n')
        out_sf.write('summary q-values: ')
        out_sf.write(str(qList[nPara])+'\n')
        out_sf.write('summary q-errors: ')
        out_sf.write(str(errqList[nPara])+'\n\n')
        out_sf.close()


if __name__ == "__main__":
    nFile = 0
    for file in filenames:
        nFile =nFile+1  # file count for summary

        # Use all funtions for each file ->  takes very long !!!
        #for function in list(FUNCTION_DICT.keys()):
         #    doAll(file_location, file, function,nFile)

        ## or    choose only  one of the functions (comment 2 lines above and uncomment line below)
        function= GPara.function
        doAll(file_location, file, function,nFile)
