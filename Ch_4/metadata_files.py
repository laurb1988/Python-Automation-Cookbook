import os
from datetime import datetime

file_name = 'zen_of_python.txt'
stats = os.stat(file_name)
print(stats)
print("###############FILE_SIZE###############")
print(stats.st_size)
print("###############FILE_LAST_MODIFIED###############")
print(datetime.fromtimestamp(stats.st_mtime))
print("###############FILE_LAST_ACCESSED###############")
print(datetime.fromtimestamp(stats.st_atime))