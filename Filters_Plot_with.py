import numpy as np
import astropy
from astropy.io import ascii
import matplotlib.pyplot as plt

g = ascii.read('DES_BLIND+HOSTZ/DES_g.dat')
g_W = g['col1']
g_P = g['col2']

r = ascii.read('DES_BLIND+HOSTZ/DES_r.dat')
r_W = r['col1']
r_P = r['col2']

i = ascii.read('DES_BLIND+HOSTZ/DES_i.dat')
i_W = i['col1']
i_P = i['col2']

z = ascii.read('DES_BLIND+HOSTZ/DES_z.dat')
z_W = z['col1']
z_P = z['col2']

plt.plot(g_W, g_P, label='g', color = 'forestgreen')
plt.plot(r_W, r_P, label='r', color = 'coral')
plt.plot(i_W, i_P, label='i', color = 'indianred')
plt.plot(z_W, z_P, label='z', color = 'gray')

plt.title('SDSS Filters with host-galaxy photo-z')
plt.xlabel('Wavelength ($\AA$)')
plt.ylabel('Filter Transmission')

plt.legend()
plt.show()