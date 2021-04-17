# api/serializers.py
from rest_framework import serializers
from personalInfo import models


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'Name',
        )
        model = models.PersonalInfo

    def save(self, user):
        perInfo = models.PersonalInfo(
            Name = self.validated_data['Name'],
            User_id = user
        )     

        perInfo.save()

        return perInfo 