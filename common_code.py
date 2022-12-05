import datetime

def print_timestamp(file_path):
    with open(rf'{file_path}', 'a') as f:
        f.write(f'\nDate running: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n')

def write_in_result_file(file_path, string):
    with open(rf'{file_path}', 'a') as f:
        f.write(f'{string}\n')