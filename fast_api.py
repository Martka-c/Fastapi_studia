import base64

import cv2
import numpy as np
import primefac

from fastapi import FastAPI, File, UploadFile
from error_types import BaseError
from image_helper import ImageHelper
from prime_number_supervisor import PrimeNumber


IMAGEDIR = "fastapi-images/"
app = FastAPI()


@app.get("/prime/{prime_number}")
async def is_prime_number(prime_number: str):
	try:
		PrimeNumber.validate_number(prime_number)
		message = primefac.isprime(int(prime_number))
	except BaseError as ex:
		message = ex.message
	return {"message": message}


@app.post("/analyze")
async def analyze_route(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img_dimensions = str(img.shape)
    return_img = ImageHelper.process_image(img)

    # line that fixed it
    _, encoded_img = cv2.imencode('.PNG', return_img)

    encoded_img = base64.b64encode(encoded_img)

    return{
        "message": "done"
    }