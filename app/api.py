import httpx
from fastapi import APIRouter, UploadFile, File, HTTPException

from .config import settings

router = APIRouter()


@router.post("/moderate", status_code=200)
async def moderate_image(file: UploadFile = File(...)):
    if file.content_type not in settings.allowed_types:
        raise HTTPException(400, detail=f"File type {file.content_type} not allowed")

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                settings.api_url,
                files={"image": (file.filename, file.file, file.content_type)},
            )
        except httpx.RequestError as e:
            raise HTTPException(500, detail=f"Request error: {e.__class__.__name__}")

    if response.status_code != 200:
        raise HTTPException(500, detail="API error")

    result = response.json()
    if result["status"] == "OK":
        if result["data"]["nsfw"]:
            return {"status": "REJECTED", "reason": "NSFW content"}
        else:
            return {"status": "OK"}
