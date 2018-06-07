#Find out what types are out there since not all are included in readme
#Count how many exist for each type
#Result: {'-9': 17068, '1 ': 834, '22': 236, '32': 73, '33': 62, '21': 48, '3 ': 13, '23': 13}

import re
from astropy.io import ascii
from astropy.table import Table

list = ascii.read('DES_BLINDnoHOSTZ.LIST', data_start = 0)
i=0
SN = dict()

for i in range(18347):
    with open(list['DES_SN000018.DAT'][i]) as file:
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
