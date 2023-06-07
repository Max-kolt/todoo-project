from fastapi import APIRouter
from src.schema import RegisterSchema, LoginSchema, ResponseSchema
from src.services.auth_service import AuthService

router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.post('/register', response_model=ResponseSchema, response_model_exclude_none=True)
async def register(request_body: RegisterSchema):
    token = await AuthService.register_service(request_body)
    return ResponseSchema(detail='Successfully save data!', result={'token_type': 'Bearer', 'access_token': token})


@router.post('/login', response_model=ResponseSchema)
async def login(request_body: LoginSchema):
    token = await AuthService.login_service(request_body)
    return ResponseSchema(detail='Successfully save data!', result={'token_type': 'Bearer', 'access_token': token})

