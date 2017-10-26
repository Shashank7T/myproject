from . models import employees
from rest_framework import serializers


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        #fields = ('firstname','lastname') # in order to display any specific fields from a list of fields
        fields = '__all__'  #To display all the fields stated in the model


