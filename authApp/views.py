from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def register(request):
    """Registers users and sends token to them
    :param request: HttpRequest
    :return: JSON
    """
    serializer = UserSerializer(data=request.data)
    # return response with 400 status and json details if data is not valid
    serializer.is_valid(raise_exception=True)
    # create user
    user = serializer.create_user()

    token = Token.objects.get(user=user)
    return Response({'token': token.key})
