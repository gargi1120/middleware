class jsonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.translation = {
            "english":{"greetings":"Hello", "header":"welcome django"},
            "Dutch":{"greetings":"Hallo", "header":"welkome django"}

        }

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        # print(request.META)
        if 'Dutch' in request.META["HTTP_ACCEPT_LANGUAGE"]:     # check dutch language asel tr    # jas aapan ekhadya website la gelyavar lnguage selec karato ts ethun language select hoil
            response.context_data = self.translation
            return response
        return response

