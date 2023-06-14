from django.db import models

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=255)
    slug_field = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    # To remove extra 's' from model name in admin panel
    class Meta:
        verbose_name_plural = "Rooms"