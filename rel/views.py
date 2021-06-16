from django.shortcuts import render, redirect

from .view import add
from django.http import HttpResponse
from .forms import ContactForm

#from django.http import request as Request

# Create your view here.
def index(request):
    #print(dir(Request))
    #print(request.META)
    a=3
    b=4
    c = add.add_2(a,b)
    print(request.user)
    return HttpResponse(str(c))

def contact_form(request):
    if request.method == 'POST':
        print("AGE=", request.POST.get('age'))
        cform = ContactForm(request.POST)
        if cform.is_valid():
            print("age=", cform.cleaned_data["age"])
            cform.save()
            return HttpResponse('<h1>Thank you!</h1>')

    else:
        cform = ContactForm()
    return render(request,"cform.html",{'cform':cform})

