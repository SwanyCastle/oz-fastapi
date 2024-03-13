from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO

from model.predict import predict

app = FastAPI()

@app.post("/predict/image")
async def predict_img(file: UploadFile = File(...)):
    # 예외 처리
    extension = file.filename.split('.')[-1] in ('jpg', 'png', 'jpeg')

    if not extension:
        return "Change the extension"
    
    img = Image.open(BytesIO(await file.read()))

    print('img type: ', type(img))

    result = predict(img)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)