from django.urls import path

from questions.views import index,greet
  ##or
# from  .views import index,greet

urlpatterns = [
    path('index',index),
    path('greet',greet)
]