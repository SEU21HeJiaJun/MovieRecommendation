# Create your views here.
from django.core import serializers
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic import View
from django.shortcuts import redirect,reverse, render
from libs.base_rander import render_to_response
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import Movie

class Login(View):
    def get(self,request):
        data={'error':''}
        return render_to_response(request,'dashboard/auth/login.html',data=data)

    def post(self,request):#登录逻辑
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        #判断当前用户输入的信息是否在数据库中
        user_exist = User.objects.filter(username=username).exists()
        SuperUser = User.objects.get(username=username).is_superuser
        data = {}

        if user_exist:
            if SuperUser == 1:
                return redirect('/admin/')

            if SuperUser == 0:
                auth_user = authenticate(username=username, password=password)
                if auth_user == None:
                    data['error'] = '用户密码错误'
                    return render_to_response(request, 'dashboard/auth/login.html',data=data)
                if auth_user != None:
                    login(request, auth_user)
                    serialized_user = serializers.serialize('json', [auth_user])
                    request.session['user'] = serialized_user
                    #这个地方将登陆的用户存入了对话，其他函数和文件加入一个request.session.get('user')语句即可调用
                    return redirect('dashboard_home')

        if not user_exist:
            data['error'] = '账号不存在'
            return render_to_response(request, 'dashboard/auth/login.html',data=data)

class LogoutUser(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('dashboard_login'))
    def post(self,request):
        pass

class Home(View):
    def get(self,request):
        data = {}
        return render_to_response(request,'dashboard/home.html',data=data)
    def post(self,request):
        pass

class Register(View):
    def get(self,request):
        return render_to_response(request, 'dashboard/auth/register.html', data={'error': ''})
    def post(self, request):
        username = request.POST.get('username','')
        password_1 = request.POST.get('password_1','')
        password_2 = request.POST.get('password_2','')
        print(username, password_1, password_2)
        data = {}
        if password_1 != password_2:
            data['error'] = '密码输入不一致，重新输入'
            return render_to_response(request, 'dashboard/auth/register.html', {'error': data})
        else:
            User.objects.create_user(password=password_1,is_superuser=0,username=username)
            return redirect(reverse('dashboard_login'))

def movie_introduction(request, movie_id):
    """介绍特定id电影的信息"""
    movie = Movie.objects.get(id=movie_id)
    if request.POST:
        movie.uid.add(request.user) #为电影增加点赞的用户
    context = {'movie': movie}
    return render(request, 'dashboard/MovieIntroduction.html', context)

def search(request):
    """搜索电影名字"""
    if request.POST:
        movie = Movie.objects.get(title=request.POST['wd'])
        return redirect('dashboard_MovieIntroduction', movie_id=movie.id)

    return render(request, 'dashboard/home.html')

def self_recommendation(request):
    """用户电影推荐算法"""
    #推荐算法返回movie的列表
    #return movies=[]
    movies = []
    context = {'movies': movies} #发送给模板
    return render(request, 'dashboard/SelfRecommendation.html', context)