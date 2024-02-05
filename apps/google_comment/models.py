from django.db import models
from django.core.validators import MaxValueValidator
from ckeditor.fields import RichTextField
from apps.diet_app.mixin import TimeBasedStampModel


class GoogleComment(TimeBasedStampModel):
  comment_author = models.CharField(("Yorumu Yapan Kişi"), max_length=50)
  comment_star = models.PositiveIntegerField(("Yorum Yıldızı"), validators = [MaxValueValidator(5)])
  comment_point = models.DecimalField(("Yorum Puanı"), max_digits=2, decimal_places=1, default = 4.9)
  comment_content = RichTextField(("Yorum İçeriği"))
  comment_date = models.DateField(("Yorum Yapılma Tarihi"), auto_now=False, auto_now_add=False)

  class Meta:
    verbose_name = "Google Yorum"
    verbose_name_plural = "Google Yorumları"

  def __str__(self) -> str:
      return self.comment_author
