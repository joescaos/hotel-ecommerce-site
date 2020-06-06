from django.shortcuts import render

# Create your views here.

from .models import About

def about_us(request):
    about_us = About.objects.last()

    return render(request, 'about.html', {
        'about_us': about_us,
        }
    )
