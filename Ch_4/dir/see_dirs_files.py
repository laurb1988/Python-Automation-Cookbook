import os, re
for root, dirs, files in os.walk('.'):
    for file in files:
        print(file)

print('###################################################')

for root, dirs, files in os.walk('.'):
    for file in files:
        full_file_path = os.path.join(root, file)
        print(full_file_path)


print('Print PDF FILES')

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.pdf'):
            full_file_path = os.path.join(root, file)
            print(full_file_path)

print('Print only files with numbers')
for root, dirs, files in os.walk('.'):
    for file in files:
        if re.search(r'[0-9]', file):
            full_file_path = os.path.join(root, file)
            print(full_file_path)