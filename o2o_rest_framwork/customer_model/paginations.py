from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)

class ListPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 3
class ListPagePagination(ListPagination):
    page_size=2