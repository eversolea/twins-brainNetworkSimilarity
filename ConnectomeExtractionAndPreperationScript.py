import scipy.io
from scipy.stats.stats import pearsonr
import numpy as np
import csv
import h5py
from statisticalAnalysisHelpers import *

#Importing the Matlab data using scipy
connectomesFromMatlab = scipy.io.loadmat('loadable2.mat')
twinInfoFromMatlab = scipy.io.loadmat('twinCovariatesDWI_only_twin.mat')

connectomeData = connectomesFromMatlab["ADJS"][0]
patientID_Data = connectomesFromMatlab["SUBS"]

dzTwins_id = twinInfoFromMatlab["DZ_ID"]
dzTwins_age = twinInfoFromMatlab["DZ_age"]
dzTwins_sex = twinInfoFromMatlab["DZ_sex"]

mzTwins_id = twinInfoFromMatlab["MZ_ID"]
mzTwins_age = twinInfoFromMatlab["MZ_age"]
mzTwins_sex = twinInfoFromMatlab["MZ_sex"]


#TODO: Refactor the below so i dont use _nextIndex's anymore or np.empty ... forgot about .append()

#Create an array to keep track of indexes of  twins in connectomeData.
#After we have pulled the dz and mz twins out of connectomeData, we want an array of only non-twin connectomes.
dzMzTwinIndexes = np.empty(dzTwins_id.size + mzTwins_id.size)
dzMzTwinIndexes_nextIndex = 0

#Creating the dzTwinConnectomes data structure. It will be structured as follows:
# dzTwinConnectomes[0]
#   -Twin A array
#       [0] Connectome, [1] patientID
#       [2] Age, [3] Sex
#   -Twin B array
#       [0] Connectome, [1] patientID
#       [2] Age, [3] Sex
dzTwinConnectomes = np.empty(dzTwins_id.shape[0], dtype = np.ndarray)
#Creating rawDzTwinConnectomes array which will only contain connectomes
rawDzTwinConnectomes = []

#Populating the dzTwinConnectomes data structure
for i in range(0, dzTwins_id.shape[0]):
    data = [[],[]]
    patientData = [[],0,0,0]
    
    #Get index for Twin A to access in connectomeData array, and populate data structure
    index = np.where(patientID_Data == dzTwins_id[i][0])[0][0]
    dzMzTwinIndexes[dzMzTwinIndexes_nextIndex] = index
    dzMzTwinIndexes_nextIndex = dzMzTwinIndexes_nextIndex + 1

    rawDzTwinConnectomes.append(connectomeData[index])
    
    #These connectomes have 380 regions - 180 regions per hemisphere based on the HCPMMP1 parcellation (360 reigons) and 10 subcortical regions.
    #Lines 1-180 represent the left hemisphere, while lines 191-370 represent the right hemisphere.
    #So we will store this connectome as a 360 reigon connectome using lines 1-180 and lines 191-370 
    patientData[0] = np.delete(np.delete(connectomeData[index], slice(370,380), 0), slice(370,380), 1) #Trim last 10 subcortical reigons
    patientData[0] = np.delete(np.delete(patientData[0], slice(180,190), 0), slice(180,190), 1) #Trim first 10subcortical reigons
    #print(patientData[0].shape) #Debug
    patientData[1] = dzTwins_id[i][0]
    patientData[2] = dzTwins_age[i][0]
    patientData[3] = dzTwins_sex[i][0]
    data[0] = patientData

    

    patientData = [[],0,0,0]
    #Get index for Twin B to access in connectomeData array, and populate data structure
    index = np.where(patientID_Data == dzTwins_id[i][1])[0][0]
    dzMzTwinIndexes[dzMzTwinIndexes_nextIndex] = index
    dzMzTwinIndexes_nextIndex = dzMzTwinIndexes_nextIndex + 1

    rawDzTwinConnectomes.append(connectomeData[index])

    patientData[0] = np.delete(np.delete(connectomeData[index], slice(370,380), 0), slice(370,380), 1) #Trim last 10 subcortical reigons
    patientData[0] = np.delete(np.delete(patientData[0], slice(180,190), 0), slice(180,190), 1) #Trim first 10subcortical reigons
    patientData[1] = dzTwins_id[i][1]
    patientData[2] = dzTwins_age[i][1]
    patientData[3] = dzTwins_sex[i][1]
    data[1] = patientData

    #Populate dzTwinConnectomes
    dzTwinConnectomes[i] = data





