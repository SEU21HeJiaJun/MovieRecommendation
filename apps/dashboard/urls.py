from django.urls import path
from .views import Login,LogoutUser,Register,Home,Admin
urlpatterns = [
    path('login/',Login.as_view(),name='dashboard_login'),
    path('logout/',LogoutUser.as_view(),name='dashboard_logout'),
    path('register/',Register.as_view(),name='dashboard_register'),
    path('home/',Home.as_view(),name='dashboard_home'),
    path('admin/',Admin.as_view(),name='dashboard_admin')
    #path('SelfRecommendation/,,name='dashboard_SelfRecommendation'),
    #path('MovieIntroduction/',,name='dashboard_MovieIntroduction'),
]