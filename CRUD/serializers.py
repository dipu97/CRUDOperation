from rest_framework import serializers
from .models import DataSet


class DatasetSerializers(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'
