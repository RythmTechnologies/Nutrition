from django.db import models
from ckeditor.fields import RichTextField
from apps.diet_app.mixin import TimeBasedStampModel, MyS3Storage

class AboutMe(TimeBasedStampModel):
    bio = RichTextField(("Hakkımda içerik"))
    image = models.ImageField(upload_to="about/",storage=MyS3Storage(), verbose_name="Profil Fotoğrafı")

    class Meta:
        verbose_name = "Hakkımda"
        verbose_name_plural = "Hakkımda"

    def __str__(self):
        return self.bio

class Sertifica(TimeBasedStampModel):
    header = models.CharField(("Sertifika Başlık"), max_length=50)
    content = RichTextField(("Sertifika İçerik"))
    sertifica_date = models.DateField(("Sertifika Alınma Tarihi"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Sertifika"
        verbose_name_plural = "Sertifika"

    def __str__(self):
        return self.header