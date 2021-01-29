from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .utils import login_require
from .views import bookList, testproject, cookie, get_cookie, save_session, register
from . import views
from django.conf.urls import url,include
router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'books', views.BookInfoViewSet, basename=None)  # 向路由器中注册视图集

urlpatterns = [
    url(r'^',include(router.urls)),
    # 匹配书籍列表信息的URL,调用对应的bookList视图
    # url(r'^booklist/$', bookList, name='index'),
    # url(r'^testproject/$', testproject, name='test'),
    # url(r'^cookie/$', cookie, name='cookie'),
    # url(r'^get_cookie/$', get_cookie, name='get_cookie'),
    # url(r'^save_session/$', save_session, name='save_session'),
    # url(r'^register/$', views.Register.as_view(), name='register'),
    # url(r'^loader_index/$', views.loader_index, name='loader_index'),
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<id>\d+)$',views.BookDetailView.as_view()),
]
