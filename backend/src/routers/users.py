from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials

from src.repository.auth_repo import JWTRepo
from src.schema import RegisterSchema, LoginSchema, ResponseSchema
from src.repository.users import UserRepository


router = APIRouter(prefix='/user', tags=['user'])


#Получение пользователя по токену
@router.get('/', response_model=ResponseSchema, response_model_exclude_none=True)
async def get_user(credentials: HTTPAuthorizationCredentials):
    token = JWTRepo().extract_token(credentials.credentials)
    result = UserRepository.get_by_username(token['username'])
    return ResponseSchema(detail='Successfully fetch data!', result=result)
