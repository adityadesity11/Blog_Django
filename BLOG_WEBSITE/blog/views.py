from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Author,Post


# Create your views here.
def test(request):
    return render(request,"base.html")

def home(request):
    posts = Post.objects.all()
    print(posts)
    if request.user.is_authenticated:
        author = Author.objects.filter(user=request.user)     
        return render(request,'home.html',{'posts':posts, 'author':author[0]})
    
    return render(request,'home.html',{'posts':posts, 'author':None})
    


def post_page(request,pk):
    post = Post.objects.get(id=pk)
    if request.user.is_authenticated:
        author = Author.objects.filter(user=request.user)     
        return render(request,'post.html',{'post':post, 'author':author[0]})
    return render(request,'post.html',{'post':post,'author':None})

@login_required(login_url='home')
def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        author = Author.objects.filter(user=request.user)

        post = Post(author=author[0],title=title,body=body)
        post.save()
        return redirect('home')
    return redirect('home')

@login_required(login_url='home')
def my_blogs(request):
    author = Author.objects.filter(user = request.user)[0]
    posts = Post.objects.filter(author=author)
    print(request.user,author,posts)
    return render(request,'myblogs.html',{'posts':posts,'author':author})
@login_required(login_url='home')
def profile(request,pk):
    author = Author.objects.filter(user=request.user)[0]
    return render(request,'profile.html',{'author':author})


#Authenticcation:  
def register(request):
    if request.method == 'POST':
        data = request.POST
        username= data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        image = request.FILES['image']
        print(data)
       
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'username already taken!')
            return redirect('register')
        
        user = User.objects.create(
           first_name = first_name,
           last_name = last_name,            
           username = username       
        )
        user.set_password(password)
        user.save()
        name = first_name+" "+last_name
        author = Author(user=user,name=name,image=image)
        author.save()

    
        return redirect('login_page')
    return render(request,'register.html')


def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        print(data)
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.info(request,'username does not exist')
            return redirect('login_page')
        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Bad credentials!')
            return redirect('login_page')
        
        login(request,user)
        return redirect('home')
    return render(request,'login.html')




def logout_page(request):
    logout(request)
    return redirect('login_page')