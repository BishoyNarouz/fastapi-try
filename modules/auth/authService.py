from modules.auth.dto.indexDto import LoginDto, RegisterDto
from modules.shared.services.bcryptService import PasswordService


class LoginService:

    async def login(self, loginDto: LoginDto):
        print(
            f'hashed password {PasswordService().hashPassword(loginDto.password)}')
        print(
            f'hashed password {PasswordService().comparePassword(loginDto.password, "$2b$12$ifnbMcHs12M0piVGUM071.5a2a7YHd6wM1RRMiN1VWMfW.nlixhme")}')
        return loginDto
