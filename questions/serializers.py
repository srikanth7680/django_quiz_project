from rest_framework.serializers import ModelSerializer

from questions.models import Question
class QuestionListSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['question','category','added_dt']