from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
# ...existing code...
from django.urls import path
from . import views

# ...existing code...
urlpatterns = [
    # ...existing patterns...
    path('follow/<int:user_id>', views.follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow-user'),
    # ...existing patterns...
]
# ...existing code...