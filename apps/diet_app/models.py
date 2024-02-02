from django.db import models

from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Services Model ORM Start
class HomeSlider(TimeBasedStampModel):
  header = models.CharField(("Header"), max_length=50)
  content = RichTextField(("slider içerik"))
  photo = models.ImageField(("İçerik Resim"), upload_to="HomeCarousel")

  class Meta:
    verbose_name = 'Ana Sayfa Slider'
    verbose_name_plural = 'Ana Sayfa Slider'

  def __str__(self) -> str:
      return self.header
  
# Services Model ORM End

class TopContent(TimeBasedStampModel):
  content = RichTextField(("içerik"))
  photo = models.ImageField(("İçerik Resim"), upload_to="HomeCarousel")

  class Meta:
    verbose_name = 'Ana Sayfa Content '
    verbose_name_plural = 'Ana Sayfa Content'

  def __str__(self) -> str:
      return self.content
