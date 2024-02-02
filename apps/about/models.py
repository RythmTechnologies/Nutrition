from django.db import models
from ckeditor.fields import RichTextField
from apps.diet_app.mixin import TimeBasedStampModel

class AboutMe(TimeBasedStampModel):
    bio = RichTextField(("Hakkımda içerik"))
    image = models.ImageField(upload_to="about/", verbose_name="Profil Fotoğrafı")

    def __str__(self):
        return self.bio

    class Meta:
        verbose_name = "Hakkımda"
        verbose_name_plural = "Hakkımda"

class Sertifica(TimeBasedStampModel):
    header = models.CharField(("sertifika başlık"), max_length=50)
    content = RichTextField(("sertifika içerik"))

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Sertifika"
        verbose_name_plural = "Sertifika"
