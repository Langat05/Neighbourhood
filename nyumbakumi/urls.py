from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('create/profile', views.create_profile, name='create-profile'),
    path('update/profile', views.update_profile, name='update-profile'),
    path('authorities', views.authorities, name='authorities'),
    path('health', views.health, name='health'),
    path('post',views.post, name='post'),
    path('new/post', views.new_post, name='new-post'),
    path('search', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)