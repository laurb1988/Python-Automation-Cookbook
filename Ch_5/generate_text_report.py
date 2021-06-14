from datetime import datetime

TEMPLATE = """
Movies Report
==============
DATE: {date}
Movies seen last 30 days: {num_movies}
Total minutes: {total_minutes}
"""

data = {'date': datetime.now(), 'num_movies': 3, 'total_minutes': 376,}
report = TEMPLATE.format(**data)
FILENAME_TEMPL = "{date}_report.txt"
filename = FILENAME_TEMPL.format(date = data['date'].strftime('%Y-%m-%d'))
print(filename)
with open(filename, 'w') as f:
    f.write(report)