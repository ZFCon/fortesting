from dal import autocomplete

from django import forms

from .models import *

from django.contrib.auth.models import User


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('__all__')
        widgets = {
            'user': autocomplete.ModelSelect2(url='user', attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 1})
                }
