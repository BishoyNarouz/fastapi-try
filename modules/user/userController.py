from fastapi import APIRouter

router = APIRouter()


router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],   # Guards
    # responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{id}")
async def read_users(id: int):
    return [{"username": "Rick"}, {"username": "Morty"}]
