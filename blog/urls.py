from django.urls import path
from . import views
from .views import (
   PostListView,
   PostDetailView,
   PostCreateView,
   PostUpdateView,
   PostDeleteView,
   UserPostListView
)

urlpatterns = [

   #  path('admin/', admin.site.urls),
   
   path('', PostListView.as_view(), name='blog-home' ),  # for home page we can let the url request, empty; we gonna directly assigning path)
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail' ),
   path('post/new/', PostCreateView.as_view(), name='post-create' ),       # template is post_form.html       <model>_<form>.html
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update' ),  # it will use post_form.html template, we dont need explicidly to create a new form
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete' ),  # now all it need is a template, and the template
   # this expects is just a form that asks if we are sure to delete the post, and if we submit the form, then the post
   # will be deleted. So, let's create this and its name be:- post_confirm_delete.html 
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts' ),


   path('about/', views.about, name='blog-about'),
   path('order/', views.order, name='blog-order'),
]









"""
         also in the third argument i am going to get the name of this path "blog-home"
            views.home is the function that we created at views.py file in this app, and returns httpResponse that we are 
            on the blog page
            and name is "blog-home" instead of home, because there will be times when we are gonna reverse look up of this 
            naming it as generally as "home" could collide with home file of different app routes

            now we have a url path for our blog home page mapped to our home function in the views file, but this 
            couldn't work quite yet, 
            because if we remember, we have urls.py file in our main  dir "django_project" as well
            and that url module will tell our whole website
            which urls  should sent us to our blog app

"""
