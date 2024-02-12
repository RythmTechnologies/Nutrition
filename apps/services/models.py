from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel, MyS3Storage
from autoslug import AutoSlugField

# Services Model ORM Start
class Services(TimeBasedStampModel):
  title = models.CharField(("Başlık"), max_length=50)
  description = models.TextField(("İçerik Yazısı"),max_length=150)
  image = models.ImageField(("Banner Resim"), upload_to="services",storage = MyS3Storage(), height_field=None, width_field=None, max_length=None)

  def __str__(self) -> str:
      return self.title

  class Meta:
    verbose_name = 'Hizmet'
    verbose_name_plural = 'Hizmetler'
