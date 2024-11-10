from io import BytesIO

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.model_utils import load_trained_model, predict
from app.preprocess_util import preprocess_image

router = APIRouter()
model = load_trained_model()

@router.get("/")
async def info():
    return {"message": "Hello, from FloodSight"}


@router.post("/validate")
async def validate_image(file: UploadFile = File(...)):
    try:
        file_content = await file.read()
        image_stream = BytesIO(file_content)
        preprocessed_image = preprocess_image(image_stream)
        result = predict(model, preprocessed_image)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))