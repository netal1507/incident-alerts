from django.contrib import admin
from .models import Incident, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "is_top",
        "created_at",
    )

    list_filter = ("status", "category", "is_top")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}

