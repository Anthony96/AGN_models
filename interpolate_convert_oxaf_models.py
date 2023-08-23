#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################
__author__ = "Antonello Calabro"
__affiliation__= "INAF - Osservatorio Astronomico di Roma"
__email__  = "antonello.calabro@inaf.it"
__status__ = "Production"
###################################################################

# Import necessary modules
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from astropy.io import ascii
from astropy.table import Table
import sys,os,glob
# import matplotlib.pyplot as plt

# Files AA1 to AA8 are created with the oxaf tool on the GitHub page: https:// github.com/ADThomas-astro/oxaf.
folderAA='*****' # put your directory 
fileAA1='oxaf_sed_-1.70_2.0_0.10'
fileAA2='oxaf_sed_-1.70_2.0_0.40'
fileAA3='oxaf_sed_-1.00_2.0_0.10'
fileAA4='oxaf_sed_-1.00_2.0_0.40'
fileAA5='oxaf_sed_-1.70_2.0_0.25'
fileAA6='oxaf_sed_-1.00_2.0_0.25'
fileAA7='oxaf_sed_-1.22_2.0_0.25' 
fileAA8='oxaf_sed_-1.22_2.0_0.25'
#
file_chosen=fileAA6   # Choose one SED 
#
#
tab_input=np.genfromtxt(folderAA+file_chosen+'_4python.txt',dtype=None,names=True)
xAA_orig00=tab_input['kev']
yAA_orig00=tab_input['nuFnu']

# conversion from keV to Ryd :
# xAA=xAA*1000*0.0734985857
# conversion from kev to Hz
convfactor=2.417989242*1E14
xAA_orig=xAA_orig00*1000*convfactor # This is in Hertz
xAA=np.log10(xAA_orig)
# Take the logarithm of yAA : 

# Io ho nuFnu, ma lui in interp vuole soltanto log(Fnu)
yAA_orig=yAA_orig00/xAA_orig
yAA=np.log10(yAA_orig)+17

# ------------------------------------------------
int_function=interp1d(xAA,yAA)
new_x=np.linspace(min(xAA),max(xAA),30)
new_y=int_function(new_x)
#
#
# NOW save result !!!
data = Table()
data['x'] = np.array(new_x, dtype=np.float64)
data['y'] = new_y
ascii.write(data, folderAA+file_chosen+'_4interp.txt', overwrite=True)

print('---- End program ----')
quit()
