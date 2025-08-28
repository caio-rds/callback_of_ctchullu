from fastapi import APIRouter, HTTPException

from app.services.grimmories import GrimmoriesService
from app.models.grimmories import ResponseGrimmories

router = APIRouter(prefix="/grimmories", tags=["grimmories"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseGrimmories | None)
async def get_grimmory(_id: str):
    if grimmory := await GrimmoriesService.get_grimmory(_id):
        return grimmory
    raise HTTPException(status_code=404, detail="Grimmory not found")

@router.get("/", response_model=list[ResponseGrimmories], response_model_exclude_none=True)
async def get_grimmories():
    if grimmories := await GrimmoriesService.get_grimmories():
        return grimmories
    raise HTTPException(status_code=404, detail="No grimmories found")
