from fastapi import APIRouter
from model.retrieve import VectorStoreRetrieveRequest, RetrieveResponse, Chunk

router = APIRouter()


@router.post("/retrieve", response_model=RetrieveResponse)
async def retrieve(retrieve_req: VectorStoreRetrieveRequest):
    """
    Retrieve information
    """
    return RetrieveResponse(query=retrieve_req.user_query, retrieved_chunks=[Chunk(text="txt1", source="src1")])
