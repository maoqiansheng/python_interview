# 

def my_middleware(get_response):
    print('before_first_request')
    def middleware(request):
        print('before_request')
        response = get_response(request)
        print('after_request')
        return response
    return middleware