import os
from datetime import datetime

from typing import Any, Union

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
async def token(login_form: OAuth2PasswordRequestForm = Depends()) -> dict[str, str]:
    """
    Generating token method
    :param login_form: form to logging in/out
    :return: json with generated token value
    """
    return {"access_token": login_form.username + "_token"}


@app.get("/current_datetime")
async def get_datetime(token_value: str = Depends(oauth2_scheme)) -> dict[str, Any]:
    """
    Returns current data
    :param token_value: token giving access to this method
    :return: json with current date
    """

    return {"current_time": datetime.now()}


@app.get("/prime/{number}")
async def prime_number_checker(number: Any) -> dict[str, str]:
    """
    Checks if given number is a prime number
    :param number: number to check
    :return: True if number is prime, otherwise False. In case of any error raises BaseError.
    """
    try:
        prime_num_validator.validate_number(number)
        message = primefac.isprime(int(number))
    except BaseError as ex:
        return {"error": ex.message}
    return {"is_prime": message}


@app.post("/picture/invert")
async def image_inverter(file: UploadFile = File(...)) -> Union[FileResponse, dict[str, str]]:
    """
    inverts image, returns inversed file to download
    :param file: uploaded file
    :return: FileResponse if saving image worked correctly, otherwise json with error description
    """
    contents = await file.read()
    numpy_array = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)
    return_img = ImageHelper.process_image(img)

    _, encoded_img = cv2.imencode('.png', return_img)
    filepath = os.getcwd() + "/test_image.png"
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="image/jpeg", filename="test_image.png")
    return {"error": "File doesn't exist."}
