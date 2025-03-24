from django.contrib import admin
from .models import *
from django.db import transaction
import os
# Register your models here.
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ('name', 'status')
    
    @transaction.atomic
    def delete_queryset(self, request, queryset):
        for gallery in queryset:
            # Delete related HomeImage objects and their images
            for gallery_image in gallery.images.all():
                if gallery_image.image:
                    if os.path.isfile(gallery_image.image.path):
                        os.remove(gallery_image.image.path)
                gallery_image.delete()
            gallery.delete()

admin.site.site_header = "Radharavi Admin Panel"  # Change the admin panel header
admin.site.site_title = "Radharavi Site Admin"  # Change the browser tab title
admin.site.index_title = "Welcome to Radharavi Administration"  # Change the dashboard title