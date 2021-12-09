from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from muiristapi.models import Muirist
from django.contrib.auth.models import User
from rest_framework import serializers


@api_view(['GET'])
def user_profile(request):

    muirist = Muirist.objects.get(user=request.auth.user)
  
    muirist = MuiristSerializer(
        muirist, many=False, context={'request': request})
    
    profile = {
        "muirist": muirist.data,
    }

    return Response(profile)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class MuiristSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Muirist
        fields = ('user', 'name')

