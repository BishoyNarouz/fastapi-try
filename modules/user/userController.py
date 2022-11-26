from fastapi import APIRouter

router = APIRouter()
from prisma.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],   # Guards
    # responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users():
    res = await User.prisma().find_many()
    print(res)
    return res
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{id}")
async def read_users(id: int):
    return [{"username": "Rick"}, {"username": "Morty"}]
