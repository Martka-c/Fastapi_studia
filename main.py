from datetime import datetime

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.post("/token")
async def token(login_form: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": login_form.username + "_token"}


@app.get("/current_datatime")
async def index(token_value: str = Depends(oauth2_scheme)):
    return {"current_time": datetime.now()}


@app.get("/prime/{number}")
async def index(token_value: str = Depends(oauth2_scheme)):
    #MS TODO: here call processing method
    return {"ready_token": token_value}


@app.post("/picture/invert")
async def index(token_value: str = Depends(oauth2_scheme)):
    #MS TODO: here call processing method
    return {"ready_token": token_value}

