"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


note: This is where we setup the mapping from certain urls to where we sent the users


"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # in it we are gona tell django which route should get mapped to our blog urls, for this we are going to 
    # import another function from django.urls and that is include function
    # now we can add in the list of urlpatterns, to specify, which route should to our blog urls 
    # so we go here
    path('', include('blog.urls')),  # handles all request for blog app that we created

    path('register/', user_views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.htm'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.htm'), name='logout'),

    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.htm'),
        name='password_reset'),
    
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.htm'),
        name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.htm'),
        name='password_reset_confirm'),

    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.htm'),
        name='password_reset_complete'),
        
    path('profile/', user_views.profile, name='profile'),


    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




"""
1- if we want to make blog as the home page of our website
    then put empty sting on the path of 'blog/', then we get blog page as the home page of our website

2- 
"""