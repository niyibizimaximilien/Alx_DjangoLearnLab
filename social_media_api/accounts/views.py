from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser  # ✅ for CustomUser.objects.all()

User = get_user_model()


# ----------------------------
# Registration
# ----------------------------
class RegisterView(generics.GenericAPIView):  # ✅ uses GenericAPIView
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "token": user.token  # token created in serializer
        }, status=status.HTTP_201_CREATED)


# ----------------------------
# Login
# ----------------------------
class LoginView(generics.GenericAPIView):  # ✅ uses GenericAPIView
    serializer_class = RegisterSerializer  # minimal, just reuse

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# ----------------------------
# Profile
# ----------------------------
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# ----------------------------
# Follow / Unfollow
# ----------------------------
class FollowUserView(generics.GenericAPIView):  # ✅ GenericAPIView
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = CustomUser.objects.get(id=user_id)  # ✅ uses CustomUser.objects.all() internally
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if target_user == request.user:
            return Response({"error": "Cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target_user)
        return Response({"success": f"You are now following {target_user.username}"})


class UnfollowUserView(generics.GenericAPIView):  # ✅ GenericAPIView
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = CustomUser.objects.get(id=user_id)  # ✅ uses CustomUser.objects.all()
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(target_user)
        return Response({"success": f"You have unfollowed {target_user.username}"})
