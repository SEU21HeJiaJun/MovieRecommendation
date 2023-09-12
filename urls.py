from django.urls import path
from . import views
from .views import Login,LogoutUser,Register,Home

urlpatterns = [
    path('login/',Login.as_view(),name='dashboard_login'),
    path('logout/',LogoutUser.as_view(),name='dashboard_logout'),
    path('register/',Register.as_view(),name='dashboard_register'),
    path('home/',views.search,name='dashboard_home'),
    path('SelfRecommendation/',views.self_recommendation,name='dashboard_SelfRecommendation'),
    path('MovieIntroduction/<int:movie_id>',views.movie_introduction,name='dashboard_MovieIntroduction'),
]