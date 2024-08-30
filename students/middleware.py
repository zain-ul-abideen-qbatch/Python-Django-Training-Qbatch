class SimpleLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code executed for each request before the view is called
        
        print(f"Request Method: {request.method}, Request Path: {request.path}  and I'm called before going to the View")

        response = self.get_response(request)

        # Code executed for each response after the view is called
        print(f"Response Status Code: {response.status_code} and I'm called after view is called")

        return response
