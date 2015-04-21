#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The_Noizzier

Program that adds noise to spectra.
The program reads the config file, which has the name of a file
which is a list of files to be degraded and the number of degradations
required.

Additionally you can also input the SNR you measured into the list of files.

The list of files should be similar to:

star1.dat 100
star2.dat 150

If an estimation of the SNR is not provided the program will perform
an estimative alone.
Also possible to configure is the number of degradations wanted.

You should alter the variables in the file "The_Noizzier_config.py".

To make the file executable you need to use the following command:

chmod +x TheNoizzier.py
To run this program just write  ./TheNoizzier.py in the terminal

v1.00    2015-04-20

@author: gdcteixeira
"""

from astropy.io import fits as pyf
import numpy as np
from PyAstronomy import pyasl
from The_Noizzier_config import filenames, numb_degradations


def fits_reader(filename):
    """
    fits_reader
    Function that reads the header and the data of a function
    input: filename
    output: datapoints and header
    """
    data = pyf.getdata(filename)
    header = pyf.getheader(filename)
    return data, header


def skaro_degradations(filename, initial_noise=False, numb_degradation=10):
    """
    skaro_degradations
    Function that computes and writes new spectra with added noise
    Input: filename; initial noise - how much noise the original spectra has;
    numb_degratation - number of degradations to compute
    Output: the program produces several files with the lower SNR
    """
    data, header = fits_reader(filename)
    string_name = str(filename)
    string_name = string_name.replace('.fits', '')
    data_temp = np.array([element for element in data if element != 0])
    if not initial_noise:
        esti_noise = pyasl.estimateSNR(np.arange(len(data_temp)), data_temp, 27,
                                       deg=3, controlPlot=False)
        initial_noise = esti_noise["SNR-Estimate"]
    noise_step = initial_noise/numb_degradation
    for i in range(numb_degradation):
        noise = initial_noise-noise_step*i
        new_flux = noize_adder(noise, data, len(data))
        pyf.writeto(str(string_name)+'snr'+str(int(noise))+'.fits', new_flux,
                    header)
    return

def noize_adder(new_noise, data, number_of_points):
    """
    noize_adder
    Function that adds noise using a normal distribution
    input: new_noise - noise to add; data - flux data; number_of_points: number
    of points to compute, by default this is equal to the original datapoints
    in order not to lose resolution
    output: data - flux data with added noise
    """
    norm = np.random.normal(0, 1, number_of_points)*float(1)/new_noise+1
    data = data*norm
    return data

###################################
###################################
##             MAIN              ##
###################################
###################################

print "WELCOME TO The_Noizzier v1.0"
print "AUTHOR: gdcteixeira"
print "The_Noizzier WILL NOW TAKE OPERATIONAL CONTROL............."
print "ACKNOWLEDGED USER. OPERATIONAL CONTROL ON............."


for line in open(filenames):
    line = line.split()
    if len(line) != 2:
        skaro_degradations(line[0], False, numb_degradations)
    else:
        skaro_degradations(line[0], float(line[1]), numb_degradations)

print str("Successfully created "+str(numb_degradations)+" degraded spectra "+
          "for each file")


print "RELEASING OPERATIONAL CONTROL............."
print str("The_Noizzier HAS SUCCESSFULLY COMPLETED ALL TASKS AND RETURNED "+
          "CONTROL TO THE USER.")
 