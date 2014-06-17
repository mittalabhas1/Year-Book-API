from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User, UserDetails
from users.serializers import UserSerializer, UserDetailsSerializer

class UserList(generics.ListCreateAPIView):
	model = User
	serializer_class = UserSerializer

class UserDetail(generics.ListCreateAPIView):
	model = UserDetails
	serializer_class = UserDetailsSerializer

	# def create(self, request, *args, **kwargs):
	# 	try:
	# 		obj = UserDetails()
	# 		id = User.objects.get(pk=request.DATA.get('uid'))
	# 		obj.uid = id
	# 		obj.name = request.DATA.get('name')
	# 		obj.course = request.DATA.get('course')
	# 		obj.email = request.DATA.get('email')
	# 		obj.phoneNo = request.DATA.get('phoneNo')
	# 		obj.dob = request.DATA.get('dob')
	# 		obj.hometown = request.DATA.get('hometown')
	# 		obj.answers = request.DATA.get('answers', [])
	# 		obj.save()
	# 		# print obj.json_serialize()
	# 		return Response(obj.json_serialize(), status=status.HTTP_201_CREATED)
	# 	except User.DoesNotExist:
	# 		resp = {
	# 			"error": "APINotFoundError",
	# 			"code": 400,
	# 			"error_message": "User not found"
	# 		}
	# 		return Response(resp, status=status.HTTP_400_BAD_REQUEST)
