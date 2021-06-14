import mistune
from datetime import datetime

with open('markdown_template.md') as f:
    template = f.read()
    context = {
        'date': datetime.now(),
        'pmovies': ['Casablanca', 'The sound of music', 'Vertigo'],
        'total_minutes': 404,
    }
    context['num_movies'] = len(context['pmovies'])
    context['movies'] = '\n'.join('* {}'.format(movie) for movie in context['pmovies'])
    md_report = template.format(**context)
    report = mistune.markdown(md_report)

with open('report.html', 'w') as f:
    f.write(report)