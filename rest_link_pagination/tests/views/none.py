from rest_framework import generics
from rest_link_pagination.tests import serializers, views


class NoPaginationList(views.FakeQueryset, generics.ListAPIView):
    serializer_class = serializers.TestSerializer
