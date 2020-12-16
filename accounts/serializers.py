from rest_framework.serializers import SerializerMethodField
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    name = SerializerMethodField()
    email = SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = [
                    'name',
                    'email', 
                    'description', 
                    'image', 
                    'tel', 
                    'social_networks', 
                    'location', 
                    'created_at', 
                    'updated_at'
                ]
    
    def get_name(self, obj):
        return str(obj.username)

    def get_email(self, obj):
        return str(obj.email)