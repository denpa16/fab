from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('polls', views.PollViewSet, basename='polls')

# CRUD вопросов
router.register('polls/(?P<id>\d+)/questions',views.QuestionViewSet,basename='questions')

# CRUD вариантов ответов
router.register('polls/(?P<id>\d+)/questions/(?P<question_pk>\d+)/choices',views.ChoiceViewSet,basename='choices')

# READ всех активных опросов
router.register('active_polls', views.ActivePollListViewSet)

router.register(
    'polls/(?P<id>\d+)/questions/(?P<question_pk>\d+)/answers',
    views.AnswerCreateViewSet,
    basename='answers'
)

router.register(
    'my_polls',
    views.UserIdPollListViewSet,
    basename='list_userid_polls'
)

urlpatterns = router.urls