from jinja2 import Template
from datetime import datetime

with open('jinja_template.html') as f:
    template = Template(f.read())
    context = {
        'date': datetime.now(),
        'movies': ['Casablanca', 'The sound of music', 'Vertigo'],
        'total_minutes': 404,
    }

with open('report.html', 'w') as f:
    f.write(template.render(context))