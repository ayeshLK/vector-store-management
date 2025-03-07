from fastapi import APIRouter, File, Form, Response, UploadFile

router = APIRouter()


@router.post("/upload", response_class=Response, responses={200: {"description": "Success with no content"}})
async def upload(
        request_id: str = Form(..., title="Request ID"),
        file: UploadFile = File(..., title="File")):
    """
    Process and store PDF files
    """
    return Response(status_code=200)
