from rest_framework import serializers
from .models import Question


# class TagSerializer(serializers.Serializer):
#     tag_name = serializers.CharField(max_length=50)
    
#     def create(self, validated_data):
#         return Tag.objects.create(**validated_data)

# class QuestionSerializer(serializers.Serializer):
#     tagss = TagSerializer()
#     question_text = serializers.CharField(max_length=200)
#     choice_text1 = serializers.CharField(max_length=200)
#     choice_text2 = serializers.CharField(max_length=200)
#     choice_text3 = serializers.CharField(max_length=200)
#     choice_text4 = serializers.CharField(max_length=200)
#     correct_option = serializers.CharField(max_length=200)

#     def create(self, validated_data):
#         return Question.objects.create(**validated_data)

from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


class QuestionSerializer(serializers.ModelSerializer):
    # tag = TagSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'