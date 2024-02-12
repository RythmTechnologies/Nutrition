from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel


class Seo(TimeBasedStampModel):
  meta_description = models.CharField(("Meta Açıklama"), max_length=155, blank=True, null=True)
  meta_keywords = models.CharField(("Meta Anahtar Kelimeler"), max_length=255, blank=True, null=True)

  def __str__(self) -> str:
      return self.meta_description