#Creating the mzTwinConnectomes data structure. It will be structured same as  dzTwinConnectomes
mzTwinConnectomes = np.empty(mzTwins_id.shape[0], dtype = np.ndarray)
#Creating rawMzTwinConnectomes array which will only contain connectomes
rawMzTwinConnectomes = []

#Populating the mzTwinConnectomes data structure
for i in range(0, mzTwins_id.shape[0]):
    data = [[],[]]
    patientData = [[],0,0,0]
    
    #Get index for Twin A to access in connectomeData array, and populate data structure
    index = np.where(patientID_Data == mzTwins_id[i][0])[0][0]
    dzMzTwinIndexes[dzMzTwinIndexes_nextIndex] = index
    dzMzTwinIndexes_nextIndex = dzMzTwinIndexes_nextIndex + 1

    rawMzTwinConnectomes.append(connectomeData[index])
    
    patientData[0] = np.delete(np.delete(connectomeData[index], slice(370,380), 0), slice(370,380), 1) #Trim last 10 subcortical reigons
    patientData[0] = np.delete(np.delete(patientData[0], slice(180,190), 0), slice(180,190), 1) #Trim first 10subcortical reigons
    patientData[1] = mzTwins_id[i][0]
    patientData[2] = mzTwins_age[i][0]
    patientData[3] = mzTwins_sex[i][0]
    data[0] = patientData

    patientData = [[],0,0,0]
    #Get index for Twin B to access in connectomeData array, and populate data structure
    index = np.where(patientID_Data == mzTwins_id[i][1])[0][0]
    dzMzTwinIndexes[dzMzTwinIndexes_nextIndex] = index
    dzMzTwinIndexes_nextIndex = dzMzTwinIndexes_nextIndex + 1

    rawMzTwinConnectomes.append(connectomeData[index])

    patientData[0] = np.delete(np.delete(connectomeData[index], slice(370,380), 0), slice(370,380), 1) #Trim last 10 subcortical reigons
    patientData[0] = np.delete(np.delete(patientData[0], slice(180,190), 0), slice(180,190), 1) #Trim first 10subcortical reigons
    patientData[1] = mzTwins_id[i][1]
    patientData[2] = mzTwins_age[i][1]
    patientData[3] = mzTwins_sex[i][1]
    data[1] = patientData
    
    #Populate dzTwinConnectomes
    mzTwinConnectomes[i] = data




#Make a new connectomeData_noTwins array with no twins. It will be structured as follows:
#  connectomeData_noTwins[0]
#    [0] Connectome, [1] patientID

numNonTwins = connectomeData.size - (dzTwins_id.size + mzTwins_id.size)
connectomeData_noTwins = np.empty(numNonTwins, dtype = np.ndarray)
connectomeData_noTwins_nextIndex = 0

#Populate connectomeData_noTwins with all nontwin connectomes
for i in range(0, connectomeData.size):
    #if current connectome is not a twin:
    if i not in dzMzTwinIndexes:
        data = [[],0]
        data[0] = np.delete(np.delete(connectomeData[i], slice(370,380), 0), slice(370,380), 1) #Trim last 10 subcortical reigons
        data[0] = np.delete(np.delete(data[0], slice(180,190), 0), slice(180,190), 1) #Trim first 10subcortical reigons
        data[1] = patientID_Data[i]
        connectomeData_noTwins[connectomeData_noTwins_nextIndex] = data
        connectomeData_noTwins_nextIndex = connectomeData_noTwins_nextIndex + 1
        #TODO: Can I find Age and Sex data to populate connectomeData_noTwins with?

#Debug print to make sure our data acquisition code worked correctly
print(connectomeData_noTwins.shape)
print(mzTwinConnectomes.shape)
print(dzTwinConnectomes.shape)




