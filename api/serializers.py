from rest_framework import serializers
from .models import Task
from .models import Bro

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
class BroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bro
        fields = "__all__"
