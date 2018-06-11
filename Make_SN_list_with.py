#Go through the list of SNs and find a certain type of supernova for no host Z
#Then make a table containing a title and a col of all the types


import re
from astropy.io import ascii
from astropy.table import Table

list = ascii.read('DES_BLIND+HOSTZ/DES_BLIND+HOSTZ.LIST', data_start = 0)
i=0
SNIa = []
for i in range(18320):
    with open('DES_BLIND+HOSTZ/'+list['DES_SN000041.DAT'][i]) as file:
        for line in file:
            line = re.findall(r'SNTYPE: ?...', line)
            if line!= []:
                x = line
                if ((x[0][9]=='1') and (x[0][10]==' ')): #adjust for other types
                    SNIa = SNIa+[list['DES_SN000041.DAT'][i]]
    i+=1
    
data = Table({'SNIa List': SNIa}, names=['SNIa List']) #adjust for other types
ascii.write(data, 'SNIa_List_with.dat') #adjust for other types