#Render connectome heatmaps
heatMap(mzTwinConnectomes[0][0][0], True, "C:\\Users\\austi\\Documents\\School\\Summer 2022\\Computational Neuroscience\\Term Project\\dataForExtractingConnectomes\\connectomeImages\\mzConnectome","#777777",0.05)
heatMap(mzTwinConnectomes[0][1][0], True, "C:\\Users\\austi\\Documents\\School\\Summer 2022\\Computational Neuroscience\\Term Project\\dataForExtractingConnectomes\\connectomeImages\\mzConnectome2","#777777",0.05)
heatMap(dzTwinConnectomes[0][0][0], True, "C:\\Users\\austi\\Documents\\School\\Summer 2022\\Computational Neuroscience\\Term Project\\dataForExtractingConnectomes\\connectomeImages\\dzConnectome","#777777",0.05)
heatMap(dzTwinConnectomes[0][1][0], True, "C:\\Users\\austi\\Documents\\School\\Summer 2022\\Computational Neuroscience\\Term Project\\dataForExtractingConnectomes\\connectomeImages\\dzConnectome2","#777777",0.05)
heatMap(connectomeData_noTwins[0][0], True, "C:\\Users\\austi\\Documents\\School\\Summer 2022\\Computational Neuroscience\\Term Project\\dataForExtractingConnectomes\\connectomeImages\\nonTwin","#777777",0.05)
heatMap(connectomeData_noTwins[2][0], True, "C:\\Users\\austi\\Documents\\School\\Summer 2022\\Computational Neuroscience\\Term Project\\dataForExtractingConnectomes\\connectomeImages\\nonTwin2","#777777",0.05)


#Statistical Analysis below:
#============================

#Reminder:
# mzTwinConnectomes[0]
#   -Twin A array
#       [0] Connectome, [1] patientID
#       [2] Age, [3] Sex
#   -Twin B array
#       [0] Connectome, [1] patientID
#       [2] Age, [3] Sex

