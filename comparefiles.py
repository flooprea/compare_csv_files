import os
import pandas as pd
import time
from unzip import unzip_file, any_zip_file_in_directory
from common_code import print_timestamp, write_in_result_file

current_path = rf'{os.getcwd()}'
path_before = rf'{os.getcwd()}\files-before'
path_after = rf'{os.getcwd()}\files-after'
resultfile_path = rf'{current_path}\resultfile.txt'
zip_extension = '.gz'
zip_files_found = False

#print timestamp and start timer
print_timestamp(resultfile_path)
start_time = time.time()

print(rf'Checking files in {path_before}')
for file in os.listdir(path_before):
    #check if any file is zipped
    if not any_zip_file_in_directory(path_before, zip_extension):
        break
    else:
        #unzip file if it is zipped
        unzip_file(rf'{path_before}\{file}', zip_extension)

print(rf'Checking files in {path_after}')
for file in os.listdir(path_after):
        #check if any file is zipped
    if not any_zip_file_in_directory(path_after, zip_extension):
        break
    else:
        #unzip file if it is zipped
        unzip_file(rf'{path_after}\{file}', zip_extension)

#compare files
for file in os.listdir(path_after):
    file_path_after = rf'{path_after}\{file}'
    file_path_before = rf'{path_before}\{file}'
    file_name_before = file.replace('.csv', '_before.csv')

    #read CSVs
    dfafter = pd.read_csv(file_path_after, low_memory=False)
    dfbefore = pd.read_csv(file_path_before, low_memory=False)
    
    
    #compare and print result
    if dfafter.equals(dfbefore):
        out_string = f'Comparing {file} with {file_name_before} >>> Files are identical.'
        print(out_string)
    else:
        out_string = f'Comparing {file} with {file_name_before} >>> Files have differences!!!'
        print(out_string)

    #store output in result
    with open(rf'{current_path}\resultfile.txt', 'a') as f:
        f.write(f'{out_string}\n')

#print execution time
out_string = "Execution time: --- %s seconds --- \n" % round((time.time() - start_time), 2)
print(out_string)
with open(resultfile_path, 'a') as f:
    f.write(f'{out_string}')

    Password123#