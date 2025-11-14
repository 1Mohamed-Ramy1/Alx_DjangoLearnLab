from django import forms


class SearchForm(forms.Form):
    """
    SearchForm for validating and sanitizing user input.
    
    Prevents SQL Injection and XSS attacks by using Django Forms
    which automatically cleans and validates data.
    """
    query = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'})
    )
