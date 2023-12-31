from django.urls import path
from src.grades.views import StudentAPIView, MailingAPIView


urlpatterns = [
    path('students/', StudentAPIView.as_view({
        'get': 'list', 'post': 'create'
    }), name='sturents-list-create'),
    path('students/<str:pk>/', StudentAPIView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    }), name='sturent-ret-upd-del'),
    path('mailing/', MailingAPIView.as_view(), name='mailing'),
]