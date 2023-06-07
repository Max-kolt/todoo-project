from datetime import timedelta, datetime

from jose import jwt
from typing import Optional
from config import ALGORITHM, SECRET_KEY

from fastapi import Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials


class JWTRepo:
    def __init__(self, data: dict = {}, token: str = None) -> None:
        self.data = data
        self.token = token

    def generate_token(self, expires_delta: Optional[timedelta] = None):
        to_encode = self.data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return encode_jwt

    def decode_token(self):
        try:
            decode_token = jwt.decode(self.token, SECRET_KEY, algorithms=[ALGORITHM])
            return decode_token if decode_token["expires"] >= datetime.time() else None
        except Exception:
            return {}

    @staticmethod
    def extract_token(token: str):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


"""class JWTBearer(HTTPException):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(detail={auto_error: auto_error})

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403,
                    detail={'status': 'Forbidden', 'message': 'Invalid authenticational schema.'}
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403,
                    detail={'status': 'Forbidden', 'message': 'Invalid or expired token.'}
                )
        else:
            raise HTTPException(
                status_code=403,
                detail={'status': 'Forbidden', 'message': 'Invalid authorization code.'}
            )

    @staticmethod
    def verify_jwt(jwt_token: str):
        return True if jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM]) is not None else False"""
