from django.shortcuts import render, get_object_or_404
from .models import GalleryImage, Gallery


def gallery_list(request):
    galleries = Gallery.objects.get_active_galleries()
    context = {
        "galleries": galleries
    }

    return render(request, "gallery_list.html", context)


def gallery_detail(request, pk, slug):
    gallery = get_object_or_404(Gallery, id=pk, slug=slug)
    gallery_images = GalleryImage.objects.filter(gallery=gallery)

    context = {
        "gallery": gallery,
        "gallery_images": gallery_images
    }

    return render(request, "gallery_detail.html", context)
