from django.shortcuts import render, redirect

from .view import add
from django.http import HttpResponse
from .forms import ContactForm
import json

from django.views import View
from django.views.generic.edit import CreateView
from .models import Item
from .forms import Item_Form
from django.urls import reverse_lazy

class ItemCreation(CreateView):
    model = Item
    form_class = Item_Form
    #success_url = reverse_lazy("item:index")

class Paint(View):
    color = "Color"

    def get(self, request):
        return HttpResponse(json.dumps({f'{self.color}':f'{str(request.method)}'}))

class Red(Paint):
    color = "Red"

class Blue(Paint):
    color = "Blue"

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

