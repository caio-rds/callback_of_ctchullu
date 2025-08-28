from fastapi import APIRouter, HTTPException

from app.services.locations import LocationsService
from app.models.locations import ResponseLocation

router = APIRouter(prefix="/locations", tags=["locations"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseLocation | None)
async def get_location(_id: str):
    if location := await LocationsService.get_location(_id=_id):
        return location
    raise HTTPException(status_code=404, detail="No location found")

@router.get("/", response_model=list[ResponseLocation], response_model_exclude_none=True)
async def get_locations():
    if locations := await LocationsService.get_locations():
        return locations
    raise HTTPException(status_code=404, detail="No locations found")