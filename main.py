# Authentication
# Authorization
# Guard
# sqlAlchemy Integration
# Data Validation  ------> Done
# Error HANDLING   -------> Done
# Structure -----> Done
# Virtual Packages --------> Done
# env file  --------> Done
# Virtual Env   ------> Done
# Password Hashing and comparing --------> Done
# importing modules
# global prefix
# seeders
# prisma upgrade to 4.6.1

import os

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


from prisma import Prisma

prisma = Prisma(auto_register=True)


@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


app.include_router(userController.router, prefix=os.getenv("GLOBAL_PREFIX"))
app.include_router(authController.router, prefix=os.getenv("GLOBAL_PREFIX"))
