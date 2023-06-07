from fastapi import APIRouter, Depends
from fastapi.security import  HTTPAuthorizationCredentials

from src.repository.auth_repo import JWTRepo
from src.schema import RegisterSchema, LoginSchema, ResponseSchema
from src.repository.records import RecordRepository


router = APIRouter(prefix='/record', tags=['record'])


@router.get('/{username}', response_model=ResponseSchema)
async def get_user_records(username: str):
    pass