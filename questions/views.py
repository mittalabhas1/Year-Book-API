from questions.models import Questions, Answers
from questions.serializers import QuestionSerializer, AnswerSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class QuestionList(APIView):
	"""
	Lists all the questions
	"""
	def get(self, request, format=None):
		questions = Questions.objects.all()
		serializer = QuestionSerializer(questions, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = QuestionSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class AnswerView(APIView):
	"""
	Answer of a question by a user
	"""
	def get(self, request, pk, uid, format=None):
		answer = Answers.objects.get(user=uid, qid=pk)
		serializer = AnswerSerializer(answer)
		return Response(serializer.data)

	def put(self, request, pk, uid, format=None):
		try:
			answer = Answers.objects.get(user=uid, qid=pk)
			serializer = AnswerSerializer(answer, data=request.DATA)
		except Exception, Answer.DoesNotExist:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)