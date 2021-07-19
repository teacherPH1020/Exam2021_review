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

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
