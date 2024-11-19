from django.db import models
from django.utils.timezone import now

class Component(models.Model):
    name = models.CharField(max_length=100)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Component"
        verbose_name_plural = "Components"
        ordering = ['name']  # Orders components alphabetically by name

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        ordering = ['name']  # Orders vehicles alphabetically by name

    def __str__(self):
        return f"{self.name} ({self.registration_number})"


class Issue(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    class Meta:
        verbose_name = "Issue"
        verbose_name_plural = "Issues"
        ordering = ['vehicle', 'component']  # Orders issues by vehicle, then by component

    def __str__(self):
        return f"Issue for {self.vehicle.name} - {self.component.name}"
