import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

f = open('DES_BLIND+HOSTZ/DES_SN000105.DAT', 'r')
lines = f.read()
print (lines)
f.close()

rdr = ascii.get_reader(Reader=ascii.Basic)
rdr.header.splitter.delimiter = ' '
rdr.data.splitter.delimiter = ' '
rdr.header.start_line = 14
rdr.data.start_line = 15
rdr.data.end_line = None
t = rdr.read('DES_BLIND+HOSTZ/DES_SN000105.DAT')
MJD = t['MJD']
FLT = t['FLT']
FIELD = t['FIELD']
FLUXCAL = t['FLUXCAL']
FLUXCALERR = t['FLUXCALERR']

plt.errorbar(MJD[FLT=='g'], FLUXCAL[FLT=='g'], FLUXCALERR[FLT=='g'], capsize = 4, label='g')
plt.errorbar(MJD[FLT=='r'], FLUXCAL[FLT=='r'], FLUXCALERR[FLT=='r'], capsize = 4, label='r')
plt.errorbar(MJD[FLT=='z'], FLUXCAL[FLT=='z'], FLUXCALERR[FLT=='z'], capsize = 4, label='z')
plt.errorbar(MJD[FLT=='i'], FLUXCAL[FLT=='i'], FLUXCALERR[FLT=='i'], capsize = 4, label='i')
plt.title('SN000105 with host-galazy photo-z; SNTYPE: -9')
plt.xlabel('Modified Julian Date')
plt.ylabel('Calibrated Flux')

plt.legend()
plt.show()