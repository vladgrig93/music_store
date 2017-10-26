from django.shortcuts import render, HttpResponse, redirect
from ..login_app.models import *
def index(request): 
    records=Record.objects.all()
    artists=Artist.objects.all()
    context={'records': records, 'artists':artists}
    return render(request, 'users_app/user_portal.html', context)

def viewcart(request):
    return render(request, 'users_app/cart.html')

def category(request):
    category = request.POST['genre']
    request.session['genre']=request.POST['genre']
    display=Record.objects.filter(genre=request.POST['genre'])
    context={'display':display}
    return render(request, 'users_app/categories.html', context)

def artist(request):
    artist = request.POST['artist']
    request.session['artist']=request.POST['artist']
    display=Artist.objects.filter(name=request.POST['artist'])
    context={'display':display[0]}
    return render(request, 'users_app/artist.html', context)

def record(request):
    pass

def search(request):
    noartist = False
    norecord = False
    if request.POST['search'] == "":
        return render(request, "users_app/searchresults.html")
    records = Record.objects.filter(name__startswith=request.POST['search'])
    artists = Artist.objects.filter(name__startswith=request.POST['search'])
    if not records:
        norecord = True
    if not artists:
        noartist = True
    return render(request, "users_app/searchresults.html", {"records":records, "artists": artists, "header1":"Records:", "header2":"Artists:", "noartist":noartist,"norecord":norecord})

