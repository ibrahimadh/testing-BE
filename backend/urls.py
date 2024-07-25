from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemDetail, ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)


urlpatterns = [
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('', include(router.urls))
]