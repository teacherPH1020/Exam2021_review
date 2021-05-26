from django.shortcuts import render

from .view import add
from django.http import HttpResponse


# Create your view here.
def index(request):
    a=3
    b=4
    c = add.add_2(a,b)
    return HttpResponse(str(c))