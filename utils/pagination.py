from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

class PostPageNumberPagination(PageNumberPagination):
    page_size = 2


class FormationLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

class FormationPageNumberPagination(PageNumberPagination):
    page_size = 2

class EventPageNumberPagination(PageNumberPagination):
    page_size = 3