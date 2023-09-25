from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login_page'),
    path('logout',views.logout_page,name='logout_page'),
    path('posts/<str:pk>',views.post_page,name='post_page'),
    path('add-blog',views.add_blog,name='add-blog'),
    path('my-blogs',views.my_blogs,name='my_blogs'),
    path('author/<str:pk>',views.profile,name='profile'),
]