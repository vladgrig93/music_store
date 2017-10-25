from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'admin_app/admin_portal.html')