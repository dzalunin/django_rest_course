from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from authapp.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserModelSerializer
