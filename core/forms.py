from django import forms
from .models import Contact, Subscriber

class ContactForm(forms.ModelForm):
    subscribe = forms.BooleanField(required=False, label="Newsletter abonnieren?")

    class Meta:
        model = Contact
        fields = ['email', 'name', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Deine E-Mail'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dein Name'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deine Nachricht', 'rows': 5}),
        }