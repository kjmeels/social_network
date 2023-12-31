from pathlib import Path

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .mixins import info_mixin
from .types import Settings

BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS = Settings()

templating = Jinja2Templates(
    directory=BASE_DIR / 'templates',
    context_processors=[info_mixin]
)
static = StaticFiles(directory='static')
media = StaticFiles(directory=BASE_DIR / 'media')
