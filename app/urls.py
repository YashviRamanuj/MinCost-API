from django.urls import path
from .views import MinCost

urlpatterns = [
    path('', MinCost, name="MinCost"),
]
