from django.urls import path
from . import views

urlpatterns = [
    path('',views.hero_view, name = 'hero'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('home/mylist/',views.list_view, name = 'list_view'),
    path('home/mylist/create/',views.create_item, name='create_item'),
    path('recycler/',views.recycler_home, name='recycler'),
]