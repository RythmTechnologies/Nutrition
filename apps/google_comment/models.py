from django.db import models
from django.core.validators import MaxValueValidator
from ckeditor.fields import RichTextField
from apps.diet_app.mixin import TimeBasedStampModel
from django.core.exceptions import ValidationError

class GoogleComment(TimeBasedStampModel):
  comment_author = models.CharField(("Yorumu Yapan Kişi"), max_length=50)
  comment_star = models.PositiveIntegerField(("Yorum Yıldızı"), default=5,validators = [MaxValueValidator(5)])
  comment_point = models.DecimalField(("Yorum Puanı"), max_digits=2, decimal_places=1, default = 4.9)
  comment_content = RichTextField(("Yorum İçeriği"))
  comment_date = models.DateField(("Yorum Yapılma Tarihi"), auto_now=False, auto_now_add=False)
  
  @property
  def stars_display(self):
      full_stars = '★' * self.comment_star
      empty_stars = '☆' * (5 - self.comment_star)
      return full_stars + empty_stars
  @property
  def stars_count(self):

      return float(self.comment_point)    
  def clean(self):
      if self.comment_point > float(self.comment_star):
          raise ValidationError({'comment_point': 'Yorum puanı, yorum yıldız sayısından büyük olamaz.'})

  def save(self, *args, **kwargs):
      self.clean()
      super(GoogleComment, self).save(*args, **kwargs)

  class Meta:
    verbose_name = "Google Yorum"
    verbose_name_plural = "Google Yorumları"

  def __str__(self) -> str:
      return self.comment_author
  
