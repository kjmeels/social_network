from fastapi import Request
from fastapi.responses import HTMLResponse

from .router import router
from src.settings import templating


@router.get(
    '/',
    response_class=HTMLResponse,
    name='social_network_index'
)
async def index(request: Request):
    return templating.TemplateResponse(
        'social_network/base.html',
        {'request': request}
    )

