from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'done']
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'done': 'Concluído'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
    
class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2"==True)