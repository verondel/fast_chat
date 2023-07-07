from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

# from src.auth.base_config import current_user
from src.database import get_async_session
from src.database import Client  # ???????????
from src.operations.models import message
from src.operations.schemas import MessageCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/opr")
async def get_specific_user(email: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Client).where(Client.email == email)
        result = await session.execute(query)
        return result.first()[0]
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


# @router.post("")
# async def add_message(new_operation: MessageCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(message).values(**new_operation.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}


@router.get("/main")
async def main(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(1))
    return result.all()
