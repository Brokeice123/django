from django.shortcuts import render


def contact(request):
    return render(request, 'Contact.html')


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def donate(request):
    return render(request, 'donate.html')


def index(request):
    return render(request, 'index.html')
