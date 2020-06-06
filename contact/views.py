from django.shortcuts import render, redirect
from django.core.mail import send_mail as sm, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import ContactDetails

from .forms import ContactForm



def send_mail(request):
    contactdetails = ContactDetails.objects.last()
    template_name = 'contact.html'
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']

            try:
                sm(subject, message, from_email, ['test@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header')

            return redirect('contact:success')

    else:
        contact_form = ContactForm()

    context = {
        'contactdetails': contactdetails,
        'contact_form': contact_form,
    }

    return render(request, template_name, context)

def success(request):
    return HttpResponse('Message sent successfully')