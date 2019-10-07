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


    data2010 = data2010.rename(columns={"P0010001": "Total Population", "P0010002": "Total Pop of 1 Race",
                             "P0010003": "Pop of 1 race: White", "P0010004": "Pop of 1 race: Black",
                             "P0010005": "Pop of 1 race: American Indian Alaskan",
                             "P0010006": "Pop of 1 race: Asian",
                             "P0010007": "Pop of 1 race: Native Hawaiian Pacific Islander",
                             "P0010008": "Pop of 1 race: Other Race", "OP000001": "Pop 2 or more races: Black and",
                             "OP000002": "Pop 2 or more races: American Indian Alaskan and",
                             "OP000003": "Pop 2 or more races: Asian and",
                             "OP000004": "Pop 2 or more races: Native Hawaiian Pacific Islander and",
                             "P0020002": "Total Hispanic Population",
                             "P0020005": "Total Non-Minority Population (White Not Hispanic)",
                             "P0020006": "Not Hispanic Pop of 1 race: Black",
                             "P0020007": "Not Hispanic Pop of 1 race: American Indian Alaskan",
                             "P0020008": "Not Hispanic Pop of 1 race: Asian",
                             "P0020009": "Not Hispanic Pop of 1 race: Native Hawaiian Pacific Islander",
                             "P0020010": "Not Hispanic Pop of 1 race: Other Race",
                             "OP00005": "Not Hispanic Pop 2 or more races: Black and",
                             "OP00006": "Not Hispanic Pop 2 or more races: American Indian Alaskan and",
                             "OP00007": "Not Hispanic Pop 2 or more races: Asian and",
                             "OP00008": "Not Hispanic Pop 2 or more races: Native Hawaiian Pacific Islander and",
                             "P0030001": "Total Pop 18+", "P0030003": "18+ Pop 1 race: White",
                             "P0030004": "18+ Pop 1 race: Black", "P0030005": "18+ Pop 1 race: American Indian Alaskan",
                             "P0030006": "18+ Pop 1 race: Asian", "P0030007": "18+ Pop 1 race: Native Hawaiian Pacific Islander",
                             "P0030008": "18+ Pop 1 race: Other race", "OP00009": "18+ Pop 2 or more races: Black and",
                             "OP00010": "18+ Pop 2 or more races: American Indian Alaskan and",
                             "OP00011": "18+ Pop 2 or more races: Asian and",
                             "OP00012": "18+ Pop 2 or more races: Native Hawaiian Pacific Islander",
                             "P0040002": "Hispanic 18+ Pop", "P0040005": "Non-Minority 18+ Pop (White Non-Hispanic)",
                             "P0040006": "Not Hispanic 18+ Pop 1 race: Black",
                             "P0040007": "Not Hispanic 18+ Pop 1 race: American Indian Alaskan",
                             "P0040008": "Not Hispanic 18+ Pop 1 race: Asian",
                             "P0040009": "Not Hispanic 18+ Pop 1 race: Native Hawaiian Pacific Islander",
                             "P0040010": "Not Hispanic 18+ Pop 1 race: Other race",
                             "OP000013": "Not Hispanic 18+ Pop 2 or more races: Black and",
                             "OP000014": "Not Hispanic 18+ Pop 2 or more races: American Indian Alaskan and",
                             "OP000015": "Not Hispanic 18+ Pop 2 or more races: Asian and",
                             "OP000016": "Not Hispanic 18+ Pop 2 or more races: Native Hawaiian Pacific Islander and",
                             "H0010001": "Total Housing Units",
                             "H0010002": "Occupied Housing Units",
                             "H0010003": "Vacant Housing Units"})
    
    # Write cleaned data to a new file
    data2000.to_csv( clean2000 )
    data2010.to_csv( clean2010 )
    
    
    

def main():
   collectData()
   cleanData()
        
if __name__== "__main__" :
    main()