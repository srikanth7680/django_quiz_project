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

from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView


class ListUsers(APIView):
    def get(self,request,format = None):

        # usernames = [user.username for user in User.objects.all()]
        usernames = [{'username': user.username,'email':user.email,'first_name':user.first_name} for user in User.objects.all()]
        return Response(usernames)
    def post(self,request):
        print(request.data)
        print('user created')
        user = User.objects.create_user(username=request.data['username'],
                email='sun@gmail.com',password=request.data['password'])
        return Response(user.username)
