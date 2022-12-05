import os

def rename_files(path, rename_substring, extension):
    for file in os.listdir(path):
        if rename_substring not in file:
            resultfile = file.replace(extension, f'_before{extension}')
            os.rename(rf'{path}\{file}', f'{path}\{resultfile}')


def is_before(file, before_substring):
    if before_substring in file:
        return True
    else:
        return False