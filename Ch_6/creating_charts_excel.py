import openpyxl
from openpyxl.chart import BarChart, Reference

xlsfile = openpyxl.Workbook()
data = [('Name', 'Addmission'),
        ('Gone with the wind', 225.7),
        ('Star Wars', 94.4),
        ('ET: The Extraterrestrial', 161.0)]
sheet = xlsfile['Sheet']
for row in data:
    sheet.append(row)

chart = BarChart()
chart.title = 'Addmission per movie'
chart.y_axis.title = 'Millions'
data = Reference(sheet, min_row=2, max_row=4, min_col=1, max_col=2)
chart.add_data(data, from_rows=True, titles_from_data=True)
sheet.add_chart(chart, 'A6')
xlsfile.save('movie_chart.xlsx')