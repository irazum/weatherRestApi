from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def rest_urls(request, url):
    return Response({"cod": "404", "message": "Resource could not be found"}, status=404)
