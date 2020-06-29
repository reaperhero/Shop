from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from common.models import Goods, Types
from common.views import loadinfo

def lists(request, page=1):
    '''商品列表页(搜索&分页)'''
    context = loadinfo(request) # 获取商品信息查询对象
    goods = Goods.objects

    # 根据类型id查询
    tid = request.GET.get('tid',None)
    if tid:
        goods = goods.filter(typeid=tid) # 根据typeid 查询goods

    # 关键字查询
    kw = request.GET.get('kw', None)
    if kw:
        # 过滤goods字段
        goods = goods.filter(goods__contains=kw)
    goods = goods.all()

    paginator = Paginator(goods, 4)  # 4以条每页创建分页对象
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数, 返回第一页。
        goods = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        goods = paginator.page(paginator.num_pages)
    except InvalidPage:
        # 如果请求的页数不存在, 重定向页面
        return HttpResponse('找不到页面的内容')

    # 封装信息加载模板输出
    context['goods'] = goods
    context['paginator'] = paginator
    return render(request, "goods/list.html", context=context)
    # 判断添加搜索条件
    """
    Paginator 类中有三个常用的属性，它们分别是:
        count: 表示所有页面的对象总数。 
        num_pages: 表示页面总数。
        page_range: 下标从 1 开始的页数范围迭代器

    Page 对象有三个常用的属性:
        object_list: 表示当前页面上所有对象的列表。
        numberv: 表示当前页的序号，从 1 开始计数。
        paginator: 当前 Page 对象所属的 Paginator 对象。

    Page 对象还拥有几个常用的函数: 
        has_next(): 判断是否还有下一页，有的话返回True。
        has_previous(): 判断是否还有上一页，有的话返回 True。
        has_other_pages(): 判断是否上一页或下一页，有的话返回True。
        next_page_number(): 返回下一页的页码。如果下一页不存在，抛出InvalidPage异常
        previous_page_number(): 返回上一页的页码。如果上一页不存在，抛出InvalidPage异常
    """



def detail(request, gid):
    '''商品详情页'''
    context = loadinfo(request)
    # 加载商品详情信息
    ob = Goods.objects.get(id=gid)
    ob.clicknum += 1  # 点击量加1
    ob.save()
    context['good'] = ob
    return render(request, "goods/detail.html", context)