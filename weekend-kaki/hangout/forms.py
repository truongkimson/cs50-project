from django import forms
from .models import Hangout
from django.contrib.auth.models import User


class HangoutViewForm(forms.ModelForm):
    class Meta:
        model = Hangout
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control',
                                                  'readonly': True}),
                   'location': forms.TextInput(attrs={'class': 'form-control',
                                                      'readonly': True}),
                   'date': forms.DateInput(attrs={'class': 'form-control',
                                                  'placeholder': 'DD/MM/YYYY'}),
                   'description': forms.Textarea(attrs={'class': 'form-control',
                                                        'rows': 3,
                                                        'readonly': True}),
                   'owner': forms.Select(attrs={'disabled': True}),
                   'participants': forms.SelectMultiple(attrs={'disabled': True})}


class HangoutModifyForm(forms.ModelForm):
    class Meta:
        model = Hangout
        exclude = ['owner']


class HangoutCreateForm(forms.ModelForm):
    class Meta:
        model = Hangout
        fields = '__all__'
        widgets = {'owner': forms.HiddenInput(),
                   'participants': forms.SelectMultiple(attrs={'class': 'ui fluid search dropdown'})}
