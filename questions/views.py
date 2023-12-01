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
def question_list(request):
    questions = Question.objects.all()
    question_list = []
    for question in questions:
        question_list.append(question.question)
    context = {'question':question_list}
    print(context)
    return render(request,'questions/question_list.html',context)

def question_details(request,question_id):
    question = Question.objects.get(id=question_id)
    question_dict = {
        'question' : question.question,
        'category' : question.category,
        'added_date' : str(question.added_dt)
    }
    json_obj = json.dumps(question_dict)
    return HttpResponse(json_obj)

##Question_Template
def question_details_template(request,question_id):
    question = Question.objects.get(id=question_id)
    context = {
        'question' : question.question,
        'category' : question.category,
        'added_date' : str(question.added_dt)
    }
    return render(request,'questions/question_details_template.html',context)