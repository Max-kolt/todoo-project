from uuid import uuid4
from passlib.context import CryptContext

from src.repository.auth_repo import JWTRepo
from src.schema import *
from src.models.users import User
from src.repository.users import UserRepository
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    @staticmethod
    async def register_service(register: RegisterSchema):
        _user_id = str(uuid4())

        _user = User(
            id=_user_id,
            username=register.username,
            fname=register.fname,
            lname=register.lname,
            password=pwd_context.hash(register.password)
        )

        _username = await UserRepository.get_by_username(register.username)
        if _username:
            raise HTTPException(status_code=400,detail='Ussername already taken')
        else:
            await UserRepository.create(**_user.dict())
            return JWTRepo(data={'username': register.username}).generate_token()

    @staticmethod
    async def login_service(login: LoginSchema):
        password = await UserRepository.get_by_username(login.username)
        if password is not None:
            if not pwd_context.verify(login.password, password):
                raise HTTPException(status_code=400, detail='Invalid password!')
            return JWTRepo(data={'username': login.username}).generate_token()
        raise HTTPException(status_code=400, detail='Username not found!')

