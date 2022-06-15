from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile,Post
from .serializer import ProfileSerializer,PostSerializer
from rest_framework import status
from .forms import UpdateUserProfileForm
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts,})

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

def profile(request, username):
        user_prof = Post.get_Profile(username)
        if request.user == user_prof:
           return redirect('update_profile', username=request.user.username)

        return render(request, 'user_profile.html', {'user_prof': user_prof,})

def update_profile(request, username):
    profile= Profile.objects.get_or_create(user=request.user)
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        profile= Profile.objects.get_or_create(user=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'prof_form': prof_form,'images': images,})

def one_post(request,id):
    posts = Post.objects.filter(id=id).all()
    return render(request, 'one_post.html', {'posts': posts,})

def search_post(request):
    if 'search' in request.GET and request.GET['search']:
        name = request.GET.get("search")
        results = Post.search_post(name)
        message = f'name'
        loops = {
            'results': results,
            'message': message
        }
        return render(request, 'search_results.html', loops)
    else:
        message = "You haven't searched for any User"
    return render(request, 'search_results.html', {'message': message})