from django.shortcuts import render

from django.http import HttpResponse
import json
from questions.models import Question, Answer
from django.contrib import admin

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
        question_list.append({'question':question.question,
                             'id':question.id})
    context = {'questions':question_list}
    print(context)
    return render(request,'questions/question_list.html',context)

def question_details(request,question_id):
    question = Question.objects.get(id=question_id)
    # question = Question.objects.filter(id=1).update(question = "who is the CM of Karnataka?")
    # question = Question.objects.filter(id=1).delete()
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
    answer_objs = Answer.objects.filter(Question=question)
    answer_list = []
    for option in answer_objs:
        answer_list.append({'answer':option.answer})
    context = {
        'question' : question.question,
        'category' : question.category,
        'added_date' : str(question.added_dt),
        'answer_list' :answer_list
    }
    return render(request,'questions/question_details_template.html',context)


