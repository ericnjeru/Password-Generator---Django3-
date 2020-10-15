from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    choice = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    if request.GET.get('uppercase'):
        choice.extend(list('ABCDEFGHJIKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        choice.extend(list('!@#$%^&*(){}?/'))
    if request.GET.get('numbers'):
        choice.extend(list('123456789'))

    length = int(request.GET.get('length'))
    for x in range(length):
        thepassword += random.choice(choice)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
