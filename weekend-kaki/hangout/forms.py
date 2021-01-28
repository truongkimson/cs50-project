import unicodedata

from django import forms
from .models import Hangout
from django.contrib.auth.forms import AuthenticationForm
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
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'location': forms.TextInput(attrs={'class': 'form-control'}),
                   'date': forms.DateInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control',
                                                        'rows': 3}),
                   'owner': forms.HiddenInput(),
                   'participants': forms.SelectMultiple(attrs={'class': 'ui fluid search dropdown'})
                   }


class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'username',
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(
                widget=forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username',
                                               'autofocus': True},
                       )
    )

    password = forms.CharField(
                label='Password',
                strip=False,
                widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                                  'class': 'form-control',
                                                  'placeholder': 'Password'})
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
