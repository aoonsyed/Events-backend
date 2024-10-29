from rest_framework import serializers
from .models import Event, User, Location
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['address', 'city', 'country']

class EventSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    Submitted_By = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Event
        fields = ['name', 'description', 'event_datetime', 'location', 'Latitude', 'Longitude', 'Category', 'Status', 'Submitted_By']

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(
            address=location_data['address'],
            city=location_data['city'],
            country=location_data['country']
        )
        event = Event.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            event_datetime=validated_data['event_datetime'],
            location=location,
            Latitude=validated_data['Latitude'],
            Longitude=validated_data['Longitude'],
            Category=validated_data['Category'],
            Status=validated_data['Status'],
            Submitted_By=validated_data['Submitted_By']
        )
        return event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CustomUserTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'email': user.email,
            'name': user.name,
            'role': user.role,
        }