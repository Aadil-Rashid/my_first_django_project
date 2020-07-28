
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.htm', context)

    
    """
        # return HttpResponse('<h1>You are in blog applcation, in side the Home, this is what we want you to see</h1>')

        this is the logic for how we want to handle when a  user goes to our blog's home page
        but we have not actually maped our url  pattern,  to this view function yet , 
        so to do this , 
        We are going to create new bolg module  in our blog directory called "urls.py" and in that file is where we 
        map the url that we want to corrospond to each view function
        so lets do that now 
    """
def about(request):
    return render(request, 'blog/about.htm', {'title': 'About'})

    # return HttpResponse('<h1> Blog - About page that we want you to see </h1>')

 
def order(request):
    return render(request, 'blog/order.htm')

    # return HttpResponse('<h1>This is our order page of our website</h1>')

# let us create now class based views, these views have a lot of backend defined and we
# can use alot of its methods as it has a lot of buildin functionality.
"""
there are different kinds of class based views:-
e.g; list views, detail views, create views, update views and delete views, etc...


"""


class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'     
    template_name = 'blog/user_posts.htm'   # <app>/<model>_<viewtype>.html
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    template_name = 'blog/home.htm'   # <app>/<model>_<viewtype>.html
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
   

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

       
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'   # '/' stands for home directory... like it is convention

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False







   

"""

blog/post_list.html
it means
             <app>/<model>_<viewtype>.html

in case of function based views, we have   'posts' , 
but in case of class based view , we have  'object list' instead of posts... its by default 


"""



""" 
1    first of all we will handle this views of our newely created app

"""

# 2
# Create your views here.

# Now we are going to create new function here. and i am going to call this function "home"
#  and this funtion is going to handle the traffic from the home page of our blog and this function 
# gona tare "request argument" , we are not going to use request variable just yet but we need to add this to just 
# get our function to work 
# and in this function, we are simply going to      return   "what we want user to see"
#  when they are sent to this route.

"""
posts = [
    {
        'author': 'Aadil Rashid',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'December 1, 2020'
    },
    {
        'author': 'Aaquib Rashid',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 2, 2020'
    }
]

"""
