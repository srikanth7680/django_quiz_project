from questions.serializers import QuestionListSerializer
from questions.models import Question
from rest_framework import generics

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer