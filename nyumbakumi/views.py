from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)


@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    return render(request,'user_profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)

    return render(request,'user_profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request,'profile_form.html',{"form":form})  

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form})  

@login_required(login_url='/accounts/login/')
def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    authorities = Authorities.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'authorities.html',{"authorities":authorities})   

@login_required(login_url='/accounts/login/')
def health(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    health = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'health.html',{"health":health})     

@login_required(login_url='/accounts/login/')
def post(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    posts = Post.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'post.html',{"posts":posts})      

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.username = current_user
            post.neighbourhood = profile.neighbourhood
            post.avatar = profile.avatar
            post.save()

        return HttpResponseRedirect('/post')

    else:
        form = PostForm()

    return render(request,'post_form.html',{"form":form})    
    

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_post(search_term)
        message=f"{search_term}"

        print(searched_posts)

        return render(request,'search.html',{"message":message,"posts":searched_posts})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})    