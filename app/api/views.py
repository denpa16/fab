from rest_framework import viewsets
from .serializers import PollSerializer, QuestionSerializer
from .models import Poll, Question
from rest_framework.generics import get_object_or_404


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