from fastapi import APIRouter, Response, status
from model.setup import VectorStoreSetupRequest

router = APIRouter()


@router.post("/setup")
async def setup(setup_req: VectorStoreSetupRequest):
    """
    Setup configurations for VectorDb
    """
    return status.HTTP_200_OK
