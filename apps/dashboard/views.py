# Create your views here.
from django.views.generic import View
from django.shortcuts import redirect,reverse,render
from django.contrib.auth.hashers import make_password
from libs.base_rander import render_to_response
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.db import models
from django.core.paginator import Paginator

class Login(View):
    def get(self,request):
        data={'error':''}
        return render_to_response(request,'dashboard/auth/login.html',data=data)

    def post(self,request):#登录逻辑
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        #判断当前用户输入的信息是否在数据库中
        user_exist = User.objects.filter(username=username).exists()
        data = {}

        if user_exist == 1 and User.is_superuser == 1:
            user = authenticate(username=username, password=password)
            if not user:
                data['error'] = '管理员密码错误'
                return render_to_response(request, 'dashboard/auth/login.html', data=data)
            if user.is_authenticated:
                login(request, user)
                return redirect(reverse('dashboard_admin'))

        if user_exist == 1 and User.is_superuser == 0:
            auth_user = authenticate(username=username, password=password)
            if not auth_user:
                print(auth_user)
                data['error'] = '用户密码错误'
                return render_to_response(request, 'dashboard/auth/login.html',data=data)
            if auth_user.is_authenticated:
                login(request, auth_user)
                return redirect(reverse('dashboard_home'))

        if user_exist == 0 :
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

class Admin(View):
    def get(self,request):
        data = {}
        return render_to_response(request,'dashboard/auth/admin.html',data=data)
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

# class AdminManager(View):
#     def get(self,request):
#         if request.user.is_authenticated:
#             users = User.objects.all()
#             # 获取当前页面的页数，默认是第一页
#             page = request.GET.get('page',1)
#             # 设置页面显示数据的数量
#             p = Paginator(users, 2)
#             # 获取总页数
#             total_page = p.num_pages
#             # 防止用户输入的页数为负数
#             if int(page) <= 1:
#                 page = 1
#             # 获取当前也米娜对应的数据
#             current_page = p.get_page(int(page)).object_list
#             print(current_page)
#
#             data = {'users': current_page, 'total':total_page,'page_num':int(page)}
#             return render_to_response(request, 'dashboard/auth/admin.html', data=data)
#
#         else:
#             return redirect(reverse('dashboard_login'))
#
# class UpdateAdminStatus(View):
#     def get(self,request):
#         status = request.GET.get('status','on')
#         _status = True if status == 'on' else False
#         user_id = request.GET.get('id',None)
#         if user_id != None:
#             user = User.objects.filter(pk=user_id).first()
#             user.is_superuser = _status
#             user.save()
#         # request.user.is_superuser = _status
#         # request.user.save()
#         return redirect(reverse('admin_manager'))
#
#     def post(self,request):
#         pass
#
# class UserList(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             users = User.objects.all()
#             # 获取当前页面的页数，默认是第一页
#             page = request.GET.get('page', 1)
#             # 设置页面显示数据的数量
#             p = Paginator(users, 2)
#             # 获取总页数
#             total_page = p.num_pages
#             # 防止用户输入的页数为负数
#             if int(page) <= 1:
#                 page = 1
#             # 获取当前页面对应的数据
#             current_page = p.get_page(int(page)).object_list
#             print(current_page)
#
#             data = {'users': current_page, 'total': total_page, 'page_num': int(page)}
#             return render_to_response(request, 'dashboard/auth/users_list.html', data=data)
#
#         else:
#             return redirect(reverse('dashboard_login'))