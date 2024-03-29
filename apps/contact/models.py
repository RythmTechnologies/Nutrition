from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.diet_app.mixin import TimeBasedStampModel


class Contact(TimeBasedStampModel):
    name = models.CharField(max_length=100, verbose_name="Ad")
    email = models.EmailField(verbose_name="E-posta")
    phone =  PhoneNumberField(region='TR')
    message = models.TextField(verbose_name="Mesaj")
    appointment_date = models.DateField(verbose_name="Randevu Tarihi",null=True,blank=True)
    appointment_time = models.TimeField(verbose_name="Randevu Saati",null=True,blank=True)
    appointment_type = models.CharField(max_length=50, verbose_name="Randevu Türü", choices=[
        ('online', 'Online'),
        ('yüz yüze', 'Yüz Yüze'),
    ],null=True,blank=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.appointment_date} - {self.appointment_time} "
    class Meta:
        verbose_name = "iletişim"
        verbose_name_plural = "iletişim"