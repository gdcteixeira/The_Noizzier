###The_Noizzier

Program to add noise to a spectra

This is the current version which takes a spectra and produces
several fits files with degrading SNR

v1.01 2015-04-22
@author: gdcteixeira
_________________________________
*REQUIRED PYTHON LIBRARIES:

numpy
astropy
PyAstronomy

*INSTALLATION:

In order to make The_Noizzier an executable file you need to change the 
file permissions of The_Noizzier_v1.01.py using the command:

chmod +x The_Noizzier_v1.01.py

*INPUT PARAMETERS:

filenames - a file with the filenames of the spectra to be degraded. 
Additionally you can also input your own measured SNR of that spectra
in the same file. If so the file should be an ASCII file with two columns,
the filename, SNR

numb_degradations - the number of degraded spectra you want to obtain. This
number will influence the noise introduced at each step


*OUTPUT

The output consists of :
fits files for spectra with increasing levels of noise. The filename will
have an estimative of the SNR of that spectra

*RUNTIME

The_Noizzier is a relatively fast code so it should finish with relative
speed. Limiting factors of speed, the number of files to introduce noise
into and the number of degradations demanded.

*RUNNING The_Noizzier

To get help on the input use the command 
./The_Noizzier_v1.01.py	-h

*TEST SUITE

In this repository it is also available a directory with one spectrum,
in order to test the program.

*EXAMPLE

Running the program with the test suite
./The_Noizzier_v1.01.py list_of_files_v2.dat -d 10

*CHANGELOG

The v1.01 no longer requires a configuration file.
Added argparse module.

*TROUBLESHOOT AND FEEDBACK

If you have any problems with the code or want to give feedback, please contact the author: G. D . C. Teixeira

