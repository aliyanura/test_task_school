from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from src.grades.services import StudentService
from src.grades.serializers import StudentSerializer



class StudentAPIView(ModelViewSet):
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = StudentSerializer
    queryset = StudentService.filter(is_deleted=False)
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,)
        serializer.is_valid(raise_exception=True)
        StudentService.create(
            data=serializer.validated_data
        )
        return Response({'message': 'Student successfully created'},
                        status=status.HTTP_201_CREATED)


