from django.db import models

# Create your models here.
from django.db import models

# نموذج لإعدادات الموقع (اختياري)
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="site/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name
