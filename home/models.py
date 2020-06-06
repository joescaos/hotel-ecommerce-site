from django.db import models

# Create your models here.

class Services(models.Model):
    service_name = models.CharField(max_length=50)
    service_description = models.TextField()

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'