import uvicorn
from fastapi_users import FastAPIUsers
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from src.auth.auth import auth_backend, fastapi_users, current_user
from src.models import Client as Use
from src.auth.schemas import UserRead, UserCreate
from src.models import Client as User

from src.pages.router import router as pages_router
from src.operations.router import router as operations_router
from src.chat.router import router as chat_router

app = FastAPI(
    title="vera's fast app"
)

# app.mount("/static", StaticFiles(directory="src/static"), name="static")

# проблемы с доступом в джой казино?
# if __name__ == "__main__":
#      uvicorn.run(app, host="127.0.0.1", port=8002)

# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(pages_router)
app.include_router(operations_router)
app.include_router(chat_router)

origins = [
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000/",
    "http://127.0.0.1:8000/pages/second",
    "http://127.0.0.1:8000/auth/jwt/login",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"
