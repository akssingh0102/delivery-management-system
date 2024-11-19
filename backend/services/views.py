from rest_framework import viewsets
from .models import Component, Vehicle, Issue
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from datetime import datetime, timedelta
from .models import Issue

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


@api_view(['GET'])
def revenue_data(request):
    # Example data aggregation
    today = datetime.now()
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)

    # Calculate daily revenue (last 7 days)
    daily = []
    for i in range(7):
        day = today - timedelta(days=i)
        revenue = Issue.objects.filter(created_at__date=day.date()).aggregate(
            revenue=Sum('component__purchase_price')
        )['revenue'] or 0
        daily.append({'date': day.strftime('%Y-%m-%d'), 'revenue': revenue})

    # Monthly revenue (last 12 months)
    monthly = []
    for i in range(12):
        month = (today.month - i - 1) % 12 + 1
        year = today.year - (1 if i >= today.month else 0)
        revenue = Issue.objects.filter(
            created_at__year=year, created_at__month=month
        ).aggregate(revenue=Sum('component__purchase_price'))['revenue'] or 0
        monthly.append({'month': f'{year}-{month:02d}', 'revenue': revenue})

    # Yearly revenue (last 5 years)
    yearly = []
    for i in range(5):
        year = today.year - i
        revenue = Issue.objects.filter(
            created_at__year=year
        ).aggregate(revenue=Sum('component__purchase_price'))['revenue'] or 0
        yearly.append({'year': str(year), 'revenue': revenue})

    return Response({'daily': daily, 'monthly': monthly, 'yearly': yearly})