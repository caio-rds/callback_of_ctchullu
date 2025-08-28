from fastapi import APIRouter, HTTPException

from app.models.entities import ResponseEntity
from app.services.entities import EntitiesService

router = APIRouter(prefix="/entities", tags=["entities"])


@router.get("/{_id}", response_model_exclude_none=True)
async def get_entity(_id: str):
    if entity := await EntitiesService.get_entity(_id=_id):
        return entity
    raise HTTPException(status_code=404, detail="Entity not found")


@router.get("/", response_model=list[ResponseEntity], response_model_exclude_none=True)
async def get_entities():
    if entities := await EntitiesService.get_entities():
        return entities
    raise HTTPException(status_code=404, detail="No entities found")
