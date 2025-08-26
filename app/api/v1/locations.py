from fastapi import APIRouter

from app.services.locations import LocationsService
from app.models.locations import ResponseLocation

router = APIRouter(prefix="/locations", tags=["locations"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseLocation | None)
async def get_location(_id: str):
    return await LocationsService.get_location(_id=_id)

@router.get("/", response_model=list[ResponseLocation], response_model_exclude_none=True)
async def get_locations():
    return await LocationsService.get_locations()