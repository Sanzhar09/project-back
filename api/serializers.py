from rest_framework import serializers
from api import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = 'id','name'

class ArticleSerialize(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    category = CategorySerializer()
    title = serializers.CharField()
    image = serializers.CharField()
    text = serializers.CharField()

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = 'id', 'name'

class Manager(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    password = serializers.CharField()