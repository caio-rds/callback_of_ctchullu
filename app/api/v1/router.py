from fastapi import APIRouter
import app.api.v1.entities as entities
import app.api.v1.locations as locations
router = APIRouter()

router.include_router(entities.router)
router.include_router(locations.router)