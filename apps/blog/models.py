from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel,MyS3Storage
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Category(TimeBasedStampModel):
  name = models.CharField(("Kategori Adı"), max_length=50)

  class Meta:
    verbose_name = "Kategori"
    verbose_name_plural = "Kategoriler"

  def __str__(self) -> str:
    return self.name

class Label(TimeBasedStampModel):
  name = models.CharField(("Etiket Seo İçin"), max_length=50)

  class Meta:
    verbose_name = "Etiket"
    verbose_name_plural = "Etiketler"


  def __str__(self) -> str:
    return self.name


class Blog(TimeBasedStampModel):
  author = models.ForeignKey(User, verbose_name=("Blog Yazısını Giren"), on_delete=models.CASCADE)
  title = models.CharField(("Blog Başlık"), max_length=50)
  short_content = models.CharField(("Blog Kısa Başlık"), max_length=120)
  description = HTMLField(("Blog İçerik"))
  image = models.ImageField(("Blog Resim"), upload_to="blog/",storage=MyS3Storage(), height_field=None, width_field=None, max_length=None)
  category = models.ForeignKey(Category, verbose_name=("Blog Kategori"), on_delete=models.CASCADE)
  label = models.ManyToManyField(Label, verbose_name=("Blog Etiket"))
  slug = AutoSlugField(
        populate_from="title", editable=False, always_update=True, blank=True
    )

  class Meta:
    verbose_name = "Blog"
    verbose_name_plural = "Bloglar"

  def __str__(self) -> str:
    return self.title




