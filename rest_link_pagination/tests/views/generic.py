from rest_framework import generics
from rest_link_pagination import mixins
from rest_link_pagination.tests import serializers, views


class PaginatedList(views.FakeQueryset, mixins.LinkPaginationMixin,
                    generics.ListAPIView):
    serializer_class = serializers.TestSerializer
    paginate_by = 1
