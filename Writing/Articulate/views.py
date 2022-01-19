from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .form import *


# Create your views here.

def index(request):
    return render(request, 'Articulate/index.html')

def home(request):
    try:
        profiles = Profile.objects.all()
        stories = StoryModel.objects.all()
        return render(request, 'Articulate/home.html', {
            "profiles": profiles,
            "stories": stories
        })
    except Exception as e:
        print(e)
    render(request, 'Articulate/home.html')




    # context = {'stories': StoryModel.objects.all()}
    # return render(request, 'Articulate/home.html', context)

def login_view(request):
    # if request.method == "POST":
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return HttpResponseRedirect(reverse("explore"))
    #     else:
    #         return render(request, "Articulate/login.html", {
    #             "message": "Invalid credentials."
    #         })
    return render(request, 'Articulate/login.html')

def register(request):
    # if request.method == "POST":
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     user = User.objects.filter(username = username).first()
    #     if user is None:
    #         user = User.objects.create(username = username)
    #         user.set_password(password)
    #         user.save()
    #         return HttpResponseRedirect(reverse("explore"))
    #     else:
    #         return render(request, "Articulate/register.html", {
    #             "message": "Username already taken"
    #         })
    return render(request, 'Articulate/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def explore(request):
#     genre = {}
#     genres = GenreModel.objects.all()
#     for g in genres:
#     #     genre[g] = (g.story)
#         genre_story = GenreModel.objects.filter(genre = g)
#         genre[g] = genre_story
#         print(genre_story)
#     print(genre.values, '\n\n')
    genres = {}

    for genre in GenreModel.objects.all():
        genres[genre] = []
        for story in genre.story.all():
            genres[genre].append(story)
        #     print(story)
    #     print('genre: ', genres[genre], genre)
    # print('genres: ', genres)
    # print(genres)
    context = {
        # 'stories': StoryModel.objects.all(),
        'genres': genres
    }
    return render(request, 'Articulate/explore.html', context)

def write(request):

    if request.user.is_authenticated:

        context = {'form': StoryForm}

        try:

            if request.method == 'POST':
                # print("hello0")
                form = StoryForm(request.POST)
                image = request.FILES['image']
                title = request.POST.get('title')
                user = request.user
                if form.is_valid():
                    genres = form.cleaned_data['genre']
                    # print("genres", genres)

                    
                    content = form.cleaned_data['content']
                    # print("hello2")

                    # print(content)
                story = StoryModel.objects.create(
                    user = user, title = title, content = content, image = image
                )

                # print("story id" , story.id)
                # print(genres)
                for genre in genres:
                    # g = GenreModel.objects.create(genre = genre, story = story.id)
                    # g.save()
                    # print("hello4")
                    # print(g)
                    gen = GenreModel.objects.filter(genre = genre).first()
                    # print("gen model", gen, "genModel")
                    # if len(gen) == 0:
                    #     g = GenreModel.objects.create(genre = genre)
                    #     g.story.add(story)
                    #     g.save()
                    # else:
                    gen.story.add(story)
                    


                # print("hello3")
                # print(story)
                return redirect('see_story')

        except Exception as e:
            print(e)
        return render(request, "Articulate/write.html", context)
    else:
        return redirect('login')

def story_detail(request, slug):
    context = {}
    try:
        story = StoryModel.objects.filter(slug = slug).first()
        context['story'] = story

    except Exception as e:
        print(e)
    return render(request, 'Articulate/story_detail.html' , context)

def see_story(request):
    context = {}
    try:
        story_objs = StoryModel.objects.filter(user = request.user)
        context['story_objs'] = story_objs
    except Exception as e:
        print(e)
    return render(request, 'Articulate/see_story.html', context)

def delete_story(request, id):
    if request.user.is_authenticated:
        try:
            story_obj = StoryModel.objects.get(id = id)
            if story_obj.user == request.user:
                story_obj.delete()
        except Exception as e:
            print(e)  

        return HttpResponseRedirect(reverse("see_story"))
    else:
        return redirect('login')


def update_story(request, slug):
    if request.user.is_authenticated:

        context = {}
        try:
        
            story_obj = StoryModel.objects.get(slug = slug)
        
            if story_obj.user != request.user:
                return HttpResponseRedirect(reverse("home"))

            initial_dict = {'content': story_obj.content}
            form = StoryForm(initial = initial_dict)

            if request.method == 'POST':
                
                form = StoryForm(request.POST)
                image = request.FILES['image']
                title = request.POST.get('title')
                user = request.user
                
                if form.is_valid():
                    genres = form.cleaned_data['genre']
                    content = form.cleaned_data['content']
                    
                story = StoryModel.objects.create(
                    user = user, title = title, content = content, image = image
                )
                for genre in genres:
                    gen = GenreModel.objects.filter(genre = genre).first()
                    gen.story.add(story)
                
                return redirect('write')


            context['story_obj'] = story_obj
            context['form'] = form

        except Exception as e:
            print(e)  

        return render(request, 'Articulate/update_story.html', context)
    
    else:
        return redirect('login')

def profile(request, username):
    print(username)
    # story_objs = StoryModel.objects.filter(user = request.user)
    context = {}
    try:
        
        user = User.objects.filter(username = username).first()
        # print("bye")
        story_objs = StoryModel.objects.filter(user = user)
        # print("hello0")
        profile = Profile.objects.filter(user = user)
        # print("hello4")
        # print("Hello..............", profile)
        # print("Bye................",story_objs)
        context['story_objs'] = story_objs
        
        context['profiles'] = profile
        # print("hello1")
        context['user'] = user
        # print("Hello2")
        # print(context)
    except Exception as e:
        print(e)
    return render(request, 'Articulate/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        # image = request.POST["image"]
        e_profile = Profile.objects.filter(user = request.user).first()
        about_me = request.POST['about_me']
        e_profile.about_me = about_me
        # print(about_me)
        e_profile.image = request.FILES['image']
       
        e_profile.save()
        #print(profile.user)
        
        
        # profile_url = reverse('profile', args = profile.user.username)
        # print(request.user.username)
        return profile(request, request.user.username)
    else :
        return render(request, 'Articulate/edit_profile.html')