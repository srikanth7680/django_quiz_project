from django.shortcuts import render

from django.http import HttpResponse
import json
from questions.models import Question

# Create your views here.
def index(request):
    # json_obj = json.dumps({'msg': "good morning"}) ##JSON
    # return HttpResponse(json_obj)
    # # return HttpResponse("Good morning") strings
    # return HttpResponse({"msg": "Good morning"}) ##Dict
    return HttpResponse("<html><body><h1>Hello World!</h1></body></html>") ##HTML
def greet(request):
    questions = Question.objects.all()
    question_list = []
    for question in questions:
        question_list.append(question.question)
    context = {'question':question_list}
    print(context)
    return render(request,'questions/index.html',context)