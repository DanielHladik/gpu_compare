from django.db import models

class UpscalingTechnology(models.Model):
    name = models.CharField(max_length=20)
    version = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} {self.version}"

class GraphicsCard(models.Model):
    MANUFACTURER_CHOICES = [
        ('NVIDIA', 'NVIDIA'),
        ('AMD', 'AMD'),
        ('Intel', 'Intel'),
    ]

    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=10, choices=MANUFACTURER_CHOICES)
    memory_gb = models.PositiveIntegerField()
    memory_type = models.CharField(max_length=20)
    supported_technologies = models.ManyToManyField(UpscalingTechnology, blank=True, related_name='supported_cards')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benchmark_index = models.PositiveIntegerField()
    cuda_cores = models.PositiveIntegerField(null=True, blank=True)
    tdp = models.PositiveIntegerField(null=True, blank=True)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    bus = models.CharField(max_length=50, null=True, blank=True)
    process = models.CharField(max_length=50, null=True, blank=True)
    base_clock = models.PositiveIntegerField(null=True, blank=True)
    boost_clock = models.PositiveIntegerField(null=True, blank=True)
    directx = models.CharField(max_length=20, null=True, blank=True)
    opengl = models.CharField(max_length=20, null=True, blank=True)
    opencl = models.CharField(max_length=20, null=True, blank=True)
    vulkan = models.CharField(max_length=20, null=True, blank=True)
    shader_model = models.CharField(max_length=20, null=True, blank=True)
    pixel_rate = models.CharField(max_length=50, null=True, blank=True)
    texture_rate = models.CharField(max_length=50, null=True, blank=True)
    rops = models.PositiveIntegerField(null=True, blank=True)
    tmus = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
