from django.contrib import admin
from .models import GraphicsCard, UpscalingTechnology

@admin.register(GraphicsCard)
class GraphicsCardAdmin(admin.ModelAdmin):
    list_display = ("name", "manufacturer", "memory_gb", "memory_type", "price", "benchmark_index")
    list_filter = ("manufacturer", "supported_technologies")
    search_fields = ("name",)

@admin.register(UpscalingTechnology)
class UpscalingTechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "version")
    search_fields = ("name", "version")
