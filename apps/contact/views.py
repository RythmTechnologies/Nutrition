from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız başarıyla gönderildi.')
            return redirect('iletisim')  
        else:
            messages.error(request, 'Formu gönderirken bir hata oluştu. Lütfen tekrar deneyin.')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})