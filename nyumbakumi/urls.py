from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('create/profile', views.create_profile, name='create-profile'),
    path('update/profile', views.update_profile, name='update-profile'),
    path('authorities', views.authorities, name='authorities'),
    path('health', views.health, name='health')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)