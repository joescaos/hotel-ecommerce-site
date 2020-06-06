from django.shortcuts import render

from property.models import Property, Category
from agents.models import Agent
from django.db.models import Count

# Create your views here.
def home(request):
    category_list = Category.objects.annotate(property_count=Count('property')).values('category_name',
    'property_count', 'image')
    print(category_list)
    property_list = Property.objects.all()
    agents_list = Agent.objects.all()
    
    return render(request, 'home.html', {
        'category_list_home': category_list,
        'property_list_home': property_list,
        'agents_list_home': agents_list,
    })