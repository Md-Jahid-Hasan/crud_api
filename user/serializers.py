from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers for a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a user. Override the function"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        s_text = f"{user.name} join in the community"
        feed = models.ProfileFeedItem.objects.create(
            user_profile=user,
            status_text=s_text,
        )
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        return instance


class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializer for listing feed objects"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True},
            'status_text': {'read_only': True},
        }
