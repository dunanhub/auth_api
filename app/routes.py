from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.database import async_session
from app.models import User
from app.schemas import UserCreate, UserLogin

router = APIRouter()

async def get_session():
    async with async_session() as session:
        yield session

@router.post("/register")
async def register(user: UserCreate, session: AsyncSession = Depends(get_session)):
    query = await session.exec(select(User).where(User.username == user.username))
    excepted_user = query.first()

    if excepted_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = User(username=user.username, password=user.password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username}

@router.post("/login")
async def login(user: UserLogin, session: AsyncSession = Depends(get_session)):
    query = await session.exec(select(User).where(User.username == user.username))
    db_user = query.first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "username": db_user.username}
    