#Find out what types are out there since not all are included in readme for with host Z
#Count how many exist for each type
#Result: {'-9': 17064, '1 ': 879, '22': 218, '32': 55, '21': 44, '33': 45, '3 ': 13, '23': 2}

import re
from astropy.io import ascii
from astropy.table import Table

list = ascii.read('DES_BLIND+HOSTZ.LIST', data_start = 0)
i=0
SN = dict()

for i in range(18320):
    with open(list['DES_SN000041.DAT'][i]) as file:
        for line in file:
            line = re.findall(r'SNTYPE: ?...', line)
            if line!= []:
                x = line
                type = (x[0][9])+(x[0][10])
                if type not in SN:
                    SN[type] = 1
                else:
                    SN[type] += 1
    i+=1