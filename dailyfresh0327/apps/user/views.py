from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from .models import User
import re


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        if not all([username,password,email]):
            return render(request,'register.html',{'errmsg':'数据不全！'})

        if not re.match(r'',email):
            return render(request,'register.html',{'errmsg':'邮箱格式不对'})

        if allow !='on':
            return render(request,'register.html',{'errmsg':'请同意！'})

        try:
            username=User.objects.get(username=username)
        except User.DoesNotExist:
            user=None

        if user:
            return render(request,'register.html',{'errmsg':'用户已经存在！'})

        user=User.objects.create_user(username,email,password)
        user.is_active=False
        user.save()

        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)  # bytes
        token = token.decode()

        # 发邮件
        #send_register_active_email.delay(email, username, token)

        return redirect('goods:index')


class LoginView(View):
    def get(self,request):
        if 'username' in request.COOKIES:
            username=request.COOKIES.get('username')
            check='checked'

        else:
            username = ''
            checked = ''

        # 使用模板
        return render(request, 'login.html', {'username':username, 'checked':checked})

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        if not all([username, password]):
            return render(request, 'login.html', {'errmsg':'数据不完整'})

        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                response = redirect('goods:index')
                remember=request.POST.get('remember')
                if remember == 'on':
                    response.set_cookie('username',username,max_age=300)
                else:
                    response.delete_cookie('username')
                return response

            else:
                return render(request,'login.html',{'errmsg':'帐户未激活！'})
        else:
            return render(request,'login.html',{'errmsg':'用户名或密码错误!'})


class LogOutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('goods:index'))

class Test(View):
    def get(self,request):
        return HttpResponse('ooooooooooooooo')





























