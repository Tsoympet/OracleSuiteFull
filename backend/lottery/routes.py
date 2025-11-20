from fastapi import APIRouter
from . import service, service_favorites

router = APIRouter()
router.include_router(service.router)
router.include_router(service_favorites.router)
