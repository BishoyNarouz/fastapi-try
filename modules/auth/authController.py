from fastapi import APIRouter
from modules.auth.dto.indexDto import LoginDto, RegisterDto
from modules.auth.authService import login

router = APIRouter()

router = APIRouter(
    prefix="/auth",
    tags=["users"]
)


@router.post("/login")
async def login(loginDto: LoginDto):
    return loginDto


@router.post("/register")
async def register(registerDto: RegisterDto):
    return registerDto
