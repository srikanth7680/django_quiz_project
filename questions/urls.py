from django.urls import path

from questions.views import index,question_list,question_details,question_details_template
  ##or
# from  .views import index,greet
from questions import views
from questions.apis import QuestionList,QuestionRetrieve,ListUsers,UserViewSet
from questions.models import Question

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')



urlpatterns =   router.urls

urlpatterns = [
    path('index',index),
    path('question_list',views.question_list),
    path('question/<int:question_id>',views.question_details),
    path('question_temp/<int:question_id>',views.question_details_template),

    path('drf/questions', QuestionList.as_view()),
    path('drf/<int:pk>/',QuestionRetrieve.as_view()),
    path('drf/users',ListUsers.as_view())
    ]


