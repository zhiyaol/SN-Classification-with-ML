from astropy.io import ascii
from astropy.table import Table
import matplotlib.pyplot as plt
import re
import numpy as np


def getData(folder, filename): #I'm finally using python properly
    rdr = ascii.get_reader(Reader=ascii.Basic)
    rdr.header.splitter.delimiter = ' '
    rdr.data.splitter.delimiter = ' '
    if folder == 'DES_BLINDnoHOSTZ':
        rdr.header.start_line = 12
        rdr.data.start_line = 13
    else:
        rdr.header.start_line = 14
        rdr.data.start_line = 15
    rdr.data.end_line = None
    t = rdr.read('%s/%s' % (folder, filename))
    return t
    
def getInfo(info, file):
    for line in file:
        if line.startswith('%s' % info):
            return line[(len(info)+2)::] #might have extra spaces in front and it's a string
    return None

def makeTable(folder):
    #folder: no vs +
    #infoL: info list. eg. 'SNID', 'SNTYPE', 'FILTERS', 'RA', 'DECL', 'FAKE', 'MWEBV', ETC.
    #totalNum: total number of supernovae in the foler. Might be improved to automatically going through all files in a folder
    if folder == 'DES_BLINDnoHOSTZ':
        colName = 'DES_SN000018.DAT'
        totalNum = 18347
        infoL = ['SURVEY','SNID', 'SNTYPE', 'FILTERS', 'RA', 'DECL', 'FAKE', 'MWEBV', 'REDSHIFT_SPE','NOBS', 'NVAR']
    else:
        colName = 'DES_SN000041.DAT'
        totalNum = 18320
        infoL = ['SURVEY','SNID','SNTYPE','FILTERS','RA','DECL','FAKE','MWEBV','REDSHIFT_SPE','HOST_GALAXY_GALID','HOST_GALAXY_PHOTO-Z','NOBS','NVAR']

    list = ascii.read('%s/%s.LIST' % (folder, folder), data_start = 0)
    table = dict()
    for i in infoL:
        table[i] = []
    table['FILENAME'] = []
    #table['DATA'] = []
    for i in range(totalNum):
        with open(folder + '/' + list[colName][i]) as file:
            table['FILENAME'] += [list[colName][i]]
            #table['DATA'] += [getData(folder, list[colName][i])]
            for j in infoL:
                table[j] += [getInfo(j, file)]
    infoList = [np.array(table['FILENAME'])]
    for i in infoL:
        infoList += [np.array(table[i])]
    #infoList += [np.array(table['DATA'])]
    output = Table(infoList, names = ['FILENAME']+infoL)
    #output = Table(infoList, names = ['FILENAME']+infoL+['DATA'])
    return output
    
def writeFile(folder):
    data = makeTable(folder)
    ascii.write(data, '%s_combined.dat' % folder)
    return None
    
#data = makeTable('DES_BLINDnoHOSTZ')
writeFile('DES_BLINDnoHOSTZ')