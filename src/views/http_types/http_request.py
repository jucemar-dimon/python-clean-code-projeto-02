class HttpRequest:
    def __init__(self, body: dict = None, param: dict = None) -> None:
        self.param = param
        self.body = body
