from fastapi import APIRouter

from api.main import router as main_router
from api.rates import router as rates_router

init_router = APIRouter()

init_router.include_router(main_router)
init_router.include_router(rates_router)
