from django.shortcuts import render
from .models import Event
from utils.pagination import EventPageNumberPagination
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from .serializers import (  
    EventListSerializer,
    EventCreateSerializer,
)

class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    pagination_class = EventPageNumberPagination

class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
