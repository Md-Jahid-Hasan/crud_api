from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers, models
from . import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    def update(self, request, *args, **kwargs):

        feed = models.ProfileFeedItem.objects.create(
            user_profile=request.user,
            status_text=f"{request.user.name} Just Update it's profile"
        )
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # kwargs['partial'] = True
        # feed = models.ProfileFeedItem.objects.create(
        #     user_profile=request.user,
        #     status_text=f"{request.user.name} Just Update it's profile"
        # )
        return super().partial_update(request, *args, **kwargs)


class UserLoginView(ObtainAuthToken):
    """Creating user authentication Token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedViewSet(generics.ListAPIView):
    queryset = models.ProfileFeedItem.objects.all()
    serializer_class = serializers.ProfileFeedSerializer
