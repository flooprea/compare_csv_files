import pandas as pd
import glob
import gzip
import shutil
import os



#path='C:\\Users\\florin.oprea\\Downloads\\etsy-feeds-before'
path='C:\\Users\\florin.oprea\\Downloads\\etsy-feeds-after'
rename=False

for fname in glob.glob(path+"\\*.gz"):
    if 'before' in fname:
        resultfile = fname.replace('.csv.gz','_before.csv')
    else:
        
        
    

