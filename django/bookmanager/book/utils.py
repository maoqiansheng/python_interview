from django.http import HttpResponse


def login_require(func_view):

    def wrapper(request,*args,**kwargs):
        if False:
            return func_view(request,*args,**kwargs)
        else:
            return HttpResponse("您没有登陆")
    return wrapper