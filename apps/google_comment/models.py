from django.db import models
from django.core.validators import MaxValueValidator
from tinymce.models import HTMLField
from apps.diet_app.mixin import TimeBasedStampModel

class GoogleComment(TimeBasedStampModel):
  comment_author = models.CharField(("Yorumu Yapan Kişi"), max_length=50)
  comment_star = models.PositiveIntegerField(("Yorum Yıldızı"), default=5,validators = [MaxValueValidator(5)])
  comment_content = HTMLField(("Yorum İçeriği"))
  comment_date = models.DateField(("Yorum Yapılma Tarihi"), auto_now=False, auto_now_add=False)

  @property
  def stars_display(self):
      full_stars = '★' * self.comment_star
      empty_stars = '☆' * (5 - self.comment_star)
      return full_stars + empty_stars
  @property
  def stars_count(self):
      return float(self.comment_star)

  def save(self, *args, **kwargs):
      self.clean()
      super(GoogleComment, self).save(*args, **kwargs)

  class Meta:
    verbose_name = "Google Yorum"
    verbose_name_plural = "Google Yorumları"

  def __str__(self) -> str:
      return self.comment_author

