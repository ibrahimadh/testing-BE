#to convert model instance to JSON

from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description']



class AllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
