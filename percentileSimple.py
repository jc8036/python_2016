##IMPORT DATA##
import csv

with open('BrueDataQt.csv') as BrueDataQtcsv: #open the file
    reader = csv.reader(BrueDataQtcsv)                  #read lines
    timeSeriesFromCSV=list(reader)                      #create list
    timeSeries=[float(entry[0]) for entry in timeSeriesFromCSV] #convert lists to floats

##FIND 80th PERCENTILE##
timeSeriesSorted=sorted(timeSeries)    #sort the data

#find the length of the list and therefore the 80th percentile value
pc80=timeSeriesSorted[int(len(timeSeriesSorted)*0.8)]

#import numpy
#pc80=numpy.percentile(timeSeries, 80)

##FIND EXCEEDING VALUES##
floods=[]

for i in timeSeries:   #loop through
    if i > pc80:       #check value
        floods.append(i)#add to list

#floods=[i for i in timeSeries if i>pc80]

##FIND TIMESTEP INDEX##
#for i in range(len(timeSeries)):   #loop through
#    if timeSeries[i] > pc80:       #check value
#        floods.append([i,timeSeries[i]])#add to list
#floods=[[i,timeSeries[i]] for i in range(len(timeSeries)) if timeSeries[i]>pc80]


##PLOT RESULTS##

#import matplotlib.pyplot as plt
#plt.plot(timeSeries)
#plt.plot(timeSeriesSorted)
#plt.axhline(y=pc80)
#plt.axvline(x=int(len(timeSeriesSorted)*0.8))
#plt.plot(floods)
#plt.scatter([p[0] for p in floods], [p[1] for p in floods])