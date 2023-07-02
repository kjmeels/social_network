from fastapi import APIRouter

from .views import router as view_router

router = APIRouter()
router.include_router(router=view_router)
