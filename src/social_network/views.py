from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse

from src.settings import templating

router = APIRouter(prefix='/views')


@router.get(
    '/index',
    response_class=HTMLResponse,
    name='index'
)
async def index(request: Request):
    return templating.TemplateResponse(
        'social_network/base.html',
        {'request': request}
    )
