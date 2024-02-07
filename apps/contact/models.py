from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad")
    email = models.EmailField(verbose_name="E-posta")
    phone =  PhoneNumberField(region='TR',blank=True,null=True)
    message = models.TextField(verbose_name="Mesaj")
    appointment_date = models.DateField(verbose_name="Randevu Tarihi")
    appointment_time = models.TimeField(verbose_name="Randevu Saati")
    appointment_type = models.CharField(max_length=50, verbose_name="Randevu Türü", choices=[
        ('online', 'Online'),
        ('yüz yüze', 'Yüz Yüze'),
    ])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderilme Tarihi")
    

    def __str__(self):
        return f"{self.name} - {self.email} - {self.appointment_date} - {self.appointment_time} "
    class Meta:
        verbose_name = "iletişim"
        verbose_name_plural = "iletişim"