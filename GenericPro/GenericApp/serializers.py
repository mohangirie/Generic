from rest_framework import serializers
from GenericApp.models import Emp


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ['eid','ename','esal']
