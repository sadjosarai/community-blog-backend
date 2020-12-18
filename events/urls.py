from django.urls import path
from .views import (
    EventListView,

    EventCreateView,
)

app_name = "events"
urlpatterns = [
    path('event/', EventListView.as_view(), name="list_all_event"),
    path('event/create/', EventCreateView.as_view(), name="create_event"),
]