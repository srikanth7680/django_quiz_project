from django.urls import path

from questions.views import index,question_list,question_details,question_details_template
  ##or
# from  .views import index,greet
from questions import views

urlpatterns = [
    path('index',index),
    path('question_list',question_list),
    path('question/<int:question_id>',question_details),
    path('question_temp/<int:question_id>',question_details_template)
]