from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer
from .models import Todo


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow PUT, PATCH, DELETE requests only if the user is the owner of the object
        return obj.task_owner == request.user


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]