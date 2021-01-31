from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', ])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registration Successful"})
    else:
        return Response(serializer.errors)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def posts(request):
    posts = Post.objects.values()
    return JsonResponse(list(posts), safe=False)


def home(request):
    return render(request, 'home/index.html', {})
