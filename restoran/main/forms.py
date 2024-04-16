from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def get_user(self):
        pass


class LoginForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TableBookingForm(forms.Form):
    email = forms.EmailField(label='Email')
    table_number = forms.IntegerField(label='Номер столика')
    date = forms.DateField(label='День')
    time = forms.TimeField(label='Час')


class CommentsForm(forms.Form):
    email = forms.EmailField(widget=forms.HiddenInput())
    text = forms.CharField(label='Відгук')
