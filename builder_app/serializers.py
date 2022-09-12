from django.contrib.auth.models import User

from rest_framework import serializers

from .models import TableInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableInfo
        fields = ['values']

    def validate(self, attrs):
        for value in attrs['values']:
            if len(value['reach']) != 10:
                raise serializers.ValidationError({"detail": "The length of the row is not 10"})
            if value['unit'] < 0:
                raise serializers.ValidationError({"detail": "The unit element is smaller than zero"})
            for elem in value['reach']:
                if isinstance(elem, int):
                    raise serializers.ValidationError({"detail": "Not all elements are float"})
                if elem < 0 or elem > 100:
                    raise serializers.ValidationError(
                        {
                            "detail":"The reach elements are not in interval 0-100"
                        }
                    )
            row_reach_value_copy = value['reach'].copy()
            row_reach_value_copy.sort(reverse=True)
            if row_reach_value_copy != value['reach']:
                raise serializers.ValidationError(
                    {
                        "detail": "The reach elements sequence is non-decreasing"
                    }
                )
            return attrs
