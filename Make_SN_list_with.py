#Go through the list of SNs and find a certain type of supernova for no host Z
#Then make a table containing a title and a col of all the types


import re
from astropy.io import ascii
from astropy.table import Table

list = ascii.read('DES_BLIND+HOSTZ/DES_BLIND+HOSTZ.LIST', data_start = 0)
i=0
SN = []
for i in range(18320):
    with open('DES_BLIND+HOSTZ/'+list['DES_SN000041.DAT'][i]) as file:
        for line in file:
            line = re.findall(r'SNTYPE: ?...', line)
            if line!= []:
                x = line
                if ((x[0][9]=='1') and (x[0][10]==' ')): #adjust for other types
                    SN = SN+[list['DES_SN000041.DAT'][i]]
    i+=1
    
data = Table({'SNIa List': SN}, names=['SNIa List']) #adjust for other types
ascii.write(data, 'with_SNIa_List.dat') #adjust for other types


'''
if ((x[0][9]=='1') and (x[0][10]==' '))
data = Table({'SNIa List': SNIa}, names=['SNIa List'])
ascii.write(data, 'SNIa_List_with.dat')

if ((x[0][9]=='-') and (x[0][10]=='9')):
data = Table({'-9 List': SN}, names=['-9 List'])
ascii.write(data, 'Type-9_List_with.dat')

if ((x[0][9]=='2') and (x[0][10]=='2')):
data = Table({'22 List': SN}, names=['22 List'])
ascii.write(data, 'Type22_List_with.dat')

etc.
(Same format for all other types)

if ((x[0][9]=='3') and (x[0][10]==' ')):
data = Table({'3 List': SN}, names=['3 List'])
ascii.write(data, 'Type3_List_with.dat')
'''