from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınızı giriniz...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta adresinizi giriniz...'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınızı buraya yazınız...', 'rows': 4}),
        }