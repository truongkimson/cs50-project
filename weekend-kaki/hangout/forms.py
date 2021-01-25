from django import forms
from .models import Hangout
from django.contrib.auth.models import User


class HangoutViewForm(forms.ModelForm):
    class Meta:
        model = Hangout
        fields = '__all__'
        widgets = {'owner': forms.Select(attrs={'disabled': True}),
                   'participants': forms.SelectMultiple(attrs={'disabled': True})}


class HangoutModifyForm(forms.ModelForm):
    class Meta:
        model = Hangout
        exclude = ['owner']


class HangoutCreateForm(forms.ModelForm):
    class Meta:
        model = Hangout
        fields = '__all__'
        widgets = {'owner': forms.HiddenInput()}
