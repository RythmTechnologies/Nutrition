from django.db import models

from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel,MyS3Storage
from ckeditor.fields import RichTextField

class TopContent(TimeBasedStampModel):
  content = RichTextField(("içerik"))
  photo = models.ImageField(("İçerik Resim"),storage=MyS3Storage(), upload_to="HomeCarousel")

  class Meta:
    verbose_name = 'Ana Sayfa Content '
    verbose_name_plural = 'Ana Sayfa Content'

  def __str__(self) -> str:
      return self.content
