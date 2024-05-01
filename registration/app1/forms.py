from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'price']

