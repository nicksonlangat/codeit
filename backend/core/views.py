from rest_framework import serializers, viewsets
from .models import Code, SharedLink

# Create your views here.

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields= "__all__"


class SharedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedLink
        fields= "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['code'] = CodeSerializer(instance.code).data

        return representation


class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


class SharedLinkViewSet(viewsets.ModelViewSet):
    queryset = SharedLink.objects.all()
    serializer_class = SharedLinkSerializer
    lookup_field = "link"

