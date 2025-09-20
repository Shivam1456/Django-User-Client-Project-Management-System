from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import (
    ClientListSerializer, ClientCreateSerializer, ClientSerializer,
    ProjectCreateSerializer, ProjectOutputSerializer, ProjectListSerializer
)

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ClientCreateSerializer
        return ClientListSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        output_serializer = ClientListSerializer(serializer.instance)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        client = Client.objects.get(pk=self.kwargs['client_id'])
        user_ids = serializer.validated_data.pop('users')
        instance = serializer.save(client=client, created_by=self.request.user)
        instance.users.set(user_ids)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        output_serializer = ProjectOutputSerializer(serializer.instance)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserProjectsListView(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.projects_assigned.all()