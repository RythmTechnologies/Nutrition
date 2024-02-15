from django.db import models
from apps.diet_app.mixin import TimeBasedStampModel

class Visit(TimeBasedStampModel):
    ip_address = models.CharField(max_length=15,blank=True)  # IPv4 adresleri için
    visit_count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.ip_address} - {self.visit_count}"