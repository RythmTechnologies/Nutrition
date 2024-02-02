from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad")
    email = models.EmailField(verbose_name="E-posta")
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderilme Tarihi")

    def __str__(self):
        return f"{self.name} - {self.email}"
    class Meta:
        verbose_name = "iletişim"
        verbose_name_plural = "iletişim"