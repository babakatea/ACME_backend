from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


class AccountViewSet(viewsets.ViewSet):

    # @csrf_exempt
    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({'msg': 'Please provide both email and password'}, status=HTTP_400_BAD_REQUEST)
        if email != 'j.doe@innopolis.ru':
            return Response({'msg': 'User not found'}, status=HTTP_400_BAD_REQUEST)
        if password != '12345678':
            return Response({'msg': 'Invalid password'}, status=HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create()
        return Response({'token': token.key}, status=HTTP_200_OK)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        return Response(status=HTTP_200_OK)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def info(self, request):
        return Response({
            'id': 1,
            'email': 'j.doe@innopolis.ru',
            'location': 'RU',
            'contacts': {
                'address': 'Unsupported yet',
                'phone_number': '8(800)555-35-35',
                'additional_info': 'Unsupported yet',
                'first_name': 'Evgeny',
                'last_name': 'Baticov',
                'position': 'Driver helper',
                'company': 'Unsupported yet',
            }
        }, status=HTTP_200_OK)
