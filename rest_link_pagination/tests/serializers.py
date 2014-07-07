from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
