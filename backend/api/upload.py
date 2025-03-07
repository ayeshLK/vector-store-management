from fastapi import APIRouter, File, Form, Response, status, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/upload", status_code=status.HTTP_200_OK)
async def upload(
        request_id: str = Form(..., title="Request ID"),
        file: UploadFile = File(..., title="File")):
    """
    Process and store PDF files
    """
    return status.HTTP_201_CREATED
