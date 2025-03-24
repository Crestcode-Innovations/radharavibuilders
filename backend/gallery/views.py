from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets
from .models import *
# Create your views here.


class Galleryviews(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    