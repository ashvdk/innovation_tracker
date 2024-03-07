from fastapi import APIRouter, Request

from routes.provider.filters import get_filters

router = APIRouter()

@router.post("/filters")
async def filters(request: Request):
    request_body = await request.json()
    filters_data = get_filters(request_body)
    return {
        "data": filters_data
    }