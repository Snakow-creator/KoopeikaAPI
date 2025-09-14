from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse, StreamingResponse

router = APIRouter()


def iterfile(filename: str):
    with open(filename, 'rb') as f:
        while chunk := f.read(1024 * 1024):
            yield chunk


@router.get("/files/streaming/{filename}")
async def fileroot(filename: str):
    return StreamingResponse(iterfile(filename), media_type="video/mp4")
