from rest_framework import serializers
from questions.models import Questions, Answers

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Questions
		fields = ('id', 'question')

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answers
		fields = ('qid', 'answer')