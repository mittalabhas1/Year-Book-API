from rest_framework import serializers
from users.models import User, UserDetails

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password')

class UserDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserDetails
		fields = ('uid', 'name', 'course', 'email', 'phoneNo', 'dob', 'hometown')