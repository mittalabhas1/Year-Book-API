from users.models import User, UserDetails
from users.serializers import UserSerializer, UserDetailsSerializer
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

	# def post(self, request, format=None):
	# 	serializer = UserSerializer(data=request.DATA)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
	def get(self, request, pk, format=None):
		user = UserDetails.objects.get(pk=pk)
		serializer = UserDetailsSerializer(user)
		return Response(serializer.data)