'''
#Creating Correlation Similarity Matrix for mz twins

correlSimMtx = np.empty([234,234]) #Initializing the Correlation Similarity Matrix
twin = 0 #variable that stores 0 or 1 (to read Twin A or Twin B's array in mzTwinConnectomes)
rowConnectome = [[0]] #variable to hold the row connectome we are performing correlation on for the correlation similarity matrix

for row in range(0,234):
    #set rowConnectome
    test = mzTwinConnectomes[int(row/ 2)]
    if(row % 2 == 0):
        rowConnectome = mzTwinConnectomes[int(row/ 2)][0][0]
    else:
        rowConnectome = mzTwinConnectomes[int(row/ 2)][1][0]
    
    #Populate columns with correlation with rowConnectome
    for column in range(0,234):
        if(column % 2 == 0):
            twin = 0 #Twin A
        else:
            twin = 1 #Twin B
        print(row)
        result = pearsonr(mzTwinConnectomes[int(column / 2)][twin][0].flatten(),rowConnectome.flatten())
        correlSimMtx[row][column] = result[0]


print(correlSimMtx)

finalDataMtx = np.empty([117,4]) #Initializing the final data matrix 
for row in range(0,234):
    #We only need one of the twins (we will take Twin A)
    if(row % 2 == 0):
        #Pull the data from the Correlation Similarity Matrix
        #Since we are using Twin A for our rows, Twin B's column will be row + 1 
        finalDataMtx[int(row/2)][0] = correlSimMtx[row][row + 1]

        #Now we will calculate the average of Twin A's correlation with all of its nontwins.
        average = 0.0
        for column in range(0,234):
            if column == row or column == row + 1:
                continue
            else:
                average = average + correlSimMtx[row][column]
        finalDataMtx[int(row/2)][1] = average / 232 # 234 - 2 for Twin A and Twin B 

        #Add mz twins age and Sex
        finalDataMtx[int(row/2)][2] = mzTwinConnectomes[int(row/ 2)][0][2] #Age
        finalDataMtx[int(row/2)][3] = mzTwinConnectomes[int(row/ 2)][0][3] #Sex

print(finalDataMtx)

#export finalDataMatrix to csv file

with open('mz_finalDataMtx.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(finalDataMtx)

'''
'''
#Creating Correlation Similarity Matrix for dz twins

correlSimMtx = np.empty([120,120]) #Initializing the Correlation Similarity Matrix
twin = 0 #variable that stores 0 or 1 (to read Twin A or Twin B's array in mzTwinConnectomes)
rowConnectome = [[0]] #variable to hold the row connectome we are performing correlation on for the correlation similarity matrix

for row in range(0,120):
    #set rowConnectome
    test = dzTwinConnectomes[int(row/ 2)]
    if(row % 2 == 0):
        rowConnectome = dzTwinConnectomes[int(row/ 2)][0][0]
    else:
        rowConnectome = dzTwinConnectomes[int(row/ 2)][1][0]
    
    #Populate columns with correlation with rowConnectome
    for column in range(0,120):
        if(column % 2 == 0):
            twin = 0 #Twin A
        else:
            twin = 1 #Twin B
        print(row)
        result = pearsonr(dzTwinConnectomes[int(column / 2)][twin][0].flatten(),rowConnectome.flatten())
        correlSimMtx[row][column] = result[0]


print(correlSimMtx)

finalDataMtx = np.empty([60,5]) #Initializing the final data matrix 
for row in range(0,120):
    #We only need one of the twins (we will take Twin A)
    if(row % 2 == 0):
        #Pull the data from the Correlation Similarity Matrix
        #Since we are using Twin A for our rows, Twin B's column will be row + 1 
        finalDataMtx[int(row/2)][0] = correlSimMtx[row][row + 1]

        #Now we will calculate the average of Twin A's correlation with all of its nontwins.
        average = 0.0
        for column in range(0,120):
            if column == row or column == row + 1:
                continue
            else:
                average = average + correlSimMtx[row][column]
        finalDataMtx[int(row/2)][1] = average / 118 # 120 - 2 for Twin A and Twin B 

        #Add mz twins age and Sexes
        finalDataMtx[int(row/2)][2] = dzTwinConnectomes[int(row/ 2)][0][2] #Age
       
        finalDataMtx[int(row/2)][3] = dzTwinConnectomes[int(row/ 2)][0][3] #Sex of Twin A
        finalDataMtx[int(row/2)][4] = dzTwinConnectomes[int(row/ 2)][1][3] #Sex of Twin B

print(finalDataMtx)

#export finalDataMatrix to csv file

with open('dz_finalDataMtx.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(finalDataMtx)

'''

'''
#Creating Correlation Similarity Matrix for nonwins

correlSimMtx = np.empty([120,120]) #Initializing the Correlation Similarity Matrix. Lets just grab the first 120 of the 619 nontwins.
twin = 0 #variable that stores 0 or 1 (to read Twin A or Twin B's array in mzTwinConnectomes)
rowConnectome = [[0]] #variable to hold the row connectome we are performing correlation on for the correlation similarity matrix

for row in range(0,120):
    #set rowConnectome
    test = connectomeData_noTwins[int(row)]
    rowConnectome = connectomeData_noTwins[int(row)][0]

    
    #Populate columns with correlation with rowConnectome
    for column in range(0,120):
        print(row)
        result = pearsonr(connectomeData_noTwins[int(column)][0].flatten(),rowConnectome.flatten())
        correlSimMtx[row][column] = result[0]


print(correlSimMtx)

finalDataMtx = np.empty([120,2]) #Initializing the final data matrix 
for row in range(0,119):

    #Pull the data from the Correlation Similarity Matrix
    finalDataMtx[int(row)][0] = correlSimMtx[row][row + 1]

    #Now we will calculate the average of patient A's correlation withother patients
    average = 0.0
    for column in range(0,120):
        if column == row or column == row + 1:
            continue
        else:
            average = average + correlSimMtx[row][column]
    finalDataMtx[int(row)][1] = average / 118 # 120 - 2 for Patient A and patient B


print(finalDataMtx)

#export finalDataMatrix to csv file

with open('nontwins_finalDataMtx.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(finalDataMtx)

'''