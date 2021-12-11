from re import S
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from muiristapi.models import Park, Snippet


class ParkView(ViewSet):
   

    def create(self, request):
        
        park = Park.objects.get(user=request.auth.user)
      

        try:
            
            park = Park.objects.create(
                name=request.data["name"],
                location=request.data["location"],
            )
            serializer = ParkSerializer(park, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

       
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        
        parks = Park.objects.all()
        serializer = ParkSerializer(
            parks, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
     
        try:
           
            park = Park.objects.get(pk=pk)
            serializer = ParkSerializer(park, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
  
        park = Park.objects.get(pk=pk)
        park.name = request.data["name"]
        park.location = request.data["location"]
        park.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
       
        try:
            park = Park.objects.get(pk=pk)
            park.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Park.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  
# class SnippetSerializer(serializers.ModelSerializer):
    
#     class Meta:
        
#         model = Snippet
#         fields = ('title', 'content')

class ParkSerializer(serializers.ModelSerializer):
    
    class Meta:
        # snippet = SnippetSerializer
        
        model = Park
        fields = ('id', 'name', 'location')
        depth = 1
