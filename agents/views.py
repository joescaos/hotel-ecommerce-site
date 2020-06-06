from django.shortcuts import render

# Create your views here.
from .models import Agent

def agents_list(request):
    agents_list = Agent.objects.all()

    return render(request, 'agents.html', {
        'agents_list': agents_list,
    })

    

