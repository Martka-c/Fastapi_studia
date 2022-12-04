import os
from datetime import datetime

import primefac as primefac
import numpy as np
import cv2
from fastapi import FastAPI, Depends, UploadFile, File
from fastapi.openapi.models import Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.responses import FileResponse

from image_inversing_helper import ImageHelper
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

img = None

@app.post("/picture/invert")
async def index(file: UploadFile = File(...)):
    contents = await file.read()
    numpy_array = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)
    return_img = ImageHelper.process_image(img)

    _, encoded_img = cv2.imencode('.png', return_img)
    filepath = os.getcwd() + "/test_image.png"
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="image/jpeg", filename="test_image.png")
    return {"error": "error"}


@app.get("/inverted_image")
def get_image_endpoint():
    # img = ... # Create the image here
    return Response(img, mimetype="image/png")