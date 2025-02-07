from django import forms
from .models import Livro, Exemplar, User
from django.contrib.auth.forms import BaseUserCreationForm

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"

class ExemplarForm(forms.ModelForm):
    class Meta:
        model = Exemplar
        fields = "__all__"