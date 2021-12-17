from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from muiristapi.models import Snippet, List, Muirist, Park
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import status

from muiristapi.views.snippet_view import UserSerializer

class ListView(ViewSet):
    

    def retrieve(self, request, pk=None):
       
        try:
            snippet_list = List.objects.get(pk=pk)
            serializer = ListSerializer(List, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        
        
        snippet_list = List.objects.all()

        
        serializer = ListSerializer(
            snippet_list, many=True, context={'request': request})
        return Response(serializer.data)
  
    @action(methods=['GET'], detail=False)
    def myLists(self, request):
        user = Muirist.objects.get(user=request.auth.user)
    
        try:
            list = List.objects.filter(muirist = user)
            list_serializer = ListSerializer(list, many=True, context={'request': request})
            return Response(list_serializer.data)
        except List.DoesNotExist:
            return Response(
                {'message': 'List does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )    
            
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username')    
        
class ParkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Park
        fields = '__all__'

class MuiristSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    class Meta:
        model = Muirist
        fields = ('id', 'user')
      

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'content')

class ListSerializer(serializers.ModelSerializer):
    
    park = ParkSerializer()
    muirist = MuiristSerializer()
    Snippets = SnippetSerializer(many=True)
    class Meta:
        model = List
        fields = ('id', 'Snippets', 'park', 'muirist')
        
