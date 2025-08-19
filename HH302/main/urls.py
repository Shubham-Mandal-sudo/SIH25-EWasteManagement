from django.urls import path
from . import views

urlpatterns = [
    path('',views.hero_page, name='hero'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('mylist/',views.list_view, name = 'list_view'),
    path('create/',views.create_item, name='create_item'),
]