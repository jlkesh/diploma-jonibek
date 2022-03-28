from fastapi import APIRouter
from fastapi.exceptions import RequestValidationError


router = APIRouter(tags=['Exception Handler'])


# @router.exception_handler(RequestValidationError)
# def validation_exception_handler(request, exc):
#     print(exc)
#     return JSONResponse(content={'error':str(exc)}, status_code=400)
