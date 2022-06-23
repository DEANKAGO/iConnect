from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from connect.views import profileCatfishToggle


urlpatterns = [
  # path('pp', views.pp, name='search_form'),
  # path('search/', views.search_profile, name='search'),
  # path('', views.index, name ='index'),
  # path('home/', views.home, name ='home'),
  # path('register/',views.register,name='register'),
  # path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
  # path('login/', auth_views.LoginView.as_view(template_name='django_registration/login.html'),name='login'),
  # path('profile/<int:profile_id>/',views.profile,name='profile'),
  # path('update_profile/<int:profile_id>/', views.update_profile, name='update_profile'),

    
  path('', views.index, name ='index'),
  path('home/', views.home, name ='home'),
  path('register/',views.register,name='register'),
  path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
  path('login/', auth_views.LoginView.as_view(template_name='django_registration/login.html'),name='login'),
  path('profile/<int:profile_id>/',views.profile,name='profile'),
  path('update_profile/', views.update_profile, name='update_profile'),
  path('user/<id>/catfish', profileCatfishToggle.as_view(), name='catfished'),
  path('like', views.catfish_profile, name='catfish_profile'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  
# urlpatterns = [
#     path('', views.index, name ='index'),
#     path('home/', views.home, name ='home'),
#     path('register/',views.register,name='register'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
#     path('login/', auth_views.LoginView.as_view(template_name='django_registration/login.html'),name='login'),
#     path('profile/<int:profile_id>/',views.profile,name='profile'),
#     path('update_profile/<int:profile_id>/', views.update_profile, name='update_profile'),
# ]

