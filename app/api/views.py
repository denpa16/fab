from rest_framework import viewsets
from .serializers import PollSerializer
from .models import Poll


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer