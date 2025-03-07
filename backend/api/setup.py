from fastapi import APIRouter, Response
from model.setup import VectorStoreSetupRequest

router = APIRouter()


@router.post("/setup", response_class=Response, responses={200: {"description": "Success with no content"}})
async def setup(setup_req: VectorStoreSetupRequest):
    """
    Setup configurations for VectorDb
    """
    return Response(status_code=200)
