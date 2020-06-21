from rest_framework import serializers

from todo.models import Todo

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title','text']