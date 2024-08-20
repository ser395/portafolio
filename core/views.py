from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
html_menu = '''
    <h1>Mi Portfolio</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about-me/">About</a></li>
            <li><a href="/portfolio/">Portfolio</a></li>
            <li><a href="/contact/">Contact</a></li>
        
        </ul>
    </nav>
'''

def home(request):
    return HttpResponse(html_menu+"<h3>Pagina principal</h3>")

def about(request):
    return HttpResponse(html_menu+"<h3>Acerca de...</h3><h3>Me llamo Ser395 y son Programador</h3>")

def portfolio(request):
    return HttpResponse('<h1>Mi Portfolio Personal</h1><h3>Mi Portfolio</p>Mi listado de trabajos realizados</p>')
                        