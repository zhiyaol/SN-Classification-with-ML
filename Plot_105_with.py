import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

f = open('no_SNIa_List.dat', 'r')
lines = f.read()
print (lines)
f.close()

'''rdr = ascii.get_reader(Reader=ascii.Basic)
rdr.header.splitter.delimiter = ' '
rdr.data.splitter.delimiter = ' '
rdr.header.start_line = 14
rdr.data.start_line = 15
rdr.data.end_line = None
t = rdr.read('DES_BLIND+HOSTZ/DES_SN000105.DAT')
FLUXCALERR = t['FLUXCALERR']
MJD = t['MJD']
UMJD = MJD[FLUXCALERR>0]
FLT = t['FLT']
UFLT = FLT[FLUXCALERR>0]
FIELD = t['FIELD']
UFIELD = FIELD[FLUXCALERR>0]
FLUXCAL = t['FLUXCAL']
UFLUXCAL = FLUXCAL[FLUXCALERR>0]
UFLUXCALERR = FLUXCALERR[FLUXCALERR>0]

plt.errorbar(UMJD[UFLT=='g'], UFLUXCAL[UFLT=='g'], UFLUXCALERR[UFLT=='g'], capsize = 4, label='g')
plt.errorbar(UMJD[UFLT=='r'], UFLUXCAL[UFLT=='r'], UFLUXCALERR[UFLT=='r'], capsize = 4, label='r')
plt.errorbar(UMJD[UFLT=='z'], UFLUXCAL[UFLT=='z'], UFLUXCALERR[UFLT=='z'], capsize = 4, label='z')
plt.errorbar(UMJD[UFLT=='i'], UFLUXCAL[UFLT=='i'], UFLUXCALERR[UFLT=='i'], capsize = 4, label='i')
plt.title('SN000105 with host-galazy photo-z; SNTYPE: -9')
plt.xlabel('Modified Julian Date')
plt.ylabel('Calibrated Flux')

plt.legend()
plt.show()'''