from datetime import datetime

import primefac as primefac
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from error_types import BaseError
from prime_number_helper import PrimeNumber

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
prime_num_validator = PrimeNumber()


@app.post("/token")
async def token(login_form: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": login_form.username + "_token"}


@app.get("/current_datatime")
async def index(token_value: str = Depends(oauth2_scheme)):
    return {"current_time": datetime.now()}


@app.get("/prime/{number}")
async def index(number):
    try:
        prime_num_validator.validate_number(number)
        message = primefac.isprime(int(number))
    except BaseError as ex:
        return {"error": ex.message}
    return {"is_prime": message}


@app.post("/picture/invert")
async def index(token_value: str = Depends(oauth2_scheme)):
    #MS TODO: here call processing method
    return {"ready_token": token_value}

