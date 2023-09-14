from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf_task_manager.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action

class ProfileView(viewsets.ModelViewSet):    
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()