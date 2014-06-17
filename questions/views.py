from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from questions.models import Questions, Answers
from questions.serializers import QuestionSerializer, AnswerSerializer

class QuestionList(generics.ListCreateAPIView):
	"""
	Lists all the questions
	"""
	model = Questions
	serializer_class = QuestionSerializer

class QuestionDetail(APIView):
	"""
	Lists the answers of a question of all the Users
	"""
	def get(self, request, pk, format=None):
		answers = Answers.objects.all().filter(qid=pk)
		serializer = AnswerSerializer(answers, many=True)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		try:
			question = self.get_object(pk)
			serializer = AnswerSerializer(question, data=request.DATA)
		except Exception, Answers.DoesNotExist:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)

class AnswerView(generics.ListCreateAPIView):
	"""
	Answer of a question by a user
	"""
	model = Answers
	serializer_class = AnswerSerializer
