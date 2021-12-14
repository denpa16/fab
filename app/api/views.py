from rest_framework import viewsets, mixins
from api.serializers import (
    PollSerializer, QuestionSerializer,
    ChoiceSerializer,
)
from .models import Poll, Question, Choice
from rest_framework.generics import get_object_or_404
from datetime import datetime


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer


    def get_queryset(self):
        poll = get_object_or_404(Poll, id=self.kwargs['id'])
        return poll.questions.all()

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, pk=self.kwargs['id'])
        serializer.save(poll=poll)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            poll__id=self.kwargs['id'],
        )
        serializer.save(question=question)

    def get_queryset(self):
        question = get_object_or_404(Question, id=self.kwargs['question_pk'])
        return question.choices.all()


class ActivePollListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Poll.objects.filter(end_date__gte=datetime.today())
    serializer_class = PollSerializer

