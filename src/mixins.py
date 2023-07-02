from fastapi.requests import Request


def info_mixin(request: Request):
    return {
        'request': request,
        'email': 'surname@gmail.com'
    }