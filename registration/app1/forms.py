from django import forms
from .models import Pet

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'price']

