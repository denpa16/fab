from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('polls', views.PollViewSet, basename='polls')
router.register('polls/(?P<id>\d+)/questions',views.QuestionViewSet,basename='questions')

urlpatterns = router.urls