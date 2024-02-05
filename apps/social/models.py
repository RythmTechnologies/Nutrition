from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel


class SocialMedia(TimeBasedStampModel):
  name = models.CharField(("Sosyal Medya"), max_length=50)
  link = models.URLField(("Sosyal Medya Url'i"), max_length=200)

  class Meta:
    verbose_name = "Sosyal Medya"
    verbose_name_plural = "Sosyal Medyalar"

  def __str__(self) -> str:
      return self.name
