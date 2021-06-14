import csv
#CREATE NEW CSV FILE
HEADER = ['Administration', 'Name', 'Year']
DATA = [(225.7, 'Gone with the wind', 1939),
        (194.4, 'Star Wars', 1977),
        (161.0, 'ET: The Extraterrestrial', 1982)]

with open('movies.csv', 'w', newline='') as csvfile:
    movies = csv.writer(csvfile)
    movies.writerow(HEADER)
    for row in DATA:
        movies.writerow(row)

#UPDATE CSV FILES
FILENAME = 'movies.csv'
with open(FILENAME, 'r', newline='') as file:
    data = [row for row in csv.DictReader(file)]
    data[1]['Year'] = 1977
    HEADER = data[0].keys()
with open(FILENAME, 'w', newline='') as file:     
    writer = csv.DictWriter(file, fieldnames=HEADER)
    writer.writeheader()
    writer.writerows(data)