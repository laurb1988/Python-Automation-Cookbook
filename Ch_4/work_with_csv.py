import csv
file_name = 'top_films.csv'

with open('top_films.csv') as file:
    data = csv.reader(file)
    for row in data:
        print(row)


with open(file_name) as file:
    data = csv.DictReader(file)
    structured_data = [row for row in data]


print(structured_data[0])