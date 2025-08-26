from fastapi import APIRouter

from app.services.grimmories import GrimmoriesService
from app.models.grimmories import ResponseGrimmories

router = APIRouter(prefix="/grimmories", tags=["grimmories"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseGrimmories | None)
async def get_grimmory(_id: str):
    return await GrimmoriesService.get_grimmory(_id=_id)

@router.get("/", response_model=list[ResponseGrimmories], response_model_exclude_none=True)
async def get_grimmories():
    return await GrimmoriesService.get_grimmories()
