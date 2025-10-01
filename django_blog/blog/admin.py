from django.contrib import admin
from .models import Profile
from .models import Post  # if you also have Post

admin.site.register(Profile)
# admin.site.register(Post)  # if not already registered
