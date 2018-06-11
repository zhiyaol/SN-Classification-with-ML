from astropy.io import ascii
import matplotlib.pyplot as plt

rdr = ascii.get_reader(Reader=ascii.Basic)
rdr.header.splitter.delimiter = ' '
rdr.data.splitter.delimiter = ' '
rdr.header.start_line = 12
rdr.data.start_line = 13
rdr.data.end_line = None
t = rdr.read('DES_SN000018.DAT')
MJD = t['MJD']
FLT = t['FLT']
FIELD = t['FIELD']
FLUXCAL = t['FLUXCAL']
FLUXCALERR = t['FLUXCALERR']

plt.errorbar(MJD[FLT=='g'], FLUXCAL[FLT=='g'], FLUXCALERR[FLT=='g'], capsize = 4, label='g',color = 'forestgreen') 
plt.errorbar(MJD[FLT=='r'], FLUXCAL[FLT=='r'], FLUXCALERR[FLT=='r'], capsize = 4, label='r',color = 'coral')
plt.errorbar(MJD[FLT=='i'], FLUXCAL[FLT=='i'], FLUXCALERR[FLT=='i'], capsize = 4, label='i', color = 'indianred')
plt.errorbar(MJD[FLT=='z'], FLUXCAL[FLT=='z'], FLUXCALERR[FLT=='z'], capsize = 4, label='z', color = 'gray')
plt.title('SN000018 without host-galazy photo-z; SNTYPE: -9')
plt.xlabel('Modified Julian Date')
plt.ylabel('Calibrated Flux')

plt.legend()
plt.show()