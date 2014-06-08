from rest_framework import serializers
from users.models import User, UserDetails
from questions.serializers import QuestionSerializer, AnswerSerializer

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password')

class UserDetailsSerializer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True)
	class Meta:
		model = UserDetails
		fields = ('uid', 'name', 'course', 'email', 'phoneNo', 'dob', 'hometown', 'answers')