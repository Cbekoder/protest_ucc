from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from assets.models import *
from .serializers import *
from rest_framework.response import Response
import random

class ExamAPIView(APIView):
    def get(self, request, pair_id):
        try:
            science_pairs = SciencePairs.objects.get(id=pair_id)
        except SciencePairs.DoesNotExist:
            return Response({"error": "SciencePairs not found"}, status=status.HTTP_404_NOT_FOUND)

        important_pair = ImportantSciencePairs.objects.get()
        important_sciences = [important_pair.science_1, important_pair.science_2, important_pair.science_3]
        important_questions = {}

        for science in important_sciences:
            questions = list(Question.objects.filter(science=science))
            sampled_questions = random.sample(questions, min(len(questions), 10))
            important_questions[science.name] = sampled_questions

        choice_sciences = [science_pairs.science_1, science_pairs.science_2]
        choice_questions = {}

        for science in choice_sciences:
            questions = list(Question.objects.filter(science=science))
            sampled_questions = random.sample(questions, min(len(questions), 30))
            choice_questions[science.name] = sampled_questions

        # Format response data
        response_data = []

        def format_question(question):
            serialized_question = QuestionSerializer(question).data
            options = serialized_question.pop('options')
            random.shuffle(options)
            return {
                "question_text": serialized_question['text'],
                "question_id": serialized_question['id'],
                "var_a_name": options[0]['option'],
                "var_a_id": options[0]['id'],
                "var_b_name": options[1]['option'],
                "var_b_id": options[1]['id'],
                "var_c_name": options[2]['option'],
                "var_c_id": options[2]['id'],
                "var_d_name": options[3]['option'],
                "var_d_id": options[3]['id'],
                "correct": next(option['id'] for option in options if option['is_correct'])
            }

        # Add formatted questions to response
        for science_name, questions in important_questions.items():
            formatted_questions = [format_question(question) for question in questions]
            response_data.append({
                "science": science_name,
                "questions": formatted_questions
            })

        for science_name, questions in choice_questions.items():
            formatted_questions = [format_question(question) for question in questions]
            response_data.append({
                "science": science_name,
                "questions": formatted_questions
            })

        return Response(response_data, status=status.HTTP_200_OK)

class CreateUserTestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pair_id):
        try:
            science_pairs = SciencePairs.objects.get(id=pair_id)
        except SciencePairs.DoesNotExist:
            return Response({"error": "SciencePairs not found"}, status=status.HTTP_404_NOT_FOUND)

        important_pair = ImportantSciencePairs.objects.get()
        important_sciences = [important_pair.science_1, important_pair.science_2, important_pair.science_3]
        important_questions = {}

        for science in important_sciences:
            questions = list(Question.objects.filter(science=science))
            sampled_questions = random.sample(questions, min(len(questions), 10))
            important_questions[science.name] = sampled_questions

        choice_sciences = [science_pairs.science_1, science_pairs.science_2]
        choice_questions = {}

        for science in choice_sciences:
            questions = list(Question.objects.filter(science=science))
            sampled_questions = random.sample(questions, min(len(questions), 30))
            choice_questions[science.name] = sampled_questions

        user_test = UserTest.objects.create(user=request.user)
        global order
        order = 1
        def create_user_test_question(question):
            user_test_question = UserTestQuestion.objects.create(user_test=user_test, question=question, order=order)
            order += 1
            return user_test_question

        # Add questions to UserTest
        for science_name, questions in important_questions.items():
            for question in questions:
                create_user_test_question(question)

        for science_name, questions in choice_questions.items():
            for question in questions:
                create_user_test_question(question)

        user_test_serializer = UserTestSerializer(user_test)
        return Response(user_test_serializer.data, status=status.HTTP_201_CREATED)

class SubmitUserTestView(generics.CreateAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_test_id = request.data.get('user_test_id')
        user_test = UserTest.objects.get(id=user_test_id, user=request.user)
        questions_data = request.data.get('questions')

        for question_data in questions_data:
            user_test_question = UserTestQuestion.objects.get(id=question_data['id'], user_test=user_test)
            selected_option_id = question_data.get('selected_option')
            if selected_option_id:
                selected_option = Option.objects.get(id=selected_option_id)
                UserTestAnswer.objects.create(user_test_question=user_test_question, selected_option=selected_option)

        return Response({"message": "Test submitted successfully"}, status=status.HTTP_200_OK)