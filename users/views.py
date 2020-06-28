from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.urls import reverse
from common.models import Users


def login(request):
    '''会员登录表单'''
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        try:
            print(request.POST)
            print(request.POST['username'])
            # 根据账号获取登录者信息
            user = Users.objects.get(username=request.POST['username'])
            # 判断当前用户是否是后台管理员用户
            if user.state == 0 or user.state == 1:
                if user.password == request.POST['password']:
                    # 此处登录成功，将当前登录信息放入到session中，并跳转页面
                    request.session['vipuser'] = user.toDict()
                    print('ok')
                    return redirect(reverse('index'))
                else:
                    context = {'info': '登录密码错误!'}
                    print(context)
            else:
                context = {'info': '此用户为非法用户!'}
                print(context)
        except:
            context = {'info': '登录账号错误!'}
            print(context)
        return render(request, "users/login.html", context)

def logout(request):
    '''会员退出'''
    # 清除登录的session信息
    del request.session['vipuser']
    # 跳转登录页面(url地址改变)
    return redirect(reverse('login'))

# 类似登录， 编写逻辑
def register(request):
    return HttpResponse("注册")
