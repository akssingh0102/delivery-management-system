from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from services.views import ComponentViewSet, VehicleViewSet, IssueViewSet
from services.views import revenue_data


router = DefaultRouter()
router.register(r'components', ComponentViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'issues', IssueViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/revenue/', revenue_data),

]
