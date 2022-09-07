# Authentication
# Authorization
# Data Validation
# Error HANDLING
# Guard
# Structure
# Prisma Integration
# Virtual Packages
# env file  --------> Done
# Virtual Env   ------> Done
# Password Hashing and comparing --------> Done
# importing modules

from fastapi import FastAPI
from pydantic import BaseModel
from modules.user import userController
from modules.auth import authController
from dotenv import load_dotenv
load_dotenv(verbose=True)

app = FastAPI()

app.include_router(userController.router)
app.include_router(authController.router)
