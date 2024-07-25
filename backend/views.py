from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import ItemSerializer, AllSerializer
from .models import Item


# Create your views here.
class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = AllSerializer
