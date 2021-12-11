from re import S
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from muiristapi.models import Snippet, Park, Muirist
from django.contrib.auth.models import User


class SnippetView(ViewSet):
   
    def create(self, request):
        
        
        muirist = Muirist.objects.get(user=request.auth.user)
        park = Park.objects.get(pk=request.data["parkId"])
        

        try:
            
            snippet = Snippet.objects.create(
                title=request.data["title"],
                content=request.data["content"],
                park=park,
                muirist = muirist
            )
            serializer = SnippetSerializer(snippet, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
     
        try:
           
            snippet = Snippet.objects.get(pk=pk)
            serializer = SnippetSerializer(snippet, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(
            snippets, many=True, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        park = Park.objects.get(pk=request.data['parkId'])
        
        snippet = Snippet.objects.get(pk=pk)
        snippet.title = request.data["title"]
        snippet.content = request.data["content"]
        park = park
        snippet.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
       
        try:
            snippet = Snippet.objects.get(pk=pk)
            snippet.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Snippet.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username',)

class MuiristSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        
        model = Muirist
        fields = ('id', 'user') 
        
class ParkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Park
        fields = ('id', 'name',)

class SnippetSerializer(serializers.ModelSerializer):
    muirist = MuiristSerializer()
    park = ParkSerializer()
    
    class Meta:
        
        model = Snippet
        fields = ('id', 'title', 'content', 'muirist', 'park')
        depth = 1