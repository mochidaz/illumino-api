from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from auth.auth import IsNotMember
# from common.exceptions import validation_exception_handler
from user.models import User
from user.serializers import UserSerializer
from common.serializers.generic_serializer import ResponseSerializer


class JWTObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class JwtObtain(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=request.data.get('email'))
        except User.DoesNotExist:
            raise NotFound('User does not exist!')

        if not user.active:
            raise ValidationError({
                'email': ['User is not active']
            })

        if not user.check_password(request.data.get('password')):
            raise ValidationError({
                'password': ['Password is incorrect']
            })

        response = super().post(request, *args, **kwargs)

        response.data['email'] = user.email

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': response.data,
            'error': None,
        })

        return Response(serializer.data)


class RefreshToken(TokenRefreshView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        serializer = ResponseSerializer({
            'code': 200,
            'status': 'success',
            'records_total': 1,
            'data': response.data,
            'error': None,
        })

        return Response(serializer.data)


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsNotMember]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        self.perform_create(serializer)

        resp = ResponseSerializer({
            'code': 201,
            'status': 'success',
            'records_total': 1,
            'data': {
                "message": "User created successfully"
            },
            'error': None,
        })

        return Response(resp.data)
