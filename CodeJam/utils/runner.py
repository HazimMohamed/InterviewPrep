import sys
import os
import time

file = sys.argv[1]
parent_dir = os.path.split(file)[0]
input_dir = os.path.join(parent_dir, 'input')
output_dir = os.path.join(parent_dir, 'output')


def get_mod_time(file_path):
    return os.stat(file_path).st_mtime


input_files = list(map(lambda a: os.path.join(input_dir, a), os.listdir(input_dir)))
if len(input_files) == 0:
    print('No input files found.')
    exit(1)

input_files.sort(key=get_mod_time, reverse=True)
input_file_full = input_files[0]
input_file_tail = os.path.split(input_file_full)[1]
output_file_full = os.path.join(output_dir, input_file_tail + '-output-' + str(time.time()))

syscall = 'cat "{}" | python3 "{}" > "{}"'.format(input_file_full, file, output_file_full)
os.system(syscall)
