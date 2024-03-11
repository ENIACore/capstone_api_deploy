from django.utils.deprecation import MiddlewareMixin

class CsrfTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if 'X_HTTP_CSRF' not in request.headers:

            csrf_token_cookie = request.COOKIES.get('csrftoken')
            
            if csrf_token_cookie:
                print("header not found, setting it")
                request.META['HTTP_X_CSRFTOKEN'] = csrf_token_cookie

