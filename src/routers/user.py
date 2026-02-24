from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/users/me", tags=["user"])
async def read_users_me():
    return JSONResponse(content="test user me", status_code=200)

@router.post("/users/create", tags=["user"])
# add: user scheme for form
async def create_user():
    return JSONResponse(content="User created", status_code=200)



    

