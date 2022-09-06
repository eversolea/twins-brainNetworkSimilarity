import scipy.io
from scipy.stats.stats import pearsonr
import numpy as np
import csv
import h5py
from statisticalAnalysisHelpers import *
import matplotlib.pyplot as plt
from statistics import mode, mean, median


CSVData = open("dz_finalDataMtx.csv")
finalDataMtx = np.loadtxt(CSVData, delimiter=",")
print(np.hsplit(finalDataMtx,5))
dzTwinCorrelation, nontwinCorrelation, ages, sex, sex2  = np.hsplit(finalDataMtx,5)
dzTwinCorrelation = dzTwinCorrelation.flatten()
nontwinCorrelation = nontwinCorrelation.flatten()
ages = ages.flatten()
sex = sex.flatten() #For some reason, all dz twins in our twin dataset had the same sex. So sex2 will be ignored

#MZ Twins Correlation vs nontwins Correlation 
plt.hist([dzTwinCorrelation,nontwinCorrelation], bins=np.arange(0.75,0.95,0.005), color=['yellowgreen', 'darkred'])
plt.savefig('hist_dzTwins_vs_nontwins.png')
plt.clf()

#MZ Twins Correlation vs Age
plt.scatter(dzTwinCorrelation, ages, c ="blue")
plt.savefig('scatter_dzTwins_vs_age.png')
plt.clf()

#MZ Twins Correlation vs Sex
plt.scatter(dzTwinCorrelation, sex, c ="yellowgreen")
plt.savefig('scatter_dzTwins_vs_sex.png')

#Group difference with Student t-test

#remove outliers for histogram
#ReadyRawMzTwinConnectomes = rawMzTwinConnectomes[0].flatten()
#ReadyConnectomeData_NoTwins = connectomeData_noTwins[0][0].flatten()


#Plot histogram to see if normal distribution exists
#drawHistogram2Dataset(mzTwinCorrelation,nontwinCorrelation,"C:\\Users\\austi\\Documents\\School\\Summer 2022\\Computational Neuroscience\\Term Project\\dataForExtractingConnectomes\\resultsCode\\test","hi","hi2")
#drawHistogramSingleDataset(ReadyRawMzTwinConnectomes,"hi","not sure","x","y""plot title","C:\\Users\\austi\\Documents\\School\\Summer 2022\\Computational Neuroscience\\Term Project\\dataForExtractingConnectomes\\twinA")

#See if variance is equal
''' No need, calculateGroupDifference does this for us
twinToNontwinData = []
twintoTwinData = []
for i in range(0, mzTwinConnectomes.size):
    twinToNontwinData.append(checkDifferenceOfVariance(mzTwinConnectomes[i][0][0].flatten(),connectomeData_noTwins[i][0].flatten())[1])
    twintoTwinData.append(checkDifferenceOfVariance(mzTwinConnectomes[i][0][0].flatten(),mzTwinConnectomes[i][1][0].flatten())[1])

print(twinToNontwinData)
print(twintoTwinData)
'''




#Group Differences tests

#Students-t test
'''
don't compare one connectomes and another connectomes with group difference
'''

print(calculateGroupDifference(dzTwinCorrelation, nontwinCorrelation))

'''
Take 2 connectomes, flatten it
Calculate correlation between them

ex. correlations b/t 50 participants
get 50x50 similarty matrix full of correlations (1x2, 1x3, 1x4, ..)
Calculate my correlation to my twin vs my correlation to the average of everyone else (or show a distribution of similarlity to everyone else and show z-score of mz twin is 2std dev away from other 49)


mz_effectSizeArray= []
mz_pValueArray = []
effectSizeArray= []
pValueArray = []

#using student-t test
for i in range(0, mzTwinConnectomes.size):
    data = calculateGroupDifference(mzTwinConnectomes[i][0][0].flatten(), connectomeData_noTwins[i][0].flatten())
    effectSizeArray.append(data[0])
    pValueArray.append(data[1])
    data = calculateGroupDifference(mzTwinConnectomes[i][0][0].flatten(), mzTwinConnectomes[i][1][0].flatten())
    mz_effectSizeArray.append(data[0])
    mz_pValueArray.append(data[1])   

print(effectSizeArray)
print(pValueArray)
print("   ")
print(mz_effectSizeArray)
print(mz_pValueArray)
'''