from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('polls', views.PollViewSet, basename='polls')

urlpatterns = router.urls