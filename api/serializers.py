from rest_framework import serializers
from api.models import Company,Employee
#used to convert JSON to Obj or vice verca

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # Meta class avaialble in HyperlinkedModelSerialzer only

    #send a custom field (read only)
    company_id=serializers.ReadOnlyField()

    class Meta:
        model=Company
        fields="__all__" #if yoou want all fields from that give model



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()

    class Meta:
        model=Employee
        fields="__all__"