from rest_framework import serializers


class CtegorySerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  category_name= serializers.CharField(max_length=50)
  category_description=serializers.CharField(max_length=200)
  category_status= serializers.BooleanField(default=True)