from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone','message', 'appointment_date', 'appointment_time', 'appointment_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Adınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'emailiniz'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon Numaranız '}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'mesajınız'}),
            
            'appointment_date': forms.DateInput(attrs={'class': 'form-control flatpickr-date','placeholder': 'Seçiniz.'}),
            'appointment_time': forms.TimeInput(attrs={'class': 'form-control flatpickr-time','placeholder': 'Seçiniz.'}),
            'appointment_type': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
       
        self.fields['appointment_type'].initial = 'yüz yüze'
