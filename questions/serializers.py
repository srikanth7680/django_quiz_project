from rest_framework.serializers import ModelSerializer

from questions.models import Question,Answer
class QuestionListSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['question','category','added_dt']

class UserSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['Question','answer']