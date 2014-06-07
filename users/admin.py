from django.contrib import admin
from users.models import User, UserDetails

admin.site.register(User)
admin.site.register(UserDetails)