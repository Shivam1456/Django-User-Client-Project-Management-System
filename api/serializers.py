from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User
from django.utils.timezone import make_aware
from datetime import datetime
import pytz

class ISTDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        if value is not None:
            ist = pytz.timezone('Asia/Kolkata')
            value = make_aware(value) if not value.tzinfo else value
            value = value.astimezone(ist)
        return super().to_representation(value)

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ['id', 'name']

class ProjectNestedSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='project_name')

    class Meta:
        model = Project
        fields = ['id', 'name']

class ProjectOutputSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    client = serializers.CharField(source='client.client_name')
    created_by = serializers.StringRelatedField()
    created_at = ISTDateTimeField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ProjectListSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    created_at = ISTDateTimeField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_at', 'created_by']

class ClientListSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    created_at = ISTDateTimeField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectNestedSerializer(many=True, read_only=True)
    created_at = ISTDateTimeField()
    updated_at = ISTDateTimeField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_name']

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Project
        fields = ['project_name', 'users']

    def validate_users(self, value):
        user_ids = []
        for user_data in value:
            try:
                user = User.objects.get(id=user_data['id'])
                if user.username != user_data['name']:
                    raise serializers.ValidationError(f"Name does not match for user id {user_data['id']}")
                user_ids.append(user.id)
            except User.DoesNotExist:
                raise serializers.ValidationError(f"User with id {user_data['id']} does not exist")
        return user_ids