from django.shortcuts import render
from .serializers import ControlStationSerializer
from .models import ControlStation
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
# Create your views here.


class ControlStationListView(generics.ListCreateAPIView):
    queryset = ControlStation.objects.all()
    serializer_class = ControlStationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class ControlStationDetailView(generics.RetrieveDestroyAPIView):
    queryset = ControlStation.objects.all()
    serializer_class = ControlStationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = ControlStation.objects.filter(
            pk=kwargs['pk'], poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("This is\'t your post to delete")
