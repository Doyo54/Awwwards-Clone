from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile,Post
from .serializer import ProfileSerializer,PostSerializer
from rest_framework import status
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    
    return render(request, 'index.html')

class PostView(APIView):
    def get(self, request, format=None):
        all_merch = Post.objects.all()
        serializers =PostSerializer(all_merch, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)