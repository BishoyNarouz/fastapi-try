# Authentication
# Authorization
# Data Validation
# Error HANDLING
# Guard
# Structure -----> Done
# Prisma Integration
# Virtual Packages
# env file  --------> Done
# Virtual Env   ------> Done
# Password Hashing and comparing --------> Done
# importing modules

from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from modules.user import userController
from modules.auth import authController
from dotenv import load_dotenv

load_dotenv(verbose=True)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"{exc}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {
                "statusCode": 400,
                "status": False,
                "errors": exc.errors(),
                "body": exc.body
            }
        ),
    )


app.include_router(userController.router)
app.include_router(authController.router)
