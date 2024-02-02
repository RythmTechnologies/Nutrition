from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Services Model ORM Start
class Services(TimeBasedStampModel):
  title = models.CharField(("Başlık"), max_length=50)
  short_description = RichTextField(("Kısa Açıklama"))
  short_second_description = RichTextField(("Kısa İkinci Açıklama"))
  description = RichTextField(("İçerik Yazısı"))
  image = models.ImageField(("Banner Resim"), upload_to="services", height_field=None, width_field=None, max_length=None)
  content_image = models.ImageField(("İçerik Resim"), upload_to="services", height_field=None, width_field=None, max_length=None)
  slug = AutoSlugField(
        populate_from="title", editable=False, always_update=True, blank=True
    )


  class Meta:
    verbose_name = 'Hizmet'
    verbose_name_plural = 'Hizmetler'

  def __str__(self) -> str:
      return self.title