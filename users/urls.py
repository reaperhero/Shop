from django.conf.urls import url
from . import views

urlpatterns = [
    # 会员及个人中心等路由配置
    url(r'^login$', views.login, name="login"),
    url(r'^register$', views.register, name="register"),
    url(r'^logout$', views.logout, name="logout"),
]
