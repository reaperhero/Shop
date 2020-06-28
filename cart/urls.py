from django.conf.urls import url
from . import views

urlpatterns = [
    # 购物车路由
    url(r'^cart$', views.index, name='cart_index'),  # 浏览购物车
    url(r'^cart/add/(?P<gid>[0-9]+)$', views.add, name='cart_add'),  # 添加购物车
    url(r'^cart/del/(?P<gid>[0-9]+)$', views.delete, name='cart_del'),  # 从购物车中删除一个商品
    url(r'^cart/clear$', views.clear, name='cart_clear'),  # 清空购物车
    url(r'^cart/change$', views.change, name='cart_change'),  # 更改购物车中商品数量
]
