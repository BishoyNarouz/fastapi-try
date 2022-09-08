from modules.auth.dto.indexDto import LoginDto, RegisterDto


async def login(loginDto: LoginDto):
    print(loginDto.password)
    return loginDto.password
