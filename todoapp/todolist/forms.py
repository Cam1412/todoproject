from django import forms
from django.forms import ModelForm
from .models import tache


class TacheForm(forms.ModelForm):
    class Meta:
        model = tache
        fields = ['titre', 'description','date_echeance', 'status']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la tâche'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                'rows': 4,
                'placeholder': 'Notes complémentaires'}),
            'date_echeance': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
  