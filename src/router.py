from fastapi import APIRouter
from social_network.router import router as social_network_router

router = APIRouter(prefix='/api')
router.include_router(router=social_network_router)
