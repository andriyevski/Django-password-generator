from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    # all str alphabet
    strLower = list(string.ascii_lowercase)

    # all numbers
    number = list(string.digits)

    # upper character
    if request.GET.get('uppercase'):
        strLower.extend(list(string.ascii_uppercase))

    if request.GET.get('numbers'):
        strLower.extend(list(number))

    if request.GET.get('special'):
        strLower.extend(list(string.punctuation))

    # lenght of password
    length = int(request.GET.get('length', 8))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(strLower)

    print("User pick password: {}".format(thepassword))
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
       ip = x_forwarded_for.split(',')[-1].strip()
    else:
       ip = request.META.get('REMOTE_ADDR')

    return render(request, 'generator/about.html', {'ip':ip})