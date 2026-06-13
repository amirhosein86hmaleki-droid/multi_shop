from rest_framework.pagination import PageNumberPagination
from django.conf import settings

class StandardResulteSetPagination(PageNumberPagination):
    page_size = (settings, 'PAGINATION_PAGE_SIZE', 1)
    