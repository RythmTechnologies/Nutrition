from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from dietetic import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact=form.save()
            send_mail(
                subject='Mesajınız Alındı',
                message='Mesajınızı aldık, en kısa sürede size dönüş yapacağız.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[contact.email],  # formdan alınan kullanıcı e-postası
                fail_silently=False,
            )
            send_mail(
                subject=f'Yeni İletişim Formu Mesajı: {contact.name}',
                message=f'Mesaj: {contact.message}\nE-posta: {contact.email},{contact.appointment_date},{contact.appointment_time},{contact.appointment_type}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # Yönetici e-posta adresi
                fail_silently=False,
            )
            
           
            messages.success(request, 'Mesajınız başarıyla gönderildi.')
            return redirect('iletisim')  
        else:
            messages.error(request, 'Formu gönderirken bir hata oluştu. Lütfen tekrar deneyin.')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})