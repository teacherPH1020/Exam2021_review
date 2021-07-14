from django import forms
from .models import Contact, Item



class Item_Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        labels = {"name":"food"}
        widgets = {'name' : forms.Textarea()}


def no_vowels(value):
    pass
   #raise forms.ValidationError("Vowels present")

class ContactForm(forms.ModelForm):
    age =  forms.IntegerField(label="how old")
    comment = forms.CharField(widget=forms.Textarea, validators=[no_vowels])
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            'name':'имя',
            'comment':'текст',
        }
        help_texts = {
            'email':'Обязательно в формате text@domain'
        }