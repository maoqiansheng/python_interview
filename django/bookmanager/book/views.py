import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django_redis import get_redis_connection
from django.urls import reverse
# Create your views here.
# from django.bookmanager.book.utils import login_require
# from django.bookmanager.book.models import BookInfo
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo


def testproject(request):

    return HttpResponse("test")


def bookList(request):
    print(request.META)
    # url = reverse('book:test')
    # print(url)
    # context = {'v1': value1, 'v2': value2}
    # print(context)
    # HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)
    return JsonResponse({'city': 'beijing', 'subject': 'python', 'status': 400})

def cookie(request):
    response = HttpResponse('ok')
    response.set_cookie('cookie1', 'python2', max_age=3600)  # 有效期一小时
    return response

def get_cookie(request):
    cookies = request.COOKIES.get('cookie1')
    print(cookies)
    return JsonResponse({"cookie":cookies})

def save_session(request):
    request.session['mao'] = 'qiansheng'
    return JsonResponse({"status": 200})

def register(request):
    """处理注册"""

    # 获取请求方法，判断是GET/POST请求
    if request.method == 'GET':
        # 处理GET请求，返回注册页面
        return JsonResponse({'register': '注册页面'})
    else:
        # 处理POST请求，实现注册逻辑
        return HttpResponse('这里实现注册逻辑')

# 类视图
# @method_decorator(login_require, name='dispatch')
class Register(View):
    def get(self, request):
        return HttpResponse('ok')
    def post(self, requset):
        return HttpResponse('ok')

def loader_index(request):
    context = {
        'city': '北京',
        'adict': {
            'name': '西游记',
            'author': '吴承恩'
        },
        'alist': [1, 2, 3, 4, 5]
    }
    return render(request, 'index.html', context)

class BookListView(View):
    """
    图书列表
    """
    def get(self,request):
        """
                查询所有图书
                路由：GET /books/
                """

        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                'id': book.id,
                'name': book.name,
                'pub_date': book.pub_date
            })
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """
        新增图书
        路由：POST /books/
        """
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处详细的校验参数省略

        book = BookInfo.objects.create(
            name=book_dict.get('name'),
            pub_date=book_dict.get('pub_date')
        )

        return JsonResponse({
            'id': book.id,
            'name': book.name,
            'pub_date': book.pub_date
        }, safe=False)



class BookDetailView(View):
    """
    获取单个图书信息
    修改图书信息
    删除图书
    """
    def get(self, request, id):
        """
        获取单个图书信息
        路由： GET  /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': book.id,
            'name': book.name,
            'pub_date': book.pub_date
        })

    def put(self, request, id):
        """
        修改图书信息
        路由： PUT  /books/<pk>
        """
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处详细的校验参数省略

        book.name = book_dict.get('name')
        book.pub_date = book_dict.get('pub_date')
        book.save()

        return JsonResponse({
            'id': book.id,
            'name': book.name,
            'pub_date': book.pub_date
        })

    def delete(self, request, id):
        """
        删除图书
        路由： DELETE /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer