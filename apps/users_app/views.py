from django.shortcuts import render, HttpResponse, redirect
from ..login_app.models import *
def index(request):
    Record.objects.create(name='Steal this album', rec_image='sdfas', price=20, genre='Rock', artist='System of a Down', description='fireee')
    Record.objects.create(name='Greatest Hits', rec_image='', price=20, genre='Rap', artist='Tupac', description="Tupac's greatest hits!")
    Record.objects.create(name='Jazz hits', rec_image='', price=20, genre='Jazz', artist='various', description="Mix of jazz songs")
    Record.objects.create(name='Dreams', rec_image='', price=20, genre='EDM', artist='Zhu', description="Zhu's latest album, very chill")
    Record.objects.create(name='Riding with the king', rec_image='', price=20, genre='Blues', artist='Eric Clapton', description="dope classics")    
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

'''
    $('#category-form').submit(function(e){
        e.preventDefault();
        var genre = $('#genre').val()
        $.ajax({
            url: '/user/category/' + genre,
            method: 'GET',
            success: function(res){
                $('#display-div').html(res)
            }
        })
    })
'''