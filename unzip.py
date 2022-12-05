import gzip
import shutil
import os
import glob
from common_code import write_in_result_file
#from comparefiles import resultfile_path

current_path = rf'{os.getcwd()}'
resultfile_path = rf'{current_path}\resultfile.txt'

def unzip_file(file, zip_extension):

    if is_zipped(file, zip_extension):
        write_in_result_file(resultfile_path, rf'File {file} is compressed, unzipping...')

        resultfile = file.replace('.gz', '')
        with gzip.open(file, 'rb') as f_in:
            with open(resultfile, 'wb') as f_out:
                    print('Unzipping file '+file)
                    shutil.copyfileobj(f_in, f_out)
        os.remove(file) 
    else:
        print(f'{file} is not compressed')  

    return file

def is_zipped(file, zip_extension):
    if zip_extension in file:
        return True
    else:
        return False


def any_zip_file_in_directory(directory, extension):
    if glob.glob(rf'{directory}\*.gz'):
        return True
    else:
        print(f'No more compressed files found in directory {directory}')
        write_in_result_file(resultfile_path, rf'No compressed files found in directory {directory}')
        return False
