import requests
import csv
import json
import pandas as pd

urlFor2000 = 'https://opendata.arcgis.com/datasets/f88d947d0ba945b688e00a46d6cbcd6c_9.csv'
csv2000 = 'census_2000.csv'
urlFor2010 = 'https://opendata.arcgis.com/datasets/6969dd63c5cb4d6aa32f15effb8311f3_8.csv'
csv2010 = 'census_2010.csv'
clean2000 = open( 'census_2000_CLEAN.csv', 'w' )
clean2010 = open( 'census_2010_CLEAN.csv', 'w' )

def collectData():
   # Request 2000 data from API and save it into a csv file
   request = requests.get( urlFor2000 )
   outFile = open( csv2000, 'wt' )
   outFile.write( request.text )
   
   # Request 2010 data from API and save it into a csv file
   request = requests.get( urlFor2010 )
   outFile = open( csv2010, 'wt' )
   outFile.write( request.text )
   print( outFile )
   
def openFile( filename ):
    myData = pd.read_csv( filename , sep=',', encoding='latin1')
    return myData

def removeMissing( data ):
    # Remove rows with missing data and print them onto screen 
    # Display how many rows were dropped
    rowCount = data.shape[0]
    badRows = data[data.isna().any(axis=1)]
    data = data.dropna()
    rowCount = rowCount - data.shape[0]
    
    print( badRows )
    print( 'Number of rows dropped:', rowCount, '\n' )
    return data

def cleanData():
    # Opens the csv with data so it can be cleaned 
    data2000 = openFile( csv2000 )
    data2010 = openFile( csv2010 )
    
    # Call function to remove missing values
    print( 'Missing Data for 2000 Census data: ')
    data2000 = removeMissing( data2000 )
    print( 'Missing Data for 2010 Census data: ')
    data2010 = removeMissing( data2010 )
    
    # Write cleaned data to a new file
    clean2000.write( data2000.to_string() )
    clean2010.write( data2010.to_string() )
    
    
    

def main():
   collectData()
   cleanData()
        
if __name__== "__main__" :
    main()