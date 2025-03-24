from django.db import models
import os

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', null=True, blank=True)
    status = models.BooleanField('Status', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255, verbose_name='Caption', null=True, blank=True)
    verbose_name = 'Gallery Image'
    verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return f"Image for {self.gallery.name}"
    
    def delete(self, *args, **kwargs):
        # Delete image from filesystem
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)