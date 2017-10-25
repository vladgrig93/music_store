from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages 

def index(request):
    return render(request, 'admin_app/admin_portal.html')

def addrecord(request):
    return render(request, 'admin_app/addrecord.html')

def proccess_record(request):
    if len(request.POST['name']) < 1:
        messages.error(request, "Please enter title of the record")
        return redirect('/admin/addrecord')
    if len(request.POST['artist']) < 1:
        messages.error(request, "Please enter artist of the record")
        return redirect('/admin/addrecord')
    if len(request.POST['genre']) < 1:
        messages.error(request, "Please enter genre of the record")
        return redirect('/admin/addrecord')
    if len(request.POST['price']) < 1:
        messages.error(request, "Please enter price of the record")
        return redirect('/admin/addrecord')
    if len(request.POST['description']) < 10:
        messages.error(request, "Please a description of the record longer than 10 characters")
        return redirect('/admin/addrecord')
    else:
        return redirect('admin_portal')
    # Record.objects.create(name=request.POST['name'], artitst=request.POST['artits'], genere=request.POST['genre'], price=request.POST['price'], description=request.POST['description'])
    # return redirect('/admin/admin_portal')

def record_page(request, record_id):
    return render(request, 'admin_app/record_page.html')