from django.shortcuts import render

from .models import Property, Category
from .forms import ReserveForm
from django.db.models import Q

def property_list(request):
    property_list = Property.objects.all()
    template = 'list.html'

    address_query = request.GET.get('q')
    property_type= request.GET.getlist('property_type', None)
    if address_query and property_type:
        print(address_query)
        print(property_type)
        property_list = property_list.filter(
            Q(location__icontains = address_query) &
            Q(property_type__icontains = property_type[0]) 
        ).distinct()

    context = {
        'property_list': property_list,
    }

    return render(request, template, context)

def property_detail(request, id):
    property_detail = Property.objects.get(id=id)

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReserveForm()

    return render(request, 'detail.html', {
        'property_detail': property_detail,
        'reserve_form': reserve_form
    })


