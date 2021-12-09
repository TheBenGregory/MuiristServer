from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from muiristapi.models import Muirist


class MuiristView(ViewSet):
    

    def retrieve(self, request, pk=None):
       
        try:
            muirist = Muirist.objects.get(pk=pk)
            serializer = MuiristSerializer(muirist, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
       
        muirists = Muirist.objects.all()

        
        serializer = MuiristSerializer(
            muirists, many=True, context={'request': request})
        return Response(serializer.data)

class MuiristSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Muirist
        fields = ('id', 'user', 'name')