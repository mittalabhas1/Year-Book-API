from users.models import User, UserDetails
from users.serializers import UserSerializer, UserDetailsSerializer
from questions.models import Questions, Answers
from questions.serializers import QuestionSerializer, AnswerSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class UserList(APIView):
	"""
	Lists the username and password of all the Users
	"""
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
	"""
	Returns the user details along with all the answers the user has given.
	"""
	def get(self, request, pk, format=None):
		user = UserDetails.objects.get(uid=pk)
		serializer = UserDetailsSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		try:
			user = UserDetails.objects.get(pk=pk)
			serializer = UserDetailsSerializer(user, data=request.DATA)
		except Exception, UserDetails.DoesNotExist:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)