from rest_framework import serializers
from questions.models import Questions, Answers

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Questions
		field = ('id', 'question')

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answers
		field = ('id', 'uid', 'qid', 'answer')