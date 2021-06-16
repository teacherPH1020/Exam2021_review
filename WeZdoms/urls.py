"""WeZdoms URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rel import views

urlpatterns = [
    path('rel/', views.index, name='rel'),
    path('rel/form/', views.contact_form, name='rel_cform'),
    path('', TemplateView.as_view(template_name="home.html", extra_context ={'b':" "})),
    path('admin/', admin.site.urls),
]
