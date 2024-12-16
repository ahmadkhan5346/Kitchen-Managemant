from fastapi import FastAPI
from fastapi.responses import JSONResponse
import typing
import orjson
from app.urls import router as app_router



# Create the fast api app
class ORJsonResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content)
app = FastAPI(default_response_class=ORJsonResponse)


# Register app router
app.include_router(app_router)