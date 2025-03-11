from rest_framework import serializers
from blogpost.models import blog

class blogSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    date_published = serializers.DateField()
    def create(self, validated_data):
        return blog.objects.create(**validated_data)