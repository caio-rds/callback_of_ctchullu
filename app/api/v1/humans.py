from fastapi import APIRouter, HTTPException

from app.models.entities import ResponseEntity
from app.services.humans import HumansService

router = APIRouter(prefix="/humans", tags=["humans"])

@router.get("/{_id}", response_model_exclude_none=True, response_model=ResponseEntity | None)
async def get_human(_id: str):
    if human := await HumansService.get_humans():
        return human
    raise HTTPException(status_code=404, detail="Human not found")

@router.get("/", response_model=list[HumansService], response_model_exclude_none=True)
async def get_grimmories():
    if humans := await HumansService.get_humans():
        return humans
    raise HTTPException(status_code=404, detail="No humans found")
