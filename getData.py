import requests
import csv
import json
import pandas as pd

urlFor2000 = 'https://opendata.arcgis.com/datasets/f88d947d0ba945b688e00a46d6cbcd6c_9.csv'
csv2000 = 'census_2000.csv'
urlFor2010 = 'https://opendata.arcgis.com/datasets/6969dd63c5cb4d6aa32f15effb8311f3_8.csv'
csv2010 = 'census_2010.csv'


def main():
   request = requests.get( urlFor2000 )
   outFile = open( csv2000, 'wt' )
   outFile.write( request.text )
   
   request = requests.get( urlFor2010 )
   outFile = open( csv2010, 'wt' )
   outFile.write( request.text )
   print( outFile )

        
if __name__== "__main__" :
    main()