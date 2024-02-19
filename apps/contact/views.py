from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from dietetic import settings
from django.core.mail import EmailMessage
import os

STATIC_URL = 'staticfiles/static/'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact=form.save()
            if contact.appointment_date and contact.appointment_time and contact.appointment_type:
                 body = f'''
                    <html>
                        <head></head>
                        <body>
                                <p>Merhaba {contact.name},</p>
                                <p>Randevunuz başarıyla alınmıştır.</p>
                                <p>Randevunuz {contact.appointment_date} tarihinde {contact.appointment_time} saatinde {contact.appointment_type} olacaktır.</p>
                                <p>Sorularınız veya ek bilgi ihtiyacınız olursa, lütfen bizimle iletişime geçmekten çekinmeyin.</p>
                                <p>Teşekkürler,<br>Diyetisyen Seda Nur Çıray</p>
                        </body>
                    </html>
                    '''
            body = f'''
                <html>
                    <head></head>
                    <body>
                        <p>Merhaba {contact.name},</p>
                        <p>İletişim formunuz iletildi.Sizinle Telefon numaranız üzerinden iletişime geçilecektir.</p>
                        <p>Sorularınız veya ek bilgi ihtiyacınız olursa, lütfen bizimle tekrar iletişime geçmekten çekinmeyin.</p>
                        <p>Teşekkürler,<br>Diyetisyen Seda Nur Çıray</p>
                    </body>
                </html>
            '''

            # kullanıcıya mail
            email = EmailMessage(
                subject='Mesajınız Alındı',
                body=body,
                from_email=settings.EMAIL_HOST_USER,
                to=[contact.email]
                    )
            email.content_subtype = "html"
            attachment_path = os.path.join(STATIC_URL, 'logo/logo-seda.webp')
            if attachment_path:
                email.attach_file(attachment_path)
            email.send()

            # admine mail
            email_to_admin = EmailMessage(
                subject=f'Yeni İletişim Formu Mesajı: {contact.name}',
                body=f'Mesaj: {contact.message}\nE-posta: {contact.email}\nTarih: {contact.appointment_date}\nSaat: {contact.appointment_time}\nRandevu Türü: {contact.appointment_type}',
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER]  # Yönetici e-posta adresi
            )

            email_to_admin.send()


            messages.success(request, 'Mesajınız başarıyla gönderildi.')
            return redirect('iletisim')
        else:
            messages.error(request, 'Formu gönderirken bir hata oluştu. Lütfen tekrar deneyin.')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})