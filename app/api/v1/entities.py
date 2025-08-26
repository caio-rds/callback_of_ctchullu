from fastapi import APIRouter

from app.models.entities import ResponseEntity
from app.services.entities import EntitiesService

router = APIRouter(prefix="/entities", tags=["entities"])


@router.get("/{_id}", response_model_exclude_none=True)
async def get_entity(_id: str):
    return await EntitiesService.get_entity(_id=_id)


@router.get("/", response_model=list[ResponseEntity], response_model_exclude_none=True)
async def get_entities():
    return await EntitiesService.get_entities()
