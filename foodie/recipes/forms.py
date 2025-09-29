from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Search recipes',
            'class': 'form-control me-2'  # Bootstrap class for styling
        })
    )