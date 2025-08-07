from django import forms
from .models import Task

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