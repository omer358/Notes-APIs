import logging

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, authentication, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Notes
from .serializers import NotesSerializer, UserSerializer, UserRegisterSerializer

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


@api_view(['GET'])
def ping(request):
    msg = {"msg": "Hello world"}
    return Response(msg)


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permissionNs_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        logging.info(request.user)
        user = User.objects.get(username=request.user)
        queryset = Notes.objects.all().filter(user=user.id)
        serializer_class = NotesSerializer(queryset, many=True)
        return Response(data=serializer_class.data)

    def create(self, request, *args, **kwargs):
        note = request.data
        user = User.objects.get(username=request.user)
        new_note = Notes.objects.create(
            title=note['title'],
            content=note['content'],
            user=user)
        new_note.save()
        serializer = NotesSerializer(new_note)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def delete_all(self, request):
        user_notes = Notes.objects.all().delete()
        return Response(data={'response': 'successfully deleted '})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


class Register(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        tokens = {'refresh': str(refresh), 'access': str(refresh.access_token), }
        return Response(tokens)
