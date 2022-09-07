from fastapi import APIRouter
from .dto import registerDto
router = APIRouter()

router = APIRouter(
    prefix="/auth",
    tags=["users"]
)


@router.get("/login")
async def login():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/register")
async def register(registerDto: registerDto.Register):
    return registerDto

