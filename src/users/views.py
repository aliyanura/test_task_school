from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from src.users.serializers import RegisterSerializer,\
                                  LoginSerializer
from src.users.services import TeacherService, TokenService


class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        TeacherService.create_teacher(
            phone_number=serializer.validated_data.get('phone_number'),
            password=serializer.validated_data.get('password'),
            conf_password=serializer.validated_data.get('confirm_password'),
            subject=serializer.validated_data.get('subject'),
        )
        return Response(data={
            'message': 'The teacher has successfully registered',
            'status': 'CREATED'
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher, token, _ = TokenService.create_auth_token(
            phone_number=serializer.validated_data.get('phone_number'),
            password=serializer.validated_data.get('password')
        )
        return Response(data={
            'message': 'You have successfully logged in',
            'data': {
                'token': str(token),
                'token_type': 'Token',
                'user_id': teacher.pk
            },
            'status': "OK"
        }, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        TokenService.destroy_auth_token(user=request.user)
        return Response(data={
            'message': 'You have successfully logged out',
            'status': "NO CONTENT",
        }, status=status.HTTP_204_NO_CONTENT)