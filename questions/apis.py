from questions.serializers import QuestionListSerializer
from questions.models import Question
from rest_framework import generics

##List and Create
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

##Retrieve(Detail)
class QuestionRetrieve(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer