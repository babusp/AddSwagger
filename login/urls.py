from django.urls import path

from login.views import RegisterView,LoginAPIView,Logout,ListUserAPIview,UserCreationrAPIView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path("logout/",Logout.as_view(),name="logout"),
    path("userlist/",ListUserAPIview.as_view()),
    path("createuser/",UserCreationrAPIView.as_view()),
]