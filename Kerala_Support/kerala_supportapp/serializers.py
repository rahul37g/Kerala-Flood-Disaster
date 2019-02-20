from kerala_supportapp.models import *
from rest_framework import serializers, fields


class LanguageMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageMaster
        fields = '__all__'


class ServiceTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypeMaster
        fields = '__all__'

class EmergencyTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyTypeMaster
        fields = '__all__'

class ServiceMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceMaster
        fields = '__all__'

class EmployeeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMaster
        fields = '__all__'

class LocationTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationTypeMaster
        fields = '__all__'

class LocationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationMaster
        fields = '__all__'

class StatusMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusMaster
        fields = '__all__'

class ServiceRequiredTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequiredTransaction
        fields = '__all__'

class TeamMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMaster
        fields = '__all__'
