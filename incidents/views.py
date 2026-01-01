from django.shortcuts import render, get_object_or_404
from .models import Incident, Category
#from .youtube import fetch_latest_videos
from .youtube import fetch_shorts

def home(request):
    top_incidents = Incident.objects.filter(
        is_published=True
    ).order_by("-created_at")

    categories = Category.objects.all()
    #youtube_videos = fetch_latest_videos()
    youtube_videos = fetch_shorts(max_results=10)  # fetch Shorts

    return render(request, "incidents/home.html", {
        "top_incidents": top_incidents,
        "categories": categories,
        "youtube_videos": youtube_videos,
        #"shorts_videos": shorts_videos,
    })


def category_incidents(request, slug):
    category = get_object_or_404(Category, slug=slug)
    incidents = category.incidents.filter(is_published=True)

    return render(request, "incidents/category.html", {
        "category": category,
        "incidents": incidents
    })


def incident_detail(request, slug):
    incident = get_object_or_404(Incident, slug=slug, is_published=True)
    return render(request, "incidents/detail.html", {
        "incident": incident
    })
