from django.urls import path
from .views import ControlStationListView, ControlStationDetailView
# from . import views
urlpatterns = [
    path('api/control-station',
         ControlStationListView.as_view(), name='control'),
    path('api/control-station/<int:pk>',
         ControlStationDetailView.as_view(), name='detail'),
]
