from django.urls import path

from auth.views import JwtObtain, RefreshToken, RegisterViewSet

urlpatterns = [
    path('/login', JwtObtain.as_view(), name='token_obtain'),
    path('/refresh', RefreshToken.as_view(), name='token_refresh'),
    path('/register', RegisterViewSet.as_view({'post': 'create'}), name='register'),
]