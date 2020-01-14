from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Juana Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via Láctea',
        'user': 'Pedro Perez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Manuel Goncalves',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
    }
]


def list_posts(request):
    """ Listo existing posts."""
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br/>'.join(content))
