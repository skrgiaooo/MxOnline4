from django.contrib.auth import authenticate, login
#django中自带密码验证
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from apps.users.form import LoginForm
from django.views.generic.base import View
class LoginView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "login.html")

    def post(self, request,*args, **kwargs ):
        # 表单验证
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            # 用于通过用户和密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=password)
            # 1. 通过用户名查询到用户
            # 2. 需要先加密再通过加密之后的密码查询
            if user is not None:
                # 查询到用户
                login(request, user)

                return HttpResponseRedirect(reverse("index"))
                # 登陆成功以后，返回首页
                # return HttpResponse('ok')
            else:
                # 未查询到用户
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})

        else:
            return render(request, "login.html", {"login_form": login_form})