from rest_framework import serializers
from .models import *

class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'

class Science1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = ['name']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, source='option_set')

    class Meta:
        model = Question
        fields = ['id', 'text', 'options']


class UserTestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTestAnswer
        fields = ['user_test_question', 'selected_option']

class UserTestQuestionSerializer(serializers.ModelSerializer):
    answer = UserTestAnswerSerializer()

    class Meta:
        model = UserTestQuestion
        fields = ['question', 'order', 'answer']

class UserTestSerializer(serializers.ModelSerializer):
    questions = UserTestQuestionSerializer(many=True)

    class Meta:
        model = UserTest
        fields = ['id', 'user', 'created_at', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        user_test = UserTest.objects.create(**validated_data)
        for question_data in questions_data:
            answer_data = question_data.pop('answer')
            user_test_question = UserTestQuestion.objects.create(user_test=user_test, **question_data)
            UserTestAnswer.objects.create(user_test_question=user_test_question, **answer_data)
        return user_test