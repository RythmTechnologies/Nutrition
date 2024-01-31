from django.db import models

class AboutMe(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    bio = models.TextField(verbose_name="Hakkımda")
    email = models.EmailField(verbose_name="E-posta")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    image = models.ImageField(upload_to="about/images/", verbose_name="Profil Fotoğrafı")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Hakkımda"
        verbose_name_plural = "Hakkımda"