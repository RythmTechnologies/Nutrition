from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel
from ckeditor.fields import RichTextField

# Services Model ORM Start
class Packages(TimeBasedStampModel):
    
    header = models.CharField(("Paket başlığı"), max_length=50)
    background_photo = models.ImageField(("Paket fotoğrafı"), upload_to="packages",blank=True)
    content = RichTextField(("Paket içeriği"))
    
    class Meta:
        verbose_name = 'hizmet paketleri'
        verbose_name_plural = 'hizmet paketleri'

    def __str__(self) -> str:
        return self.header
  
# Services Model ORM End

