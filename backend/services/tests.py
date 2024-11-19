from django.test import TestCase
from .models import Component, Vehicle, Issue
from decimal import Decimal
from datetime import datetime, timedelta

from rest_framework.test import APIClient
from rest_framework import status

class ComponentModelTest(TestCase):
    def test_create_component(self):
        component = Component.objects.create(
            name="Engine",
            repair_price=Decimal("150.50"),
            purchase_price=Decimal("350.00")
        )
        self.assertEqual(component.name, "Engine")
        self.assertEqual(component.repair_price, Decimal("150.50"))
        self.assertEqual(component.purchase_price, Decimal("350.00"))

class VehicleModelTest(TestCase):
    def test_create_vehicle(self):
        vehicle = Vehicle.objects.create(
            name="Car Model X",
            registration_number="REG-1234"
        )
        self.assertEqual(vehicle.name, "Car Model X")
        self.assertEqual(vehicle.registration_number, "REG-1234")

class IssueModelTest(TestCase):
    def test_create_issue(self):
        vehicle = Vehicle.objects.create(name="Car Model X", registration_number="REG-1234")
        component = Component.objects.create(
            name="Engine",
            repair_price=Decimal("150.50"),
            purchase_price=Decimal("350.00")
        )
        issue = Issue.objects.create(
            vehicle=vehicle,
            component=component,
            is_new=True,
            created_at=datetime.now() - timedelta(days=30)
        )
        self.assertEqual(issue.vehicle.name, "Car Model X")
        self.assertEqual(issue.component.name, "Engine")
        self.assertTrue(issue.is_new)
        self.assertEqual(issue.created_at.date(), datetime.now().date() - timedelta(days=30))

class RevenueDataTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_revenue_data(self):
        response = self.client.get('/api/revenue/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)